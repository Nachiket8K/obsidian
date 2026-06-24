---
title: "Chapter 10 Structural Gamification of a University GIS Course"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 10 Structural Gamification of a University GIS Course** 

## **Michael N. DeMers** 

## **10.1  Introduction** 

College level Geographic Information Systems (GIS) courses are, like most university courses, linear, rigid, punitive, and self-contained. Most have laboratories involving the use of high-end, complex GIS software with a steep learning curve. This chapter demonstrates one way to convert one such laboratory course into a quest-based learning (QBL) environment. The chapter illustrates how I am currently using **3DGamelab** ’s Quest-Based Learning Management System (LMS) to convert this traditional, college course into one that provides choice, rewards for learning from mistakes, and opportunities for credential building. I describe how to incorporate labs normally requiring face-to-face interaction, how to provide choice and still cover the material, how to leverage outside learning material, and how to encourage life-long learning. Many of the rewards, especially the badges, are linked explicitly to the US Department of Labor’s geospatial technology industry’s competency model, thus encouraging learners to see this as an opportunity to plan for future employment. Finally, this chapter discusses some of the difficulties of course mapping a complex, full-semester course. In particular it illustrates issues of adapting to learner needs, and the time and effort required to construct and deliver an interactive-intensive learning environment. I make recommendations for solutions and adaptations for such difficulties. 

Increasingly instructors of all university courses, including Geographic Information Systems courses are experiencing pressure to change to online formats of course delivery. Unfortunately the common perception still remains that by merely placing the content traditionally delivered face-to-face in a nicely ordered structure in the Learning Management System for the learner to retrieve is sufficient 

M.N. DeMers ( * ) New Mexico State University, Las Cruces, NM, USA e-mail: demers01@gmail.com 

**==> picture [14 x 7] intentionally omitted <==**

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_10 

196 

M.N. DeMers 

for such courses to be effective. Fortunately research regarding the design of online courses has matured greatly and has resulted in a set of standards for course design that is specifically intended to improve online course design. Called the QM, or Quality Matters Rubric,[1] it is a national peer review and certification process that allows course designers to receive feedback on the following eight general standards of course design: 

1. Course overview and introduction 

2. Learning objectives, 

3. Assessment and measurement 

4. Instructional materials, 

5. Course activities and learner interaction, 

6. Course technology, 

7. Learner support and accessibility 

8. Usability 

Alignment with such standards improves the likelihood of creating an environment in which effective online learning can occur. What it does not guarantee, however, is that the course design structure will, in and of itself, motivate the learner to engage in the material. Despite effective course QM Certification and the directemployment implications of practical courses like GIS, students do not always find the material particularly engaging. They do not always find the pace appropriate or sufficient learning choices available. Perhaps most importantly they seldom if ever experience a grading structure that rewards hard work and learning, but does not punish the learner for making mistakes as long as they can demonstrate that they have learned from them. Additionally, most GIS courses focus heavily on the hard technical skills of the geospatial industry while downplaying or ignoring the necessary soft skills, especially those revolving around communication (DeMers 2012). The search for a way to combine the rigor of a traditional lab-based GIS course with the allure, freedom, choice, and incentive-rich game environment suggests that the content of a traditional GIS could be ported to a quest-based environment that would provide these characteristics and lead to enhanced engagement in learning (Friedemann et al. 2015). 

## **10.2  Literature Review** 

QBL is part of a larger set of approaches to learning called game-based learning. It is important to note immediately that while games may be included in game-based courses there is a fundamental difference between the use of games as learning tools and the general process of gamification (Mallon 2013). Gamification refers to the adoption of some or all of the typical mechanics of games that carry with them the allure and addictive behavior (Banfield and Wilkerson 2014; Renaud and Wagoner 

> 1 The Quality Matters Higher Education Rubric can be found at https://www.qualitymatters.org/ rubric. 

10 Structural Gamification of a University GIS Course 

197 

2011; Rouse 2013). The mechanics of concern are points (experience points), badges, levels, leaderboards, challenges and other incentives and reward structures that motivate gamers. 

While all of the mechanics are present to a greater or lesser degree how these mechanics are implemented is highly dependent on the form of gamification in play. There are two forms of gamification—content gamification in which the course content is converted to games and structural gamification in which the content remains intact and the mechanics are modified to leverage the same incentives found in games. In content gamification exercises are converted from their tradition formats—e.g. reading assignments, writing assignments, lectures, discussions, labs, etc.—to actual games in which the object is to win the game, and as a byproduct, learn what the instructor wants. The games can be action/adventure games in which the concepts and skills being taught are necessary components of the game. They can be simulations of real world disciplinary settings in which the learner is involved in role-play. Strategy games also find themselves being used in the educational environment in which the strategy itself is composed of the content being taught. Whatever type of game is being employed, the focus of content-gamification is to set up a scenario in which the learner is not always aware of the intended learning objectives, but is rather being tricked into learning the material (DeMers 2005, 2010). 

Structural gamification does not convert the content into games but rather focuses on the game mechanics that are considered some of the more common reasons that games are so inherently addictive. While generally, but not exclusively, not focusing on making the learning itself “fun,” instead it focuses on the manner in which the course is organized. Such structural gamification means that all assignments, while traditional in their methods of delivery, are considered to be quests to be conquered. While they often have prerequisite skills and knowledge, acquired through successful completion of other quests, there is far more flexibility as to when they can be taken. In effect the course, if based on a text, does not require that the learner necessarily move linearly through the material. Within the loose structure the learners have choices regarding taking high value, long assignments versus lower value but much shorter timeframes. Such an approach allows a college level instructor the ability to provide at least some of the important characteristics of the personal learning environment (PLE), particularly the self-regulation (Dabbagh and Kitsantas 2012) that is increasingly being demanded of today’s millennial learner (Dede 2007). 

Virtually all the remaining mechanics are related to grading. Unlike normal assignments, quests are all-or-nothing in that if the learner achieves a certain level of accomplishment (normally considered 85%) the quest is considered successful. This is identical to the testing procedures of the Esri online tutorial modules (Johnson and Boyd 2007). One crucial pedagogical improvement of this approach to grading is that each time a quest is returned, the learner receives feedback from the instructor regardless of the success or failure of the quest. This greatly enhances the amount of student-faculty interaction—a feature considered highly correlated to student success (Lamport 1993; Kuh and Hu 2001). 

Collectively, there is also a fundamental difference in how course grades are accumulated. In a typical course one has a limited number of points and as the 

198 

M.N. DeMers 

**Fig. 10.1** The difference between the subtractive grading process of traditional courses versus the additive grading process of Quest-Based courses 

course progresses the learner continues to lose points—moving from a beginning score of 100% toward an ever decreasing score. In quest-based learning the process is reversed in that there are generally more points (called experience points in game parlance) than one needs to achieve a grade of A in the course. In short, QBL style grading is additive while traditional grading is subtractive (Fig. 10.1). Other graderelated components include a reward structure that encourages not just completing quests, but doing exceptional work, working hard to complete difficult tasks, etc. Each of these “rewards” is built into the system as incentives for desired behaviors. Some of these rewards are “achievements” based on completing a substantial portion of the course material. Other rewards are badges that document micro credentials for particular skills, behaviors, characteristics, or knowledge that is considered useful based on industry needs related to the course material. Badging has been shown to be useful as incentives for self-efficacy, enjoyment, and motivation in education (Ahn et al. 2014; Chen et al. 2012; Denny 2013; Finkelstein et al. 2013; Gibson et al. 2013). One added advantage of badging is that organizational websites such as Mozilla Backpack provide a means to store, retrieve, and most importantly to share these badges beyond the classroom setting for documenting selected microcredentials with peers, colleagues, current employers, or future employers. 

Competition is also encouraged by allowing students to compete with each other for the accumulation of quest experience points, levels, and awards. In video games, one’s scores are compared to those who are also engaged in the same game but not necessarily as adversaries. Such comparisons, called “leaderboards” provide a direct comparison of ones success in the game to others. In some games and in most 

10 Structural Gamification of a University GIS Course 

199 

educational settings the leader board is an opt-out item for those who do not wish to have their names included. At the same time, such anonymous members are still able to view others’ names on the leaderboard to gauge their level of success. 

Given the nature of millennial learners (Dede 2005) so commonly found in university undergraduate courses and their constant exposure to social media and computer games it seems reasonable to assume that such technology would be rapidly embraced by educators in general and college educators in particular but this does not seem to be the case (Dicheva et al. 2015). While business, marketing, corporate management and even wellness industries have adapted to gamification methods, educational adoption seems to be more of an emerging trend. Johnson et al. (2014), however, are hopeful that these technologies will soon be on the “adoption horizon” as they call it within 2–3 years. 

The missing piece to this adoption puzzle is a game-based platform; a learning management that incorporates the mechanics of structural gamification. There are few mature systems capable of being able to allow gamification mechanics, and even fewer that are specifically designed around such an approach. One of the most accessible mature systems designed around the quest mechanics of quest based learning is **3DGamelab** , a product of a company called Rezzly. The **3DGamelab** is a product of years of research in game-based learning dating back to efforts to use virtual worlds as a platform for game-based learning (Dawley 2011; Dawley and Dede 2012). With time the efforts of the researchers at Boise State University developed the principles, constructs, and mechanics of an operational quest-based learning management system (Haskell 2012, 2013). Because this platform is so new, there is little if any formal documentation regarding the success or failure of implementing courses using this approach, although there is one blog that discusses the approach briefly (Kolb 2015). This chapter is a first step in filling that intellectual void with particular reference to Geographic Information Systems education. 

## **10.3  Mechanics** 

As discussed earlier there are a few learning management systems capable of supporting the structural gamification needed to implement a truly quest-based course. Among the most mature, most robust, and most fully developed is the **3DGamelab** produced by Go Go Labs (now called Rezzly.com). Beyond its level of development, I selected this platform because it is based both on experience and educational research (Dawley 2011) and because its price per student was reasonable for this experiment. 

The **3DGamelab** is a quest-based LMS that is not just compatible with structural gamification but is based entirely on it. It provides a badging system, rewards, leveling up, leaderboards, and the mechanics to allow these features to be operationalized in a course setting. These allow the course developer to concentrate on the content rather than on these mechanics. The **3DGamelab** is integrated into existing LMS software, in this case Canvas, so the learner doesn’t have to move between elements of Canvas and **3DGamelab** . 

200 

M.N. DeMers 

## _**10.3.1  Design Considerations**_ 

Because quest-based learning provides a high level of choice both in what learning opportunities the students pursue and in the sequencing, the orchestration of the many moving parts of a complete laboratory course becomes a bit of a challenge. Fortunately, the **3DGamelab** user interface provides a roadmap for designing your QBL course. To map out the quests, **3DGamelab** the roadmap—an Xcel- based template that calculate experience points, tabulates sequencing and prerequisites, estimates time requirements, and provides other feedback for course development. It also calculates total quest points, available reward points, total possible points, winning condition (number of points for a grade of A), total number of quests, and the estimated time to complete all the quests (in minutes) (Fig. 10.2). 

As with any course there is a need to determine how much weight to assign to both types of learning activity (e.g. lecture material versus laboratory or project) as well as to each activity. I was guided as much by experience as anything but the general approach was based on the idea that one should be able to approach, but not obtain a grade of A from doing the basic lectures, labs, portfolios, quizzes, and exams. The remaining of the points require the learner to select up to 400 points from a total of 3700 points in quests that remained available. This provides plenty of material for additional learning even when the semester is concluded. As the course is often the specific numbers will be adjusted based not on the amount of time that I estimated each quest to consume, but rather by tabulating averages for each quest as the system compiles them. 

As the instructor creates each quest it is included in the table and properties related to whether the quest requires grading by the instructor or is graded automatically, the estimated time for each quest to be completed, number of experi- 

**Fig. 10.2** A portion of an Xcel-based QBL roadmap with individual quest information in the table rows and the summary data at the _top_ 

10 Structural Gamification of a University GIS Course 

201 

ence points, and the prerequisites are included and both the time and experience points are updated in the summary portion of the table. To further assist with course navigation I employed a branching diagram, not unlike a mind map, to keep track of course prerequisites and learning pathways. Some QBL instructors use a software package for tablets called Popplet[®] . I use a similar package called Scapple[®] that works on PC’s or Macs. The choice of software is a matter of familiarity, hardware, and personal preference. One reason I use the Scapple[®] software is that it allows me to use the icons I use in the course to identify the quests rather than relying on text that, for a course of this magnitude, would create a diagram that would be far too difficult to read. 

## _**10.3.2  Quests**_ 

The system allows the user to create individual quests that can carry up to 200 experience points depending on the anticipated length of time or amount of effort required to complete the assignment. For this course I created the following quests: 

- 4 introductory quests designed to teach the use of the system 

- 74 lecture quests (17 book chapters broken into smaller topical sections) 

- 27 laboratory quests (based on a commercial laboratory book) 

- 11 laboratory portfolio quests (based on the laboratory book tutorials) 

- 1 portfolio compilation quest (collecting the artifacts into a course eportfolio). 

- 20 Esri tutorial quests 

- 17 recall quests (chapter quizzes) 

- 3 unit recall quests (mid-term exams) 

- 3 group project quests (parts 1, 2, and 3) 

- 2 personal project quests (parts 1 and 2) 

- 2 quest hacker quests (make your own quest) 

- 2 literature review quests (parts 1 and 2) 

- 2 laboratory practicum quests 

- 2 course feedback quests (to provide me with ways to improve the course) 

One important aspect of the system is that it allows for not only creating the quests (assignments) but also a mechanism for learners to submit their work for evaluation within the quest-based grading model (Fig. 10.3). Because this is a quest- based course the assignments are not graded as you would a class exercise. Instead they use the 85% rule in which the instructor determines a whether or not the assignment has achieved 85% of the learning objectives of the quest. If they have, the learner’s quest is approved, usually with additional helpful comments. Alternatively, if the instructor feels that the assignment does not meet the 85% rule the assignment is returned with comments, helpful suggestions, and even additional sources of information to assist learning. This process continues until the learner completes the quest. Completed quest receive 100% of the experience points for 

202 

M.N. DeMers 

**Fig. 10.3** 3DGamelab Quest approval user interface with the ability to provide feedback and attachments if needed 

each. This is as true of quizzes (recall quests) as of any other quest, in that the learner is allowed to take quizzes as many times as they need to pass. 

The course content comprises traditional content variously emphasizing a large proportion of the GIS&T Body of Knowledge (DeMers 2009). The rewards for this course are grouped into three general categories— _awards_ , generally related to lecture and laboratory completion as well as special accomplishments such as excellence, speed, hard work, acquisition of GIScience level of understanding and others; _achievements_ (levels); and _badges_ (Fig. 10.4 , DiBiase, et al. 2010). The badges are particularly of interest to this course because each badge is directly linked to one of the 25 competencies of the US Department of Labor Geospatial Skills Competency model. These badges that can be archived in the Mozilla badging backpack, together with the e-portfolio quests and the Esri online course certificates add incentives for the students by providing them with a vast array or credentials the students can bring to potential employers. It was hoped that the implementation such a questbased GIS approach to learning would encourage greater participation, more interaction, more self-efficacy among the students, and ultimately more enjoyment. 

10 Structural Gamification of a University GIS Course 

203 

**Fig. 10.4** Twenty-five badges linked to the 25 skills in the US Department of Labor Geospatial Skills Competency Model 

## **10.4  Results** 

Developing a course of this scope, with nearly 180 interconnected quests is a complex process requiring a substantial commitment of time. Converting the narrated lectures into interactive multi-media content was by far the most time-consuming task. The laboratories however were surprisingly straightforward as the Esri laboratory manual used had the exercises fully laid out and included learning objectives and requisite products. Prior to each set of laboratory quests was a related tutorial that, in past courses, the students often skipped, making them struggle with the labs and costing the teaching assistants an inordinate amount of additional tutoring. The portfolio exercises were designed to correct this issue by requiring the student to turn in the products of the tutorials. The results were generally successful although many students did not immediately embrace the idea, and, only after learning how to navigate the system did they appreciate the tutorial. 

Because the course material is less structured than a traditional course, as expected by experiences with this same online courses prior to gamification, a 

204 

M.N. DeMers 

bimodal distribution of student engagement emerged early in the course. For week 3, n = 24 participants, the range of quest scores was 15 for a low and 1115 for a high. The mean for experience points was 332 and the median was 210. These numbers are paralleled by a high of 28 quests and a low of 2 quests. The students self-report the actual time they spend questing. One student has not reported these numbers so with n − 23 the average quest time is reported as ranging from 88 to 2 min with a mean of 31.5 min and a median of 30 min. There are nine students with less than 100 quest points and these same students started questing late; often waiting nearly 2 weeks before beginning a single course experience. Those heavily engaged in the content and those less than enthusiastically engaged. 

By week 10, 6 of the 23 students had dropped the class—notably within ±5% of the rate of the previous five offerings of the course online but without quest-based learning mechanics. Two students had achieved GISAnalyst (modeler) rank, requiring 3400 experience points (Table 10.1). Notably there seemed to be no pattern of Badge achievement, but achievements exemplified by completing higher level quests or performing exceptionally on assignments were higher among the higher ranked learners. The latter trend is to be expected as higher achieving students will also be those who not only do assignment, but do them very well and achieve more quests resulting in additional achievement-based points. 

When the course concluded 12 of the students had achieved the rank of Chief Executive Officers (over 4500 experience points), a rank associated with a grade of A in the course. Four of the students achieved a rank of GIS Master (between 4000 and 4500 experience points), a rank associated with a grade of B. Finally, one student did not complete the course, receiving a grade of incomplete. This latter  student requested an extension of the course due to illness and is, at the time of this writing, completing the work not completed during the semester. There were no C, D, or F grades in the course, consistent with the findings of Haskell (2013), but since the conclusion of the course none of the students have continued to quest nor to pursue badging microcredentials. This is at odds with Haskell’s results and suggests differences resulting from student level, quest engagement, circumstance, or course design. These results have yet to be investigated and remain important questions in the deployment of QBL courses. 

Each quest allows students to rate it and to provide some feedback regarding any aspect of it they wish. Generally the preliminary students rated the quests with average scores of approximately 4.2 out of 5 and few provided verbal input. Those few who did seemed concerned about the amount of time required to perform each quest. In the case of the laboratory quests this seems a reasonable reaction but the students seems particularly concerned that the lecture exercises required too much time for the points achieved. In informal conversations with students regarding this, their concern was not just the amount of time required, but that they feared they would not be able to achieve the necessary 5500 experience points to achieve an A, or 4000 to achieve a grade of D. One objective of the course was to require the students to spend more time on the content as there is a direct positive correlation between time on task and learning. However, based on student feedback I reduced the point scores for each level and for final grades by 1000. This value seemed more reasonable and the learners began participating with more vigor, indicating that the high levels needed for grades acted as a disincentive for participation. 

10 Structural Gamification of a University GIS Course 

205 

|Awards|12|10|13|8|10|10|7|9|4|5|5|2|3|5|4|4|6|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Achievements|8|9|7|6|6|5|4|4|2|5|2|2|2|2|2|2|2|
|Badges|0|5|1|6|1|2|1|0|0|11|0|1|0|2|1|2|1|
|RewardXP|370|390|560|360|300|290|200|310|90|370|100|70|70|150|130|130|120|
|Dropped|0|1|1|2|1|7|6|1|1|1|5|0|5|1|0|1|2|
|Completed|83|81|63|69|70|68|54|50|38|29|38|39|38|31|34|32|30|
|Active|1|5|3|7|16|6|3|2|1|6|3|5|19|7|9|6|5|
|QuestXP|3145|3035|2515|2475|2455|2315|1945|1815|1395|1035|1255|1255|1245|1095|1095|1075|1055|
|TotalXP|3495|3405|3055|2835|2755|2605|2145|2095|1485|1405|1355|1325|1315|1245|1205|1205|1175|
|Rank/grade|GISAnalystII(modeler)|GISAnalystII(modeler)|GISDatabaseManager|GISAnalyst1|GISAnalyst1|GISJourneyman|GISMasterTechnician|GISTechnician|MapReader|MapReader|MapReader|MapReader|MapReader|MapReader|MapReader|MapReader|MapReader|
|GamerTag|mastergeomex|4gingkos|desert bat|evitolas|rebecca_armenta|mrmusta|nirome|kevinvirden|marcusal|dil2.0|jacobvallee|tlowe|carmertsandiego|dsrtrosy|imjustaguy|mvela|snoopylupe|



206 

M.N. DeMers 

As the students progressed they eventually became more efficient at the lecture assignments that were primarily designed to get them to answer the questions at the end of the chapter in their own words. Initially I found that as they began taking the recall quests the number of students who passed them with a score of 9/10 (the closest a ten question quiz can be to the magical 85%) on the first try seemed considerably higher than students who took the traditional course. This indicates at least anecdotally that there is more learning happening in the quest course than the traditional course. As the weeks have gone on I have also noticed that the student responses to the lecture quest questions are becoming more robust, more detailed, and generally more insightful. I also noticed that I was able to award far more “awards of excellence” as a result of this. 

A major issue of the course appeared early on and is continuing. Some learners purposely procrastinate; using the loose structure of the course to focus on other coursework. While this was part of the design it indicates that some constraints on quest completion needs to be applied. The teaching assistants are particularly adamant about imposing some restrictions on when material must be turned in, as they are responsible for grading the laboratory exercises. The procrastination required them to be familiar with all of the 27 laboratories—an unnecessary burden on the teaching assistants. An anticipated side effect of the deliberate procrastination is that those who are regularly handing in exercises will likely be forced to wait for grading feedback as large groups of exercises from the latecomers pile up. 

At the beginning of the course the general consensus of the students was that they liked the idea of flexible scheduling. Unfortunately as the course began they also showed a lack of motivation to pursue the material aggressively to complete the course early, opting instead to wait. One positive feedback from informal discussions with the students was that they were surprised at the amount of feedback they received. This indicates that this part of the course implementation was at least recognized if not effective at enhancing the students’ learning. 

## **10.5  Summary and Conclusions** 

This course demonstrated few basic results that are notable, some positive, some negative. It appears that there is enhanced learning as evidenced both by the steadily increasing quality of assignments turned in by the students and the improved efficiency in the recall quests. As the semester progressed the answers to questions related to course content were increasingly more robust, more complete, and in the case of the better students, more insightful. This indicates a deeper level of comprehension of the material than what I have seen in previous, non-QBL incarnations of the course. The interactions between faculty and student were times greater than in both the face-to-face versions of the course as well as the previous online versions which content required less personal attention of the instructor to grade. 

Procrastination was a major problem especially for the laboratory assistants who are responsible for grading the labs. While the feedback was constant, the amount of grading was substantially higher than one would expect of a normal college 

10 Structural Gamification of a University GIS Course 

207 

course. This has both negative and positive consequences. Obviously grading nearly 2000 quests requires a dedication to grading on the part of the instructor, however the constant feedback provides an astonishing amount of faculty to student interactions—interactions often touted by face-to-face instructors as the reason for not wanting to move to online instruction. Overall the amount of time spent providing feedback seems to have paid off in much enhanced learner comprehension and this is after all the primary reason for education. 

Leveling seemed to be a motivating factor as students commented individually that they appreciated knowing what point scores they needed to achieve to obtain a specific grade. For some students the achievement of badges had meaning but these tended to focus more on the acquisition of Esri certificates of completion than on the other badges. Unfortunately, the allure of the Esri certificates resulted in many students spending an inordinate amount of time on these quests which, by design, provided far fewer points per time investment. The purpose of assigning such low scores was to discourage such an approach, as the acquisition of ArcGIS expertise is given a much lower value in the course over conceptual learning. As this activity was observed, intervention in the form of sending the learners a reminder of the need to concentrate on high value learning experiences over low value if they hoped to achieve desired grades. While the course roadmap had been provided to the learners at the beginning of the course, it was necessary to reintroduce the roadmap as well as to provide specific examples of how to achieve major rewards for less effort. This was especially important as I pointed out that the course contained Easter eggs (hidden rewards in this case) that provided huge rewards (e.g. 100 points) for achieving select benchmarks—e.g. completing an exam representing 1/3 of the lecture content. 

Overall the course seems to have a qualified success with some obvious issues needing to be addressed. Beyond the procrastination issue, some learners find the nature of the exercises, especially the lecture exercises requiring them to provide responses in their own words, to be tedious to the point of being painful. This might suggest the use of audio responses to minimize the amount of typing on the part of the learner. This approach has its own negative consequences as it increases the amount of time it takes for grading. As the course continues more feedback will be available. The students will also be asked to participate in a filmed, unstructured exit interview to provide additional insights. 

## **References** 

> Ahn J, Pellicone A, Butler BS (2014) Open badges for education: what are the implications at the intersection of open systems and badging? Res Learn Technol 22:23563. https://doi. org/10.3402/rlt.v22.23563 

> Finkelstein J, Knight E, Manning S (2013) The potential and value of using digital badges for adult learners: DRAFT for public comment. American Institute for Research, Washington, DC Banfield J, Wilkerson B (2014) Increasing student intrinsic motivation and self-efficacy through gamification pedagogy. Contemp Issues Educ Res 7(4):291–298 

> Chen Z-H, Liao CCY, Cheng HNH, Yeh CYC, Chan T-W (2012) Influence of game quests on pupils’ enjoyment and goal-pursuing in math learning. Educ Technol Soc 15(2):317–327 

208 

M.N. DeMers 

- Dabbagh N, Kitsantas A (2012) Personal learning environments, social media, and self-regulated learning: a natural formula for connecting formal and informal learning. Internet High Educ 15(1):3–8 

- Dawley L (2011) Questing across the spectrum of virtuality: aggregating learning in 3D GameLab. Int J Gaming Comput-Mediat Simul 3(4):iii–iiv 

- Dawley L, Dede C (2012) Situated learning in virtual worlds and immersive simulations. In: Spector JM, Merrill DM, Elen J, Bishop MJ (eds) Handbook of research on education communications and technology, 4th edn. Springer, New York 

- Dede C (2005) Planning for neomillennial learning styles. Educ Q 28(1):7–12. https://net.educause.edu/apps/eq/eqm05/eqm0511.asp?print=yes. Last accessed 30 March 2014 

- Dede, C. (2007). Reinventing the Role of Information and Communications Technologies in Education. In L. Smolin, K. Lawless, & N. Burbules (Eds.), Information and Communication Technologies: Considerations of Current Practice for Teachers and Teacher Educators [NSSE Yearbook 2007 (106:2), pp. 11–38. Malden, MA: Blackwell Publishing. 

- DeMers MN (2012) Preliminary analysis of GIS workforce education: linking practitioners with educators. Papers Appl Geogr Conf 35:41–49 

- DeMers MN (2010) Coyote teaching in geographic education. J Geogr 109(2):1–8 

- DeMers MN (2009) Using intended learning objectives to assess curriculum materials: the UCGIS body of knowledge. J Geogr High Educ 33(Supp 1):S70–S77 

- DeMers MN (2005) Coyote medicine: tricking your GIS students into learning. Proceedings ESRI education user conference, San Diego. http://proceedings.esri.com/library/userconf/educ05/ papers/pap1934.pdf 

- Denny P (2013) The effect of virtual achievements on student engagement. Proceedings, SIGHI conference on human factors in computing systems, CHI13. pp 763–772 

- DiBiase D, Corbin T, Fox T, Francis J, Green K, Jackson J, Jefress G, Jones B, Brent J, Mennis J, Schuckman K, Smith C, Van Sickle J (2010) The new geospatial technology competency model: bringing workforce needs into focus. Urisa J 22(2):55–72 

- Dicheva D, Dichev C, Agre G, Angelova G (2015) Gamification in education: a systematic mapping study. Educ Technol Soc 18(3):75–88 

- Friedemann S, Baumbach L, Jantke KP (2015) Textbook gamification transforming exercises into playful quests by using webble technology. Proceedings, 7th international conference on computer supported education. http://www.researchgate.net/publication/278672297 

- Gibson D, Ostashewski N, Flintoff K, Grant S, Knight E (2013) Digital badges in education, 2015. Educ Inf Technol 20:403–410 

- Haskell CH (2012) Design variables of attraction in quest-based learning. PhD dissertation, Boise State University. http://scholarworks.boisestate.edu/cgi/viewcontent.cgi?article=1286&context=td 

- Haskell CH (2013) Understanding quest-based learning. [Whitepaper]. https://works.bepress.com/ chris_haskell/21/. Retrieved 27 May 2016 

- Johnson AB, Boyd JM (2007) Content, community, and collaboration at ESRI virtual campus: a GIS Company’ perspective on creating an online learning resource. J Geogr Higher Educ 29(1):115–121 

- Johnson L, Adams Becker S, Estrada V, Freeman A (2014) Games and gamification. In NMC horizon report: 2014 higher education edition. The NewMedia Consortium, Austin, TX, pp 41–43 

- Kolb L (2015) Epic fail or Win? Gamifying learning in my classroom, Eductopia blog. http:// wwwedutopiaorg/blog/epic-fail-win-gamifying-learning-liz-kolb. Last accessed 7 Sept 2015 

- Kuh G, Hu S (2001) The effect of student-faculty interaction in the 1990s. Rev High Educ 24(3):309–332 

- Lamport M (1993) Student-faculty informal interaction and the effect on college student outcomes: a review of the literature. Adolescence 28(122):971–990 

- Mallon M (2013) Gaming and gamification. Public Serv Q 9(3):210–221 

- Renaud C, Wagoner B (2011) The gamification of learning. Princ Leadersh 12(1):56–59 

- Rouse KE (2013) Gamification in science education: the relationship of educational games to motivation and achievement. PhD dissertation, University of Southern Mississippi
