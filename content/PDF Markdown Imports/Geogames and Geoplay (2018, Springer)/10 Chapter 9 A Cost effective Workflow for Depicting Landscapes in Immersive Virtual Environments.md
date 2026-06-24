---
title: "Chapter 9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual Environments"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual Environments** 

## **Nathaniel J. Henry** 

## **9.1  Introduction** 

Geogames draw inspiration from two technologies: geographic information science (GIS) and video games. These technologies share a common history that stretches back to the invention of ancient “map games” such as chess and Go. Both fields have advanced rapidly in the past two decades, spurred by the rapid expansion of computer graphical and processing capabilities (Ahlqvist 2011). GIS analysts and video game designers might be surprised by the similarity of their data management techniques: both rely on hierarchical data management structures, employ techniques for minimizing processor loads when representing complex scenes, and use layers to organize their data sources (Shepherd and Bleasdale-Shepherd 2009). Overlapping engagements with simulation, multi-party collaboration, and the web indicate that GIS and video game technologies may be headed down converging paths (Ahlqvist 2011). 

Despite these commonalities, GIS and video games diverge sharply in their representations of space and place. Shepherd and Bleasdale-Shepherd (2009) explain this difference in terms of reality, the extent to which a technology describes the world as it actually exists, and realism, which describes the representational system used to display game objects and phenomena. King and Krzywinska (2003) add another factor for consideration: the perspective through which end users view and interact with the represented environment. The user could view the world through the eyes of a virtual character (first-person perspective) or peek over that character’s shoulder (third-person perspective). Otherwise, they might observe the world at a distance by looking down from an oblique or vertical angle. GIS and video game scholars have labeled the final two perspectives as “managerial” or “god'seye” views, and one need only play top-down games such as **Sim City** or 

N.J. Henry ( * ) The Ohio State University, Columbus, OH, USA e-mail: henry.557@osu.edu 

**==> picture [14 x 7] intentionally omitted <==**

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_9 

178 

N.J. Henry 

**Civilization** to understand why: in these games, the user often exerts greater control over the game landscape, and keeps a constant watch for decades or centuries of in-game time. 

When compared on the axes of reality, realism, and perspective, video games exhibit a greater variety in representational forms and content than GIS. Video games can depict worlds ranging from semi-historical to entirely fantastic; their depictions can be as symbolic as geometric shapes or almost as naturalistic as the real world; and players can experience games from any of the perspectives listed above and more. On the other hand, technical and thematic constraints have historically limited GIS technology to representing the world as it exists, using largely symbolic forms of representation such as markers and color gradients, from a topdown or oblique perspective (Shepherd and Bleasdale-Shepherd 2009). Additionally, realistically depicting real-world landscapes may require prohibitively high levels of effort and technological specialty for most GIS research groups. Geogames may have adopted video game technologies and formats, but current implementations often follow the reality-realism-perspective combination dictated by conventional GIS. 

In gaming, representation and perspective are more than just virtual window dressing; they ultimately determine how players will experience all phenomena in the game world. Representational style and perspective factor into the player's sense of presence, defined as “a physical sensation of complete submersion in a digital medium” (Denisova and Cairns 2015). In turn, the player’s sense of presence in the game-world can facilitate immersion, a feeling of engrossment with the narrative content of the game. Empirical studies confirm the relationship between realism, representation, presence, and immersion: according to studies conducted Denisova and Cairns (2015), people were more immersed in gameplay when they experienced it from a first-person perspective, regardless of stated preference. Additional research from Sylaiou et al. (2010) found a statistically significant correlation between a user’s sense of presence in a virtual reality environment and their enjoyment of the scenes being depicted. Certainly, surface realism and viewpoint alone are insufficient to spark immersion. Other key contributors to game immersion include intuitive game interfaces, narrative, and character-building (Taylor 2002; Bayliss 2007). However, games rendered in a naturalistic style and viewed from a first-person perspective may facilitate more engaging narrative types and stronger connections with in-game characters, further increasing the likelihood of player immersion. 

This chapter outlines an inexpensive workflow for representing real-world landscapes as three-dimensional (3D) virtual environments in a video game engine. By relying on inexpensive methods of data collection and an automated process for 3D reconstruction based on computer vision software, the workflow lowers the barriers for high-fidelity video game representations of existing landscapes. The following section defines key terminology relating to three-dimensional game environments. It then describes existing representations of real-world places, spaces, and phenomena in virtual environments, and explores commons advantages and disadvantages of these implementations. Next, the workflow is described in detail. Finally, the workflow’s implications for geogame creation are discussed and possible extensions are proposed. 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

179 

## **9.2  Modeling the World in Three Dimensions: Immersive Virtual Environments and Their Applications** 

Geogames are not the first applications to model real-world landscapes in a threedimensional virtual environment; a number of researchers have already attempted to do so on behalf of commercial, academic, and government organizations. Understanding the successes and challenges of these attempts can inform the ways that geogames engage with 3D technologies. 

While the following examples might differ in format, content, and purpose, they all aim to represent existing landscapes and phenomena in immersive virtual environments. A virtual environment can be broadly defined as a computer-generated spatial environment (Magee 2011). In the context of this chapter, immersive virtual environments refer to virtual environments formatted in a way that facilitates user immersion: that is, virtual environments rendered in three dimensions, tending towards naturalistic rather than symbolic representations, and allowing the user to view the world from a first-person or third-person perspective. 

Virtual environments encompass a broad range of possible forms and content types, so specific implementations are often better described with a more specific sub-category. Virtual worlds, for example, are multi-user virtual environments which emphasize social interaction. In virtual worlds such as **Eve Online** , **Second Life** , and **Active Worlds** , users can simulate real or fictional lives and interact with others through the use of in-world avatars (Loke 2015). On the other end of the spectrum, serious games and simulations impart contextual knowledge or skills on users by engaging them with representations of specific real-world situations (Cain and Piascik 2015; Šimic 2012). And while most users currently engage with 3D digital landscapes through a screen, the fast-developing field of virtual reality aims to provide more intuitive tools for experiencing and manipulating virtual environments (Magee 2011). 

Commercial video games have been representing real-world landscapes in three dimensions since the late 1990s, when the iconic video game protagonist Lara Croft navigated the bank of the River Thames and the roof of St. Paul’s Cathedral as part of the classic **Tomb Raider** series. However, this chapter will focus on more recent experimental applications of 3D virtual environments in academia, health services, and the military. In these fields, researchers have created virtual representations of the real world in order to solve a problem or improve an existing process, from recruit training to historic preservation. These implementations can be categorized into two types: the educational, archaeological, and archival applications, which tend to focus on user engagement and learning; and the military, health care, and emergency response applications, which tend to focus on user training and professionalization. Implementations of the same category tend to encounter similar types of successes and challenges due to their shared purposes and related institutional contexts. Given the tendency for past geogames to focus on learning and exploration, three-dimensional geogames would likely fall into the first of these categories. 

180 

N.J. Henry 

## _**9.2.1  Virtual Landscapes as a Tool for Engagement and Learning**_ 

For educators, archaeologists, and historians, three-dimensional virtual environments hold promise as a pedagogical tool. According to Dickey (2005), if education is a social practice, then video games and virtual worlds can serve as social platforms, enabling activities and narratives that lead to learning. Users in virtual environments can interact with types of data and knowledge representations that are not simply not possible in a classroom setting. Additionally, virtual learning environments may be a more attractive learning option for a younger generation of “digital natives” (Chau et al. 2013). With these goals in mind, a number of researchers have taught courses set in online virtual worlds, where students attend lectures in reconstructed classrooms, “meet up” with their avatars to complete group assignments, and even explore the virtual equivalents of their college campus together (Dickey 2005; Ritzema and Harris 2008; Fominykh et al. 2011; Chau et al. 2013). 

Archaeologists and historians in particular have engaged with 3D technology as a new way to share and explain the past. Virtual environments and virtual reality hold great potential as storytelling tools: like a good story, they can transport the user into a world conceived by the “author” and impart meaning, resulting in greater empathy and understanding of the content being displayed. There is also a hope that virtual environments will attract a wider audience of people, especially young people, to explore their own history (Dawson et al. 2011). Past applications of 3D within the fields of archaeology and archival studies have included a digital reconstruction of the Parthenon in Athens, a digital museum of Chinese culture in anticipation of the 2008 Beijing Olympics, and the depiction of Thule whalebone houses and Siglit-Inuvialit sod houses in virtual reality (Punzalan 2014; Pan et al. 2009; Dawson et al. 2011). 

Several educational studies concluded that courses in virtual worlds can enhance aspects of student engagement and enjoyment. Dickey (2005) describes how one of her courses surged in popularity after a virtual world version was created. Chau et al. (2013) found that students who participated in a virtual world course reported higher levels of satisfaction than their offline counterparts, and were particularly happy with the flexibility and geographic freedom offered by the online course. In terms of emotional engagement, Dawson et al. (2011) also received strong positive feedback about their virtual reality reconstructions of whalebone and sod houses. After a group of Inuit Elders viewed the reconstructed dwellings in 3D, they reported an increased sense of connectedness with their past. As one commented, “all the stories I used to hear when I was young are coming back to me. It really makes me think about what it would have been like to live in my ancestors’ home.” (Dawson et al. 2011). 

However, if a user experiences technical issues, it can transform the 3D experience into a frustrating endeavor far worse than traditional methods of learning. Chau et al. (2013) identified connectivity issues and difficulties learning the user interface as two common pitfalls for students enrolled in their virtual course. Students with less technical savvy face the greatest barriers to engagement in virtual world-based courses, and they can easily fall behind if the instructor does not inter- 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

181 

vene. Finally, in situations where fidelity to the real world is important, dishonest replication could lead to digital “forgeries” that misinform users about the topic at hand (Punzalan 2014). 

## _**9.2.2  Virtual Environments as a Tool for Training and Professionalization**_ 

Serious games that depict real landscapes and situations have already received significant attention as potential training platforms for medical, military, and emergency response professionals. Serious games and simulations have an obvious appeal when it comes to training exercises: as researchers have noted, “the use of simulation is a safe and inexpensive way to prepare and educate people on how to respond to emergencies” (Sharma and Otunba 2012). Using serious games and simulations, these fields can acclimate players to stressful situations, test costly equipment, and reproduce complex systems that would be impractical or dangerous to emulate in real life (Roman and Brown 2008; Boosman and Szczerba 2010). Past 3D applications have included simulators for airplane evacuation, flooding on a naval ship, unit navigation in an urban environment, and networked medical devices in a hospital ward (Sharma and Otunba 2012; Hussain et al. 2009; van der Hulst et al. 2013). Within NATO alone, militaries from at least five countries have adopted serious games as a core training platform (van der Hulst et al. 2013). Military strategists are also attempting to implement tools from the developing field of virtual reality in order to gain a competitive advantage over their adversaries (Magee 2011). 

Evidence indicates that virtual environments can serve as an effective vehicle for contextual training and learning. A number of studies have concluded that serious games can successfully impart knowledge and attitudes on military recruits (discussed in Roman and Brown 2008). Naval recruits who participated in a 3D flooding control simulation displayed more confidence during a real-life test than a control group who attended a class on the topic (Hussain et al. 2009). On the other hand, learners and trainees may not always receive the intended lesson: clunky artificial intelligence, lack of proper physics modeling, and the realism of rendered objects may render some serious games and simulations useless for medical, military, or emergency response training (van der Hulst et al. 2013). Additionally, on- screen simulations do not always replicate the stress of actual emergency situations, so some learners may not take these virtual lessons seriously (Sharma and Otunba 2012: 572). 

## _**9.2.3  Cost and Feasibility Challenges to Digitally Recreating the Real World**_ 

When it comes to the cost and feasibility of creating and implementing immersive virtual environments, training applications in the medical, military, and emergency response fields are subject to different considerations than applications intended for 

182 

N.J. Henry 

education or community outreach. Despite their high cost, 3D training applications offer a cheaper and safer alternative to testing expensive equipment or recreating potentially dangerous scenarios in person. As a result, their expected cost is actually lower than the current systems in place (Sharma and Otunba 2012). Large organizations such as medical institutions or militaries possess the computational resources and technical capabilities to generate large areas of realistic terrain and simulate complex processes (Roman and Brown 2008; Boosman and Szczerba 2010). The major barriers to 3D virtual training applications relate to institutional acceptance and the current lack of standard procedures for creating virtual environments (Magee 2011). 

Educators, archaeologists, and historians face the opposite set of problems: fewer institutional barriers stand in the way, but virtual environments are often too costly or technically difficult for widespread implementation. Educators who currently wish to construct their campus in a virtual environment must choose between expending an enormous amount of time building it by hand, or else create an automated reconstruction using expensive equipment such as a laser scanner. Tools for visualizing virtual environments, such as 3D headsets and CAVE devices, can be expensive and are not available to most educators (Loke 2015). For programs that operate on limited budgets, Dawson et al. (2011) worry that the time and money used to construct digital representations of the world would be better spent on programs that provide material content and benefits to target groups. 

Three-dimensional geogames would likely experience successes and face challenges similar to those found in existing educational, archaeological, and archival implementations. By representing landscapes as immersive virtual environments, geogames could reap the benefits in user enjoyment, presence, and learning outcomes reported by these implementations. However, if geogame designers are forced to reconstruct real 3D landscapes from scratch, they will likely encounter the same intractable feasibility issues. 

As an alternative to these methods, the next section introduces an automated workflow for digitizing existing landscapes into immersive virtual environments. Instead of using expensive or technically difficult tools, this process relies on simple data collection technologies and a user-friendly computer vision software. It takes far less time to complete than manually reconstructing a scene in a virtual environment, and the equipment involved is less expensive than standard 3D scanning equipment. Taken as a whole, this workflow is expected to reduce the barriers for representing high-fidelity virtual environments in geogames. 

## **9.3  Using Kite Aerial Photography and Computer Vision Software to Create Immersive Digital Environments** 

This process draws on multiple existing workflows for kite aerial photography and 3D scene reconstruction. Geert Verhoeven (2009, 2011) describes a number of methods used to obtain low altitude aerial photographs, and then details how these 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

183 

aerial photographs can be reconstructed into a three-dimensional digital surface using computer vision software. Olson et al. (2013) employ this process to record an archaeological site at a high spatial and temporal resolution, with an emphasis on quickly processing and storing three-dimensional data. Using a similar workflow, Currier (2015) creates a high-resolution orthographic photo mosaic of a remote Indonesian island, then assesses the resolution and accuracy of photo mosaics and digital elevation models (DEMs) that can be produced using this process. Aspects from each of these studies will be discussed in greater detail below. This chapter extends existing methods by importing a photo mosaic and DEM into a free, widelyused video game engine. The result of this workflow (Fig. 9.1) is a landscape that can be used as the basis for a playable game level. 

The workflow is outlined below, and more specific technical considerations are enumerated within Table 9.1. 

During the summer of 2014, this process was employed to digitize a stretch of beach-side cliffs at Campus Point in Santa Barbara, California. The data collection, scene reconstruction, and playable landscape creation will be discussed in turn, using the digitization of the Campus Point cliffs as an example. 

## _**9.3.1  Data Collection**_ 

Verhoeven (2009) describes the many data collection options available for capturing low-altitude aerial photographs of a study area. While booms and poles, balloons, kites, and unmanned aerial vehicles (UAVs) can all be employed, the most appealing option for many researchers is also one of the oldest: a camera rig attached to a kite. Kite aerial photography (KAP) dates back to the late 1800s; today, it is a highly popular method for aerial photography due to its portability, durability, and low cost (Verhoeven 2009). Unlike balloon photography, kite aerial photography requires only a single initial purchase; and in most areas of the United States, kites can be flown up to 150 m above the ground without regulations, while UAVs are subject to a set of stricter and frequently-changing regulations (Currier 2015). Additionally, for data collection in populous areas, negative perceptions of UAVs may color public opinion regarding the research, whereas kites are far more likely to spark positive interest and engagement. This survey used a delta kite with a width of 3.4 m, along with two tails for stability in high winds. 

Kites do introduce limitations into the circumstances under which data can be collected: the survey area must be fairly open and free of aerial obstructions such as telephone wires or tree branches. Additionally, kites can only be operated with a steady wind speed of 10–25 km/h. In this sense, they are somewhat complementary to drones and balloons, which require low wind speeds for successful operation. However, given these two conditions, a kite can successfully and reliably lift the camera rig used for aerial photo capture. 

Attached to the kite is a rig holding a downward-facing camera that shoots pictures at regular intervals. The rig itself is a simple metal frame that can be readjusted to 

184 

N.J. Henry 

**Fig. 9.1** A general workflow for depicting a real-world landscape in an immersive digital environment 

angle the camera in various directions. The camera is attached to the metal rig using a screw, and the rig is attached to the kite with a picavet cross, a suspension system designed to maximize the stability of the rig. The camera itself is an inexpensive 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

185 

**Table 9.1** Equipment, best practices, and settings used within the workflow 

|Processingstep|Hardware and software|Specifcations used|
|---|---|---|
|Kite aerial<br>photography|11-ft Delta Kite; Canon<br>Powershot S100 with the<br>Canon Hack<br>Development Kit; KAP<br>Rig|_Camera_: Focal distance of infnity; shutter<br>speed of 1/500 s; f/8 aperture; ISO greater than<br>400 (Smith et al.2009, in Currier2015)<br>_Control Points_: Set at least three; optimal results<br>with ten or more (Agisoft2016)<br>_Recording:_KAP rig hung approximately 20 m<br>below the kite (Currier2015); pictures taken at<br>10 s intervals from both vertical and oblique<br>angles|
|Photo selection|Photo viewing program|Photos should have 80% overlap on a path, 60%<br>side-by-side overlap; photos with blurry or<br>moving objects should be excluded (Agisoft<br>2016)|
|Creating point<br>cloud|Agisoft PhotoScan|_Aligning Cameras_: High accuracy; “Generic”<br>preselection_Dense Cloud_: Medium quality (to<br>speed up processing)|
|Creating 3D<br>mesh|Agisoft PhotoScan|_Mesh_: Height Field surface type; Extrapolated<br>interpolation; Dense Cloud as source data.<br>_Texture:_Orthophoto mode; Mosaic blending<br>_DEM Output_: GeoTIFF with square power-of-<br>two dimensions (such as 4096 × 4096 px)<br>_Orthophoto Output_: PNG with same dimensions<br>as the DEM|
|DEM conversion|FIJI|Convert the DEM GeoTIFF to a 16-bit<br>grayscale PNG image|
|Importing to<br>game engine|Unreal Engine 4|_DEM_: Import the PNG image using the<br>Landscape “import from fle” option (Epic<br>Games2015a)_Orthophoto_: Import by creating a<br>new Material with a “tile size” equal to the<br>Landscape dimensions, then applying it to the<br>Landscape as a base color(Epic Games2015b)|
|Post-processing<br>and cleanup|Unreal Engine 4|Rotate and resize the landscape to scale using<br>the object properties; erase areas with no data<br>using the landscape editing toolbar (Epic Games<br>2015c); adjust key game controls such as the<br>level’s starting point|



Canon point-and-shoot device running the Canon Hack Development Kit, a firmware package that extends the functionality of Canon cameras (CHDK User Manual 2016); using this kit, an interval timer can be installed on the camera at no cost. 

The Campus Point cliffs are in many ways an ideal location for kite aerial photography, due to the regular sunny weather, consistent wind, and lack of aerial obstructions. Additionally, because most of the terrain is composed of rock, sand, or dense low-lying vegetation, the cliffs are also a suitable subject for computer vision reconstruction, which can be confused by shifting objects (Agisoft 2016). However, although the game engine only imports square elevation models, the terrain could only be recorded as a long, thin strip; while the cliffs run for kilometers from the University of California at Santa Barbara to the nearby city of Isla Vista, they are 

186 

N.J. Henry 

bordered by the ocean on one side and a lagoon on the other, allowing for less than 30 m of navigable space in some areas. This meant that a square DEM was exported with many areas of no elevation data, and these unmapped areas were later removed from the video game landscape. Ultimately, a stretch of cliffs approximately 500 m long and 50 m across was processed for this study. 

Aerial photographs were collected by repeatedly flying the KAP rig, at an elevation of approximately 100 m, across the study area in a straight line. Each pass across the study area was parallel and overlapping with previous passes. Additionally, to better capture rough terrain, the camera angle was adjusted to collect downwardsfacing and oblique shots on different passes (Verhoeven 2011). Over the course of several runs, more than 1000 aerial photographs of the study area were collected. 

In addition to aerial photographs, a number of ground control points were collected using brightly-colored markers and a GPS device. The markers were created using high-contrast colors in order to simplify identification from a distance. For this study, five ground control points were collected using both temporary and permanent markers. Latitude, longitude, and elevation were collected for each marker using a GPS device. 

## _**9.3.2  Three-Dimensional Reconstruction**_ 

After collecting aerial photographs and ground control points, the study area was reconstructed as a three-dimensional point cloud, and then as a mesh, using computer vision software. Put simply, computer vision is a science that recreates three- dimensional objects from two-dimensional images using mathematical algorithms, a process sometimes referred to as “structure from motion” (Verhoeven 2011). According to Olson et al. (2013), much like the human brain can comprehend a three-dimensional object by viewing it from multiple angles, an algorithm can determine relative positions of points in 3D space by viewing them across multiple images. A software employing computer vision can use these spatial relationships to construct a set of points in 3D space, known as a point cloud. After an initial, “sparse” point cloud is constructed, the software uses it as a reference to reconstruct a more detailed set of geometries known as the “dense” point cloud (Olson et al. 2013). Finally, the software joins the dense point cloud together into a mesh and overlays textures and colors retrieved from the input images, recreating a 3D surface that is geometrically and visually similar to the original object (Agisoft 2016). 

This study used Agisoft PhotoScan Pro, a computer vision software that employs both photogrammetric and computer vision algorithms to reconstruct 3D surfaces. While many other options exist for recreating 3D objects, from free software such as 123D Catch and VisualSFM to the more expensive PhotoModeler Scanner and 3DM Analyst Pro, Agisoft PhotoScan Pro offers several advantages for 3D geogame creation. PhotoScan Pro sports an intuitive user interface that handles all aspects of the 3D reconstruction process, from adding photos to exporting the model. More importantly, the software allows users to georeference and export Digital Elevation 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

187 

Models, a crucial aspect of this workflow. The software has been well-documented in past studies and workflows (including Verhoeven 2011; Gatewing 2012; Olson et al. 2013; Currier 2015), allowing for further instruction and optimization. 

Of the aerial photographs taken over campus point, 200 were selected for 3D reconstruction. These photographs did not include blurry or moving objects, represented an appropriate amount of overlap between images, and included both oblique and downward-facing shots of the study area. The photographs were loaded into the software, where they can be viewed and edited. Several photographs showing the sky, moving objects such as people, or irregularly-shaped objects such as trees that would be poorly represented by a digital elevation model were masked and excluded from processing. The result of photo alignment is a sparse point cloud, the skeleton of the final model (Fig. 9.2). The sparse point cloud of the Campus Point cliffs contained 19,952 points before cleaning. 

After the photos have been aligned, ground control points can be marked and georeferenced in the original photographs. While each ground control point must be located in at least two input images to be correctly referenced, PhotoScan will automatically place markers in other images based on the photo alignment. After the markers have been placed and assigned Longitude, Latitude, and height, and expected accuracy, root mean square errors for the ground control points can be calculated. The user can also remove erroneous points in the sparse point cloud to improve the model's final geometry, and use the bounding box to restrict areas for further processing (Agisoft 2016). 

Once the model has been georeferenced and cleaned, the user can automatically create the dense point cloud using the sparse point cloud for reference. Since this step creates three-dimensional points based on all matched pairs between photos, the dense point cloud can end up having millions of vertices: the dense cloud for the Campus Point cliffs contained over 65 million points. This point cloud bears a striking resemblance to the original imagery even at a close range (Fig. 9.3). 

After the dense point cloud has been created, the user must carefully align the bounding box with the region of the study area that is to be exported into the game engine. The bounding box must be horizontal, with the plane of projection (represented by the red edge of the box) below the landscape. After properly aligning the bounding box and manually removing any erroneous points, the user can generate a high-resolution mesh, and then cover that mesh with a textured mosaic of the aerial photos (Fig. 9.4). 

Computer vision is resource-intensive; a model of several hundred photos can take days to process from start to finish. Several steps can be taken to reduce processing time: after aligning photos, users can split the project into “chunks”, each of which can be processed faster separately than as part of the overall model. Olson et al. (2013) recommend splitting projects with over 1000 photographs into chunks to reduce processing load. Users can also configure a dedicated GPU for 3D reconstruction, accelerating the process (Agisoft 2016). Additionally, users can choose to set the quality parameters at each step of the reconstruction to lower values, as slight variations in output quality may be negligible compared the increase in processing time (Olson et al. 2013). 

188 

N.J. Henry 

**Fig. 9.2** The sparse point cloud generated by Agisoft PhotoScan’s structure-from-motion algorithm. The _blue rectangles_ show the estimated position and alignment of the camera for each input photograph 

## _**9.3.3  Exporting to a Game Engine**_ 

Once a 3D model has been created, it can be exported as a wide variety of 3D formats, from .OBJ to .FBX and even .PDF. However, for compatibility with a game engine, two derived 2D images must be produced instead: a Digital Elevation Model (DEM) and an orthorectified photomosaic of the study area, also called an orthophoto. These two outputs can be converted into video game elements and deployed in Unreal Engine 4, an industry-leading game engine. This section will discuss Unreal Engine 4, the PhotoScan image exports, and how a few minor file conversions can allow for interoperability between the two software packages. 

Game engines are software applications that act as frameworks for game development. They render low-level processes such as object collision, loading, and user input, allowing for game developers to focus on the actual narrative and experience of a game (Ward 2008). With their reusable chunks of code and more accessible designer interfaces, game engines can help new developers quickly get a working game off of the ground. They are also invaluable assets for 3D game designers thanks to their automatic rendering of physics and 3D navigation. Using a game engine, geogames designers can quickly and easily turn 3D models into playable game levels. 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

189 

**Fig. 9.3** The dense point cloud generated in Agisoft PhotoScan 

**Fig. 9.4** The dense point cloud is connected to become a three-dimensional surface 

This study renders landscapes in Unreal Engine 4, the latest in a line of widelyused Unreal game engines. While other game engines could plausibly display this landscape, Unreal Engine 4 has several features that may appeal to geogames designers. The engine is free for most noncommercial research and education applications; its learning curve may be slightly friendlier, thanks to a large developer network and a scripting interface written in C++ (Masters 2015); and the game engine provides native support for virtual reality headsets such as the Oculus Rift, opening up further possibilities for immersive virtual reality in geogames. 

190 

N.J. Henry 

Unreal Engine 4 requires two types of inputs to import a landscape: a height map, which describes the landscape's contours, and materials, which describe the colors and textures of that landscape. First, the DEM must be exported from the 3D model and converted into a format compatible with the game engine. This application used FIJI, an open-source image editing software, to convert the image to the proper format (Schindelin 2012). Finally, the converted image was imported directly into Unreal Engine 4 as a Landscape surface (Epic Games 2015a), which can be resized, rotated, and edited using in-game tools (Epic Games 2015b, c). 

After the landscape has been appropriately formatted, it must be covered with textures from the 3D model in order to approximate appearance of the study area. This is accomplished by exporting an orthorectified photograph, or orthophoto, from the 3D model. Orthorectification is “a technique in which a photograph is differentially corrected using a DEM” (Currier 2015). Because of the correction, the resulting image or image mosaic corresponds exactly with the contours of the associated DEM. This photo can be imported into Unreal Engine 4 as a material, which can simply be dragged and dropped onto the map to recreate the subject area in high detail. Using this process, a 4096 × 4096 px orthophoto export from PhotoScan was converted into a material and placed on the landscape in Unreal Engine 4 (Fig. 9.5). Despite the oblong shape of the study area, which limited the possible dimensions of the orthophoto and DEM, the resulting ground features had a resolution equivalent to 6 cm. 

By placing the “level start” action somewhere on the landscape, the user is able to navigate a three-dimensional representation of the study area in the first person. In Fig. 9.6, the landscape is shown from the perspective of the game avatar. The resolution of the height map and texture are high enough for the user to recognize individual landscape features. 

**Fig. 9.5** The Campus Point cliffs recreated in the Unreal Engine 4 game engine 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

191 

**Fig. 9.6** From a first-person perspective, the user can identify ground objects ( _left_ ) and larger terrain features such as a rocky outcropping ( _right_ ) 

## **9.4  Discussion** 

This chapter has already discussed the potential impact of 3D immersive geogames and explored a workflow for reconstructing existing landscapes in three dimensions using computer vision software and a game engine. However, the benefits and pitfalls of this specific workflow have not yet been explored. Is this method worth the trouble of mastering kite aerial photography, photogrammetric reconstruction, and a new method for game design? 

From the perspectives of cost, time, and user experience, I argue that this workflow has much to offer geogames. All the major expenses of this process, including a kite, KAP rig, camera, GPS, and peripheral accessories can be obtained for less than US $1000 in total. These costs are incurred only once, and they provide the geogames creator with the tools to digitize new areas indefinitely. In terms of time spent, once the designer has mastered all aspects of data collection and transformation, the entire process should take less than 2 days of work. The majority of that time would be spent on kite aerial photography, which is pleasant, and processing in PhotoScan, which can be automated. Reductions in time and money spent lower the barriers for nonprofit and educational groups who desire to create immersive 3D content but are concerned about the costs involved. 

In terms of user experience, the workflow described in this chapter allows users to reconstruct existing landscapes at a resolution that is high enough to recognize individual ground features. The user navigates this landscape in the first person, and Unreal Engine 4 allows developers to set intuitive controls for the end users. Because this workflow only creates the template upon which a game can be built, geogame developers still must construct engaging narratives and gameplay if they hope to bring about user immersion. However, at the very least, this workflow allows end users to navigate and experience game environments in a way that may not have been possible from a top-down perspective. 

Several technical issues still limit the sizes and types of landscapes that can currently be represented using this workflow. Because of processing constraints, Unreal Engine 4 cannot efficiently process landscapes with a height map or material resolu- 

192 

N.J. Henry 

tion greater than 8192 × 8192 (Epic Games 2015c). This means that landscapes of a certain size cannot be digitized at a resolution high enough to accurately represent landscape features. Due to the downwards-facing orientation of orthophotos, steep vertical surfaces in the landscape are poorly textured and may be hard to clearly recognize. Additionally, as mentioned before, vegetation is not adequately represented by kite aerial photography alone (Olson et al. 2013: 259). Many of these problems could be greatly improved by representing landscape objects, including trees, rocks, and even cliffs, as discrete objects lying on top of a lower-resolution landscape. If these features were processed as Unreal static mesh objects, a data type that is more interoperable with 3D formats, then aerial photographs could be combined with shots from ground level to create game objects with a far higher resolution. By improving ground object recognition, geogames can move one step closer to accurate representation of the real world. 

Throughout the workflow, I found myself balancing trade-offs that pitted mesh quality against processing speed, landscape extent against visual resolution, and terrain variety against in-game comprehension. The game engine’s editing tools also presented me with a choice between manually enhancing the terrain and maintaining fidelity to the original remote sensing data. Navigating these trade-offs ultimately required me to make judgment calls based on the perceived preferences of an end-user. As geogames mature, developers will increasingly encounter these types of subjective challenges when making choices about visual representation, user experience, and gameplay; future research should embrace these challenges as a chance to develop the more artistic and experiential aspects of geogames. 

Because game engines are designed with customization in mind, this workflow also opens the door to a number of possible extensions. Games can be published for PC, iOS, Android, and the web, allowing users to browse and experience virtual environments through a variety of interfaces. Geogame levels are already being tested in conjunction with virtual reality; trial tests with the Oculus Rift headset have elicited extremely positive feedback from participants (Fig. 9.7). Game engines also facilitate the addition of sound and haptic (touch) feedback to a level, which could 

**Fig. 9.7** A student navigates the landscape using a virtual reality headset ( _left_ ); stereoscopic images sent to the headset create the sensation of three-dimensional navigation ( _right_ ) 

9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual… 

193 

expand the senses that players use to navigate the virtual environment. To further reduce the barriers for nonprofit and educational game creators, a similar workflow using only free software tools should be developed. Finally, the three- dimensional format opens up new possibilities for in-game storytelling and interactions; these narrative possibilities should be explored and linked to user immersion. 

## **References** 

Agisoft LLC (2016) Agisoft PhotoScan user manual: professional edition, Version 1.2. http:// www.agisoft.com/pdf/PhotoScan-pro_1_2_en.pdf. Accessed 1 Feb 2016 

Ahlqvist O (2011) Converging themes in cartography and computer games. Cartogr Geogr Inform Sci 38:278–285. https://doi.org/10.1559/15230406382278 

- Bayliss P (2007) Beings in the game-world: characters, avatars, and players. In: Proceedings of the 4th Australasian conference on interactive entertainment. RMIT University, pp 1–6 

- Boosman F, Szczerba RJ (2010) Simulated clinical environments and virtual system-of-systems engineering for health care. In: Interservice/industry training, simulation, and education conference. pp 1–9 

- Cain J, Piascik P (2015) Are serious games a good strategy for pharmacy education? Am J Pharm Educ 79:1–6 

- Chau M, Sung W, Lai S, Wang M, Wong A, Chan KWY, Li TMH (2013) Evaluating students’ perception of a three-dimensional virtual world learning environment. Knowl Manag E-Learn 5:323–333 

- CHDK User Manual (2016) Canon Hack development kit community. http://chdk.wikia.com/wiki/ CHDK_User_Manual. Accessed 1 Feb 2015 

- Currier K (2015) Mapping with strings attached: kite aerial photography of Durai Island, Anambas Islands, Indonesia. J Maps 11:589–597. https://doi.org/10.1080/17445647.2014.925839 

- Dawson P, Levy R, Lyons N (2011) “Breaking the fourth wall”: 3D virtual worlds as tools for knowledge repatriation in archaeology. J Soc Archaeol 11:387–402. https://doi. org/10.1177/1469605311417064 

- Denisova A, Cairns P (2015) First person vs. third person perspective in digital games: do player preferences affect immersion? In: Proceedings of the ACM Chicago 2015 conference on human factors in computing systems. ACM, New York, pp 145–148 

- Dickey MD (2005) Three-dimensional virtual worlds and distance learning: two case studies of Active Worlds as a medium for distance education. Br J Educ Technol 36:439–451. https://doi. org/10.1111/j.1467-8535.2005.00477.x 

- Epic Games, Inc (2015a) Creating and using custom heightmaps and layers. In: Unreal engine 4 documentation. https://docs.unrealengine.com/latest/INT/Engine/Landscape/Cu stom/index. html. Accessed 6 Aug 2015 

- Epic Games, Inc (2015b) Editing landscapes. In: Unreal engine 4 documentation. https://docs. unrealengine.com/latest/INT/Engine/Landscape/Ed iting/index.html. Accessed 6 Aug 2015 

- Epic Games, Inc (2015c) Texture support and settings. In: Unreal engine 4 documentation. https:// docs.unrealengine.com/latest/INT/Engine/Content/Types/Textures/SupportAndSettings/index. html. Accessed 6 Aug 2015 

- Fominykh M, Prasolova-Forland E, Morozov M, Gerasimov A (2011) Virtual campus in the context of an educational virtual city. Int J Interact Learn Res 22:299–328 

- Gatewing (2012) Software workflow: AgiSoft PhotoScan Pro 0.9.0. http://uas.trimble.com/sites/ default/files/downloads/gatewing_P hotoScanworkflow090.pdf. Accessed 6 Aug 2015 

- van der Hulst A, Muller T, Besselink S, Vink N (2013) The potential of serious games for training of urban operations. In: STO modeling and simulation group conference. Sydney, Australia, pp 1–8 

194 

N.J. Henry 

- Hussain TS, Roberts B, Menaker ES, Coleman SL, Pounds K, Bowers C, Cannon-Bowers JA, Murphy C, Koenig A, Wainess R, Lee J (2009) Designing and developing effective training games for the US Navy. In: Interservice/industry training, simulation, and education conference. pp 1–17 

- King G, Krzywinska T (2003) Gamescapes: exploration and virtual presence in game-worlds. In: Digital games research conference proceedings. p 109 

- Loke S (2015) How do virtual world experiences bring about learning? A critical review of theories. Australasian J Educ Technol 31:112–122 

- Magee L (2011) Virtual Reality (VR) as a disruptive technology. In: Defence Research & Development Canada Defence Research reports. http://cradpdf.drdc-rddc.gc.ca/PDFS/unc121/ p536948_A1b.pdf. Accessed 6 Aug 2015 

- Masters M (2015) Unity, source 2, unreal engine 4, or CryENGINE which game engine should i choose? Digital tutors. http://blog.digitaltutors.com/unity-udk-cryengine-game-enginechoose/. Accessed 6 Aug 2015 

- Olson BR, Placchetti RA, Quartermaine J, Killebrew AE (2013) The Tel Akko Total Archaeology Project (Akko, Israel): assessing the suitability of multi-scale 3D field recording in archaeology. J Field Archaeol 38:244–262. https://doi.org/10.1179/0093469013Z.00000000056 

- Pan Z, Chen W, Zhang M, Liu J, Wu G (2009) Virtual reality in the digital Olympic museum. IEEE Comput Graph Appl 29:91–95 

- Punzalan RL (2014) Understanding virtual reunification. Libr Q Inform Commun Policy 84:294–323 

- Ritzema T, Harris B (2008) The use of second life for distance education. J Comput Sci Coll 23:110–116 

- Roman PA, Brown D (2008) Games—just how serious are they? In: Interservice/industry training, simulation, and education conference. pp 1–11 

- Schindelin J (2012) Fiji: an open-source platform for biological-image analysis. Nat Methods 9:671–675. http://fiji.sc/. Accessed 6 Aug 2015 

- Sharma S, Otunba S (2012) Collaborative virtual environment to study aircraft evacuation for training and education. In: 2012 International conference on Collaboration Technologies and Systems (CTS). pp 569–574 

- Shepherd IDH, Bleasdale-Shepherd ID (2009) Videogames: the new GIS? In: Lin H, Batty M (eds) Virtual geographic environments. Esri, Beijing, pp 311–344 

- Šimic G (2012) Constructive simulation as a collaborative learning tool in education and training of crisis staff. Interdiscipl J Inform Knowl Manag 7:221–236 

- Smith MJ, Chandler J, Rose J (2009) High spatial resolution data acquisition for the geosciences: kite aerial photography. Earth Surf Process Land 34:155–161. https://doi.org/10.1002/esp.1702 

- Sylaiou S, Mania K, Karoulis A, White M (2010) Exploring the relationship between presence and enjoyment in a virtual museum. Int J Hum Comput Stud 68:243–253. https://doi.org/10.1016/j. ijhcs.2009.11.002 

- Taylor LN (2002) Video games: perspective, point-of-view, and immersion. Dissertation, University of Florida 

- Verhoeven G (2009) Providing an archaeological bird’s-eye view an overall picture of groundbased means to execute low-altitude aerial photography (LAAP) in archaeology. Archaeol Prospect 16:233–249. https://doi.org/10.1002/arp.354 

- Verhoeven G (2011) Taking computer vision aloft—archaeological three-dimensional reconstructions from aerial photographs with PhotoScan. Archaeol Prospect 18:67–73. https://doi. org/10.1002/arp.399 

- Ward, Jeff (2008) What is a game engine? Game career guide. http://www.gamecareerguide.com/ features/529/what_is_a_game_.php. Accessed 6 Aug 2015
