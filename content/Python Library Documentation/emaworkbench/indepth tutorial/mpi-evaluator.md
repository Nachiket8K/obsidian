---
title: "MPIEvaluator: Run on multi-node HPC systems"
source: "https://emaworkbench.readthedocs.io/en/latest/indepth_tutorial/mpi-evaluator.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# MPIEvaluator: Run on multi-node HPC systems

The `MPIEvaluator` is a new addition to the EMAworkbench that allows experiment execution on multi-node systems, including high-performance computers (HPCs). This capability is particularly useful if you want to conduct large-scale experiments that require distributed processing. Under the hood, the evaluator leverages the `MPIPoolExecutor` from `` `mpi4py.futures `` <<https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html>>`\_\_.

## Limitations

- Currently, the MPIEvaluator is only tested on Linux and macOS, while it might work on other operating systems.
- Currently, the MPIEvaluator only works with Python-based models, and won’t work with file-based model types (like NetLogo or Vensim).
- The MPIEvaluator is most useful for large-scale experiments, where the time spent on distributing the experiments over the cluster is negligible compared to the time spent on running the experiments. For smaller experiments, the overhead of distributing the experiments over the cluster might be significant, and it might be more efficient to run the experiments locally.

The MPIEvaluator is experimental and its interface and functionality might change in future releases. We appreciate feedback on the MPIEvaluator, share any thoughts about it at <https://github.com/quaquel/EMAworkbench/discussions/311>.

## Contents

This tutorial will first show how to set up the environment, and then how to use the MPIEvaluator to run a model on a cluster. Finally, we’ll use the [DelftBlue supercomputer](https://doc.dhpc.tudelft.nl/delftblue/) as an example, to show how to run on a system which uses a SLURM scheduler.

### 1. Setting up the environment

To use the MPIEvaluator, MPI and mpi4py must be installed.

Installing MPI on Linux typically involves the installation of a popular MPI implementation such as OpenMPI or MPICH. Below are the instructions for installing OpenMPI:

#### 1a. Installing OpenMPI

*If you use conda, it might install MPI automatically along when installing mpi4py (see 1b).*

You can install OpenMPI using you package manager. First, update your package repositories, and then install OpenMPI:

For **Debian/Ubuntu**: `bash    sudo apt update    sudo apt install openmpi-bin libopenmpi-dev`

For **Fedora**: `bash    sudo dnf check-update    sudo dnf install openmpi openmpi-devel`

For **CentOS/RHEL**: `bash    sudo yum update    sudo yum install openmpi openmpi-devel`

Many times, the necessary environment variables are automatically set up. You can check if this is the case by running the following command:

```
mpiexec --version
```

If not, add OpenMPI’s `bin` directory to your `PATH`:

```
export PATH=$PATH:/usr/lib/openmpi/bin
```

#### 1b. Installing mpi4py

The python package mpi4py needs to installed as well. This is most easily done [from PyPI](https://pypi.org/project/mpi4py/), by running the following command:

```
pip install -U mpi4py
```

### 2. Creating a model

First, let’s set up a minimal model to test with. This can be any Python-based model, we’re using the `` `example_python.py `` <<https://emaworkbench.readthedocs.io/en/latest/examples/example_python.html>>`\_\_ model from the EMA Workbench documentation as example.

We recommend crafting and testing your model in a separate Python file, and then importing it into your main script. This way, you can test your model without having to run it through the MPIEvaluator, and you can easily switch between running it locally and on a cluster.

#### 2a. Define the model

First, we define a Python model function.

```
[ ]:
```

```
def some_model(x1=None, x2=None, x3=None):
    return {"y": x1 * x2 + x3}
```

Now, create the EMAworkbench model object, and specify the uncertainties and outcomes:

```
[ ]:
```

```
from ema_workbench import (
    Model,
    RealParameter,
    ScalarOutcome,
    ema_logging,
    perform_experiments,
)

if __name__ == "__main__":
    # We recommend setting pass_root_logger_level=True when running on a cluster, to ensure consistent log levels.
    ema_logging.log_to_stderr(level=ema_logging.INFO, pass_root_logger_level=True)

    ema_model = Model("simpleModel", function=some_model)  # instantiate the model

    # specify uncertainties
    ema_model.uncertainties = [
        RealParameter("x1", 0.1, 10),
        RealParameter("x2", -0.01, 0.01),
        RealParameter("x3", -0.01, 0.01),
    ]
    # specify outcomes
    ema_model.outcomes = [ScalarOutcome("y")]
```

#### 2b. Test the model

Now, we can run the model locally to test it:

```
[ ]:
```

```
from ema_workbench import SequentialEvaluator

with SequentialEvaluator(ema_model) as evaluator:
    results = perform_experiments(ema_model, 100, evaluator=evaluator)
```

In this stage, you can test your model and make sure it works as expected. You can also check if everything is included in the results and do initial validation on the model, before scaling up to a cluster.

### 3. Run the model on a MPI cluster

Now that we have a working model, we can run it on a cluster. To do this, we need to import the `MPIEvaluator` class from the `ema_workbench` package, and instantiate it with our model. Then, we can use the `perform_experiments` function as usual, and the MPIEvaluator will take care of distributing the experiments over the cluster. Finally, we can save the results to a tarball, as usual.

```
[ ]:
```

```
# ema_example_model.py
from ema_workbench import (
    Model,
    MPIEvaluator,
    RealParameter,
    ScalarOutcome,
    ema_logging,
    perform_experiments,
    save_results,
)

def some_model(x1=None, x2=None, x3=None):
    return {"y": x1 * x2 + x3}

if __name__ == "__main__":
    ema_logging.log_to_stderr(level=ema_logging.INFO, pass_root_logger_level=True)

    ema_model = Model("simpleModel", function=some_model)

    ema_model.uncertainties = [
        RealParameter("x1", 0.1, 10),
        RealParameter("x2", -0.01, 0.01),
        RealParameter("x3", -0.01, 0.01),
    ]
    ema_model.outcomes = [ScalarOutcome("y")]

    # Note that we switch to the MPIEvaluator here
    with MPIEvaluator(ema_model) as evaluator:
        results = evaluator.perform_experiments(scenarios=10000)

    # Save the results
    save_results(results, "ema_example_model.tar.gz")
```

To run this script on a cluster, we need to use the `mpiexec` command:

```
mpiexec -n 1 python ema_example_model.py
```

This command will execute the `ema_example_model.py` Python script using MPI. MPI-specific configurations are inferred from default settings or any configurations provided elsewhere, such as in an MPI configuration file or additional flags to `mpiexec` (not shown in the provided command). The number of workers that will be spawned by the MPIEvaluator depends on the MPI universe size. The way this size can be controlled depends on which implementation of MPI you have. See the discussion in
[the docs of mpi4py for details](https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html#examples).

The output of the script will be saved to the `ema_mpi_test.tar.gz` file, which can be loaded and analyzed later as usual.

### Example: Running on the DelftBlue supercomputer (with SLURM)

As an example, we’ll show how to run the model on the [DelftBlue supercomputer](https://doc.dhpc.tudelft.nl/delftblue/), which uses the SLURM scheduler. For the latest configuration of the cluster see [Delft Blue system configuration](https://www.tudelft.nl/dhpc/system).

*These steps roughly follow the*[DelftBlue Crash-course for absolute beginners](https://doc.dhpc.tudelft.nl/delftblue/crash-course/)*. If you get stuck, you can refer to that guide for more information.*

#### 1. Creating a SLURM script

First, you need to create a SLURM script. This is a bash script that will be executed on the cluster, and it will contain all the necessary commands to run your model. You can create a new file, for example `slurm_script.sh`, and add the following lines:

```
#SBATCH --job-name="Python_test"
#SBATCH --time=00:06:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --partition=compute
#SBATCH --mem-per-cpu=3968mb
#SBATCH --account=research-tpm-mas

module load 2024r1
module load openmpi
module load python

mpiexec -n 1 python3 example_mpi_lake_model.py
```

Modify the script to suit your needs:

- Set the `--job-name` to something descriptive.
- Update the maximum `--time` to the expected runtime of your model. The job will be terminated if it exceeds this time limit.
- Set the `--ntasks` to the number of cores you want to use. Each node in DelftBlue currently has 48 cores, so for example `--ntasks=96` might use two nodes, but can also be distributed over more nodes. Note that using MPI involves quite some overhead. If you do not plan to use more than 48 cores, you might want to consider using the MultiprocessingEvaluator and request exclusive node access (see below).
- Update the memory `--mem-per-cpu` to the amount of memory you need per core. Each node has 192 GB of memory, so you can use up to 4 GB per core.
- Add `--exclusive` if you want to claim a full node for your job. In that case, specify `--nodes` next to `--ntasks`. Requesting exclusive access to one or more nodes will delay you scheduling time, because you need to wait for the full nodes to become available.
- Set the `--account` to your project account. You can find this on the [Accounting and Shares](https://doc.dhpc.tudelft.nl/delftblue/Accounting-and-shares/) page of the DelftBlue docs.

See [Submit Jobs](https://doc.dhpc.tudelft.nl/delftblue/Slurm-scheduler/) at the DelftBlue docs for more information on the SLURM script configuration.

Then, you need to load the necessary modules. You can find the available modules on the [DHPC modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) page of the DelftBlue docs. In this example, we’re loading the 2024r1 toolchain, which includes Python 3.10, and then we’re loading the necessary Python packages.

Finally, the script uses `mpiexec` to run Python script in a way that allows the MPIEvaluator to distribute the experiments over the cluster. The `-n 1` argument meanst that we only start a single process. This main process in turn will spawn additional worker processes. The number of worker processes that will spawn defaults to the value of `--ntasks` - 1.

Note that the bash scripts (sh), including the `slurm_script.sh` we just created, need LF line endings. If you are using Windows, line endings are CRLF by default, and you need to convert them to LF. You can do this with most text editors, like Notepad++ or Atom for example.

**additional non standard dependencies**

You might want to install additional Python packages. It is critical that if you install local packages, that you do this using the same modules as you load in your slurm script. So, in this case, we would first neeed to do

```
[netid@login3 netid]$ module load 2024r1
[netid@login3 netid]$ module load python
[netid@login3 netid]$ module load py-pip
```

This makes sure we use the same python installation as used in the slurm script. We also seperately need to load pip so that it is available from the command line. With this out of the way, we can install our packages. You can do this with `pip install -U --user <package>`. Note that you need to use the `--user` flag, because you don’t have root access on the cluster. To install the EMA Workbench, you can use `pip install -U --user ema_workbench`. If you want to install a development
branch, you can use `pip install -e -U --user git+https://github.com/quaquel/EMAworkbench@<BRANCH>#egg=ema-workbench`, where `<BRANCH>` is the name of the branch you want to install.

Packages installed in this way can be found `/home/<netid>/.local/lib/<python version>`.

If you need a more complicated setup or want to use conda to manage your virtual environemnt, please check the delft blue documentation for further information.

#### 1. Setting up the environment

First, you need to log in on DelftBlue. As an employee, you can login from the command line with:

```
ssh <netid>@login.delftblue.tudelft.nl
```

where `<netid>` is your TU Delft netid. You can also use an SSH client such as [PuTTY](https://www.putty.org/).

As a student, you need to jump though an extra hoop:

```
ssh -J <netid>@student-linux.tudelft.nl <netid>@login.delftblue.tudelft.nl
```

Note: Below are the commands for students. If you are an employee, you need to remove the `-J <netid>@student-linux.tudelft.nl` from all commands below.

Once you’re logged in, you want to jump to your scratch directory (note it’s not but is not backed up).

```
cd ../../scratch/<netid>
```

Create a new directory for this tutorial, for example `mkdir ema_mpi_test` and then `cd ema_mpi_test`

Then, you want to send your Python file and SLURM script to DelftBlue. Make sure your files are all in one folder. Open a **new** command line terminal, `cd` in the folder where your files are, and then send the files with `scp`:

```
scp -J <netid>@student-linux.tudelft.nl ema_example_model.py slurm_script.sh <netid>@login.delftblue.tudelft.nl:/scratch/<netid>/ema_mpi_test
```

Now go back to your original cmd window, on which you logged in on DelftBlue. Before scheduling the SLURM script, we first have to make it executable:

```
chmod +x slurm_script.sh
```

Then we can schedule it:

```
sbatch slurm_script.sh
```

Now it’s scheduled!

You can check the status of your job with `squeue`:

```
squeue -u <netid>
```

You might want to inspect the log file, which is created by the SLURM script. You can do this with `cat`:

```
cat slurm-<jobid>.out
```

where `<jobid>` is the job ID of your job, which you can find with `squeue`.

When the job is finished, we can download the tarball with our results. Open the command line again (can be the same one as before), and you can copy the results back to your local machine with `scp`:

```
scp -J <netid>@student-linux.tudelft.nl <netid>@login.delftblue.tudelft.nl:/scratch/<netid>/ema_mpi_test/ema_mpi_test.pickle .
```

Finally, we can clean up the files on DelftBlue, to avoid cluttering the scratch directory:

```
cd ..
rm -rf "ema_mpi_test"
```

```
[ ]:
```

```

```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/indepth_tutorial/mpi-evaluator.html
