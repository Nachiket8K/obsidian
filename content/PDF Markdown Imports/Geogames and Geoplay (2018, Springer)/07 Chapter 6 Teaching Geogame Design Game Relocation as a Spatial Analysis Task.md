---
title: "Chapter 6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task** 

## **Christoph Schlieder, Dominik Kremer, and Thomas Heinz** 

## **6.1  Introduction** 

Before we can play games, we have to design them. While both activities are complementary, educational uses of games have focused on the playing aspect. There are, however, a number of reasons for including game design into a curriculum on spatial thinking. 

First, location-based games are known to be quite effective at supporting a broad variety of learning processes (Klopfer 2008; Schaal et al. 2012). In education practice, however, we see little variation in the underlying game mechanics. A study of mobile location-based learning projects in Germany, for instance, revealed that all projects, which used gamification approaches, were adopting some variant of **Geocaching** (Lude et al. 2013). 

A second reason is that location-based games have started to become part of the media and entertainment environment of teenagers. Students in grade 10 or higher very likely have had contact with non-educational versions of these games either as players or as viewers of Let’s Play videos. **Ingress** , operated by Niantic, is one of the early popular examples of a location-based game (Hodson 2012). Researchers have also begun to look at **Pokémon Go** , an enormously successful game released by the same company in 2016 (Althoff et al. 2016). Furthermore, commercial gamification approaches increasingly use geographic location, for instance, in the form of location-based games that are marketing a touristic destination (Celtek 2010). 

C. Schlieder ( * ) Faculty of Information Systems and Applied Computer Sciences, University of Bamberg, Kapuzinerstraße 16, 96047 Bamberg, Germany e-mail: christoph.schlieder@uni-bamberg.de 

D. Kremer • T. Heinz University of Bamberg, Bamberg, Germany 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_6 

111 

C. Schlieder et al. 

112 

Finally, the design process of a location-based game involves a considerable amount of spatial analysis. When game designers identify suitable places for game play, they compare, for instance, the distances between the places based on assumptions about pedestrian locomotion. Such GIS supported analysis tasks fit very well into a curriculum on spatial thinking—see Sinton and Lund (2007) for examples of teaching spatial thinking in a multi-disciplinary context. 

However, the design of a location-based game requires a basic understanding of spatial game mechanics, software engineering skills, considerable knowledge of the geography of the place, which the players are going to explore, and, last, but not least, a sufficient amount of time for creating, testing, and improving the design. From a teaching perspective, these requirements seem prohibitive, even in secondary education. This chapter approaches the challenge of creating geogames as a classroom activity from the perspectives of location-based game design, spatial analysis and geo-information processing. We describe an approach, which avoids much of the complexity of the design process by applying _three heuristics_ : (1) We start with a rule set known to produce a well-balanced game and do not ask the students to invent the rules of the games. (2) We proceed with visiting the geographic environment, which acts as the game field and do not let the students design the game based on web cartography only. (3) We challenge the students to optimize the game flow by applying spatial analysis and do not encourage chance results. 

We will support the heuristic principles outlined above in this chapter and present the methodological and technical tools to implement them. Section 6.2 reviews related work and presents a subclass of location-based games, which has been studied extensively in the research literature. Referring to a model of the game design process, we show in Sect. 6.3 how to reduce the complexity of the design task by focusing on game relocation, that is, the task of adapting a successful locationbased game to a new environment. Relocating a geogame involves redesigning the places of gameplay. Section 6.4 illustrates how place design operates using the geogame **CityPoker** as an example. We adapt the place design process to our learning scenario by decomposing it into two phases and devote a separate section to each of them. Section 6.5 describes the place storming method, which helps students to identify places in the geographic environment that are suitable for game actions. In Sect. 6.6, we present a software tool that supports the spatial analysis tasks involved in the design of a location-based game. This tool assists students to relocate a geogame in a classroom project. Finally, we conclude in Sect. 6.7 with a discussion of the results we have obtained as well as of future research directions. 

## **6.2  Related Work and Basic Terminology** 

In this chapter, the term _geogame_ refers to competitive location-based games in which at least two players or two teams of players move in an urban or natural environment using mobile devices to communicate, to access spatial data, and to solve place-related tasks (Schlieder et al. 2006). As a characteristic design feature, such geogames allow players to perform game actions only at certain geographic 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

113 

locations. We call them _places of game play_ (POG). In a competitive two-player variant of **Geocaching** , for instance, the geocaches act as the POG. They are the only places where the player can perform the game action of finding a hidden object by physically accessing the cache. All geogames create some sort of virtual game board, which adds a layer of semantics to the geographic environment. 

There are different ways to exploit the additional layer of spatial semantics. A live action role playing game creates POGs such as a magic forest, which may have little resemblance with features of the geographic environment (Montola et al. 2009). Other genres of geogames adopt a similar approach. **Ingress** , for instance, advertises itself with the promise: “The world around you is not what it seems”. In serious games, however, designers often do not aim at creating an alternate reality distinct from geographic reality (De Gloria et al. 2012). Instead, they try to link the players by spatial actions to existing places in the environment (von Borries et al. 2007; de Souza 2009; Schaal et al. 2012). Depending on the geogame’s objective— a learning outcome, a tourist experience—the designer chooses different _places of interest_ (POI) to act as the POGs of the game. The choice of places has to be made for any geographic region where the game is played. We discuss the challenges of this game relocation task in Sect. 6.3. 

In practical terms, game relocation often involves outdoor exploration. Firsthand experience helps to determine which places support which game activities. Kristiansen et al. (2014) describe site storming, an outdoor exploration method for discovering POG and associated game tasks. Our simplified method, which we call place storming, provides more guidance to the students than site storming and it supports finding typical combinations of places and activities rather than exceptional ones. In our approach to game design in the classroom, the students engage first in a phase where they use place storming to generate a set of POI. This set consists of places the students identified as interesting because the players could engage in actions that contribute to the learning outcomes (Fig. 6.1). 

Place storming generates more places than are actually needed for the game. The surplus is important since not every subset of POI qualifies as POG. Additional constraints have to be considered during the design phase of the geogame. Important constraints arise from the balancing of the game mechanics, that is, from the way in which the rules of the geogame interact with the places. Balancing aims at rules that make the game neither too easy nor too hard to play. Another objective of balancing is fairness. The choice of POG should not give an advantage to one of the teams. Game design research has described a number of balancing methods outside the realm of location-based games (Adams and Dormans 2012). For the case of location- based games, Schlieder et al. (2006) have shown that the game designer has to provide some mechanism to compensate for the differences in locomotion speed, which always exist between players. Otherwise, a trivial winning strategy dominates: the fastest player nearly always wins. Because of the importance of locomotion, the time that players need to move between the POG becomes the most important parameter to analyze in the context of balancing. The spatial analysis of the locomotion paths between the POI is the second design activity the students engage in our approach (Fig. 6.1). It constitutes a filtering process, which selects a subset of suitable POG from the much larger set of POI. 

C. Schlieder et al. 

114 

**Fig. 6.1** Place storming and spatial analysis. Source: created by C. Schlieder 

## **6.3  The Game Relocation Process** 

We adopt an extended version of the model of the geogame design process introduced by Schlieder and Kremer (2014) to describe the context of game relocation. The model identifies six groups of design tasks and explains how the tasks interact at the three levels of ludic design, narrative design, and performative design (Fig. 6.2). It reflects the results of an analysis of a set of game design documents created by the geogames team at the University of Bamberg. 

The geogame design process begins with specifying the learning outcomes and learning strategies that the game should support. Most importantly, the game has to blend into the other activities in the curriculum. This requires the involvement of the educator and some communication with the development team. In our own game design projects, we sought early contact with the educators and asked them to view the geogame as a computer-mediated field trip rather than as an extra-curricular activity. 

The two groups of design tasks, those relating to the game objectives and those relating to the staging of the game, both refer to the situational context. They share the fact that educators participate as co-designers, which is why the design process model groups these tasks at the level of performative design. A sequential, noniterative design process such as the one indicated by the arrows in Fig. 6.2 starts and ends with addressing issues of performative design. In practice, however, most design teams iterate several times over the different groups of tasks. A walkthrough of a simplified version of the process nevertheless provides a useful conceptual framework for identifying how to streamline the design process for use in the classroom. 

115 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

**Fig. 6.2** The geogame design process 

The tasks of defining geogame objectives and staging the geogame at the _performative level_ will be familiar to educators because similar issues are handled in connection with field trips, such as identifying goals and managing contingency plans, e.g. organizing student transportation or reacting to changing weather conditions. Just like during field trips, in our example students do not contribute to defining the learning outcomes nor game staging. Because educators are involved at this performative level, it constitutes a good starting point for simplifying student participation in the design process. 

At the _level of narrative design_ , we find two different groups of tasks. The task of designing the game narrative includes creating the game story line as well as the supporting media assets. In a typical educational geogame, the creative design team develops these elements in close interaction with a focus group of educators. Once the design phase finishes, the story line and the media assets stop to evolve and become an integral part of the geogame. 

For the second group of narrative design tasks, however, the core design team will generally not be able to come up with a ready-to-play solution. These are the tasks concerned with _place design_ , that is, with choosing the game’s geographic content. Geogames tell spatial stories by selecting specific POGs and then associating place-related tasks to the POGs. Choosing places and tasks that have a good fit is critical for the gameplay component. For example, asking students to photograph a pine tree constitutes a trivial task in some geographic environments, but might be completely impossible in others. It follows that place design requires local geographic knowledge. As a design task, place design is accessible to students because they can use their everyday experiences with their spatial environment as a starting point. In our scenario, the students assumed the role of place designer by identifying the places of gameplay and creating the associated spatial tasks. 

The _level of ludic design_ , finally, groups the tasks that relate to the game mechanics and their implementation in mobile technology. _Game mechanics_ is the term 

116 

C. Schlieder et al. 

designers use to refer to all elements, which define the playing experience. Game mechanics include the rules defining the game, the modes of interaction with the player, and the game’s incentive mechanisms. While we may expect most 12–16 year old students to have some experience with a variety of different game mechanics, this does not automatically make them good designers. Even students in a university- level game design program struggle with creating well-balanced game mechanics. For that reason, we did not ask the students to design the game mechanics, but let them build their game by re-using a proven mechanic. This approach has the additional advantage that neither the students nor the educators have to be involved with programming the software implementing the game mechanics. 

Geogames are intrinsically related to places. This is why designers create, implement, and test them in a specific geographic environment. Once the geogames works there, the designers start to relocate it to other environments. In terms of the design process model, _geogame relocation_ amounts to repetition of the place design process several times. Depending on the demands of the game mechanics, relocation may imply some changes in the game narrative, too. Typically, such changes do not concern the story line but they will affect place-related tasks and the media assets associated with them. 

## **6.4  The CityPoker Game** 

The basic idea for simplifying the design process consists in letting the students, focus on the level of narrative design. Specifically, we treat the students as novice designers and focus on place design, providing them with solutions for the design tasks at the performative and the ludic levels. 

We illustrate how to put the simplified design process into practice by using **CityPoker** as an example. This is a geogame designed by the first author, which the geogames team at the University of Bamberg has implemented for different mobile technologies. In **CityPoker** two teams of players compete to improve their poker hand by finding playing cards hidden in the geographic environment. Generally, the implementations of the game rely on a game server to synchronize the game flow, but there also exists a paper and pencil version of the game, which works with any form of direct communication between players (e.g. SMS, WhatsApp). The game narrative is as simple as any card game where the cards  represent numerical values, not characters in a story. The details of the game mechanics are summarized in Box 6.1. The geogame borrows the concept of scoring hands from the variants of the traditional Poker card game. By its game mechanics, **CityPoker** is much closer to a non-betting Poker dice game than to Poker game variants such as Hold’em. 

We concentrate on the task of place design and the role of the designers (students) in this task. We refer to the students as the “designers” keeping in mind that they are actually co-designers, since the game mechanics have been taken care of by the creators of the game. At the beginning of the game, the designers assign a hand of 5 playing cards from a deck of 20 cards to each team. The designers then hide 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

117 

## **Box 6.1 CityPoker Game Mechanics** 

CityPoker is played with a deck of 20 playing cards consisting of 10, Jack, Queen, King, and Ace in the four suits ♠ ♥ ♦ ♣. In contrast to the traditional Poker card game, CityPoker is a full information game. Each team knows the hand of the opponent team. A map, which is updated during the game shows to both teams which caches contain which cards. A team may visit each of the five caches only once. Finding the caches involves a spatial search that depends on correctly solving a place-related task. 

The game is played in real-time without turn taking. The teams move independently of each other taking the following decisions: 

- (1) identify the card that the team wants to obtain next in one of the five caches 

- (2) physically move to the cache’s search region and solve the associated task 

- (3) if solved correctly, obtain information about the cache’s exact location 

- (4) find the cache and trade in one of its cards 

The game server updates the map to reflect the changes of cards in the cache and the new hand of the team. The game ends when both teams have visited all caches or after a maximum playing time, whichever occurs first. The team with the higher-ranking hand at the end of the game wins. 

pairs of the ten remaining playing cards in five distinct places in the geographic environment. Place design amounts to identifying the places that may serve as caches for the playing cards. In designing a learning experience, the domain neutral narrative of the game has a significant advantage: it does not prompt competition for the learning outcomes. As an additional benefit, the domain neutral narrative needs no thematic adaptation. In other words, with **CityPoker** , the designers can concentrate on the task of place design. 

A variety of learning tasks have been created to build on **CityPoker** . Schlieder and Kremer (2014), for instance, used the game to design a playful activity for geography classes about urban geography. The geogames team has gained a good understanding of the game mechanics and the factors affecting the balancing of the game flow, a considerable advantage to supporting the place design process. Furthermore, Kremer et al. (2013) found that the target age group of 12–16 year old students show considerable interest in this game. 

In **CityPoker** , the caches are the POG. To qualify as POG, a place must come with an associated task that contributes to the learning objectives. In addition, the set of five places has to satisfy the requirements for a balanced game. The two features of the **CityPoker** game mechanics that have the most impact on place design are the full information scenario and the hierarchical spatial search. Both are game patterns, that is, reusable elements of the game mechanics, which may appear in 

C. Schlieder et al. 

118 

**Fig. 6.3** The geogame design process. Source: generated by the CityPoker designer using ESRI cartography 

other games, too (Björk et al. 2003; Sintoris 2015). The _full information pattern_ is found in classic board games such as chess or checkers, where there is no hidden information. This pattern generally increases the combinatorial complexity of the game and causes players to reason strategically about how their game actions will affect the opponent’s actions. 

Figure 6.3 shows a typical distribution of cards as the **CityPoker** game client would show it. Note that the map displays rectangular search regions of different sizes, but not the exact cache location. The blue marker represents the start position for both teams. Consider a game, in which one team is dealt the hand K♠ Q♣ J♥ 10♣ 10♦. There are different strategic objectives this team might pursue. It could, for instance, try a full house (K♠ K♥ K♦ 10♣ 10♦) by trading in the required kings at caches 2 and 4. The opponent team, of course, will observe the team’s actions and may prevent the strategy from succeeding by getting one of the kings first. 

With respect to place design, the number of places that a strategy involves turns out to be the critical parameter. A game, in which one team just needs to visit a single nearby cache to obtain the best-ranking hand, is imbalanced. Both teams should have comparable chances of winning. A strategy that involves visiting all five caches risks being disrupted by the opponent team or the maximum playing time. Place design, thus, has to solve a spatial configuration problem: finding five places, for which the locomotion times of both team’s optimal strategies are somewhat balanced. 

The second game pattern, _hierarchical spatial search_ , relates the search regions to the caches. On the game map, the teams see only the search region, which contains the cache but not its exact location. To obtain the exact location, the team has to solve a quiz, whose answers are associated with different geographic locations. A typical place-related task is shown in Table 6.1. Exactly one of the four answers is correct. The associated location is that of the cache, the other locations being distractors. If the team does not know the answer, it has to search at all four locations, 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

119 

**Table 6.1** Place-related task 

|**Table 6.1**Place-related task|**Table 6.1**Place-related task|**Table 6.1**Place-related task|
|---|---|---|
|_Visit one of the fruit and vegetable stalls located at the Green Market. What type of local_<br>_produce doyoufnd?_|||
|1|Eggplants|_The cache is at thefountain on the Green Market._|
|2|Asparagus|_The cache is behind the bench at Market Street No. 4._|
|3|Oranges|_The cache is at the door of Market Street No. 18._|
|4|Kiwi fruits|_The cache is in thefower box at High Street No. 24._|



which is going to slow it down considerably. Being able to exclude one or two answers reduces the number of places at which to search. Ideally, the team comes up with the single correct answer and can directly move to the cache. Note that any such quiz question is chosen specifically for the geographic environment in question. Answer 2 in Table 6.1, for instance, is true in the city of Bamberg at springtime, while it will be false in many other spatio-temporal contexts. Note also that the quiz has to be designed in such a way that there is exactly one correct answer. Table 6.1 shows the information as it would be presented in the paper-and-pencil version of **CityPoker** . The mobile game client directly displays the locations on the map without resorting to street addresses. 

We call this game pattern _hierarchical spatial search_ because it can be nested recursively. Instead of associating each answer with a location, it can be associated with another quiz question and so on. Again, the more answers are known in the hierarchical nesting of questions, the less time the players spend on spatial search. Although the authors of this chapter are not aware of other geogames making use of the hierarchical spatial search pattern, it is difficult to believe that no such game exists. The pattern is too simple and too useful as to not have been employed before. Having specified the **CityPoker** game we now move on to explain how to simplify place design, the central task at the narrative level of design (Fig. 6.2). 

## **6.5  Narrative Design: Place Design Through “Place Storming”** 

The places of interest (POI) needed for an educational geogame are generally not the topographic landmarks or touristic sites that the student designers can retrieve easily from web-based repositories of point of interest data. A geogame links places to tasks. From the point of view of the gameplay, a place is interesting only if it supports one or more tasks that relate to a specific learning objective. Designing placerelated tasks that are demanding and feasible at the same time poses some challenge. Place storming is a place generating method that helps the students to find suitable tasks by using the geographic environment as a creative stimulus and by providing a starting point for the associative process. The basic idea of place storming is 

C. Schlieder et al. 

120 

_in- situ design_ , that is, the requirement that the designer should be physically present in the POG. 

Kristiansen (2009) has suggested an in-situ method for designing games called _site storming_ . The first principle of his game design manifesto states: “site-specific games should be designed on-site”. He argues that in this way, the designers gain a better understanding of the environmental constraints on the gameplay. An evaluation of the site storming method by Kristiansen et al. (2014) concludes that the method furthers creativity. Additionally, the participants found the design discussions which happened in the geographic environment particularly inspiring. 

In adapting the site storming method for the purpose of place design, we depart in several ways from the original method. In contrast to site storming, our approach is based on group exploration and in-situ discussions in groups of students. In addition, place designers produce several designs—a task for each place—while the outcome of site storming consists in a single game mechanic. To distinguish it from site storming, we refer to our adapted method as place storming. We are aware of the fact that Anderson and McGonigal (2004) have used the same term outside game design for yet another in-situ brain storming method. However, introducing it with a different meaning in the context of geogame design should not cause confusion. 

We consider a concrete learning scenario to illustrate the place storming method with an example. A geography class (student age between 14 and 16) works on the topic of sustainable food production. The students have spent some time in class researching geographic facts about food production and sustainability. A simple fact such as “seasonal local food has a small carbon imprint” serves as starting point for developing an in-game task. Similarly, the students could start from a geographic concept (e.g. carbon imprint) or a method (e.g. determining the carbon imprint). We call such a thematic anchor a _topic_ . 

Working in class, the students compile a list of topics to use in place design. The number of topics depends on the number of POI that the place generating process should provide, which in turn depends on the number of POG the game mechanics require. For instance, in **CityPoker** the game mechanics need five POGs. As a rule of thumb, the place generating process should identify at least twice as many, that is, ten POI in order to hand over a sufficient number of POI to the place filtering process, which chooses the POG. In other words, the students prepare at least ten topics about the field of sustainable food production. 

The _topic inventory_ created by the students constitutes the first resource for place storming. The topics are best seen as a to-do list to work on. In place storming, the students explore the environment and come up with a place-related task for each topic in the inventory. The outcome of place storming consists, thus, of a list of triple associations of a topic, a task, and a place. One such association for the sustainable food scenario is shown in Table 6.2. Note that in addition to the topic-place-task association, the table also lists potential results of the task, as they would be needed for the spatial search implemented by **CityPoker** . 

In addition to the topic inventory, place storming uses an inventory of direct inputs to the creative process. The _task inventory_ loosely corresponds to the game cards of site storming. It specifies a set of templates for tasks and gives hints on how 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

121 

**Table 6.2** Topic-task-place association 

|Topic|Seasonal local food has a smaller carbon imprint than out-of-season food<br>because it requires less transportation and chilling.|
|---|---|
|Task|Visit a fruit and vegetable stall located at the Green Market that sells<br>strawberries. Speak to the vendor and fnd out where and when the strawberries<br>were harvested.|
|Place|The Green Market<br>49.89308°N,10.88860°E|
|Answer|Harvested todayat aplace less than 50 km away|
|Distractors|Harvested 3 days ago at a place less than 50 km away<br>Harvested today at a place between 50 and 200 km away<br>Harvested 3 days ago at aplace between 50 and 200 km away|



to create variations of the tasks. A place-related task template can be as simple as “Ask a local person about X”. In a variation of that template, the information asked for could be about an object shown on a photograph, which the players had to take in a prior phase of the game. We keep the task inventory deliberately small. It contains between 4 and 10 task templates (e.g. Ask someone about X, determine the geographic location of Y, collect data on Z). 

Place storming needs only few preparatory steps. Box 6.2 describes the steps in form of a checklist. The general procedure of place in-situ brainstorming follow simple protocol. The two design teams A and B from step 5 of Box 6.2 explore the environment independently. Each team, however, moves as a group. Each item on the topic inventory is assigned to at least one member of the team. To make numbers work, some members may need to share the responsibility for a topic or, conversely, take care of more than one topic. 

After the preparation phase, the teams start the spatial exploration. The student designers are instructed to carefully observe the environment and to pay special attention to places that relate to the topic(s) that have been assigned to them. When 

## **Box 6.2 Checklist for the Preparation Phase of Place Storming** 

1. The educator has covered the general theme of the game (e.g. sustainable food production) with the students in class. 

2. The students have compiled the inventory of topics, which they want to illustrate by place-related game tasks. 

3. The educator has introduced the game mechanics (e.g. CityPoker) and explained how many POG it requires (e.g. 5 in the case of CityPoker). 

4. The students have identified a local geographic region (e.g. the city’s shopping district) where they want to set up their geogame. 

5. The students have split into two design teams A and B. Team A is going to design the geogame that team B plays and vice versa. 

6. The educator and the students have agreed on a date for the out-of-class activity and allocated a maximum time (e.g. 120 min) for place storming. 

C. Schlieder et al. 

122 

**Fig. 6.4** Mobile documentation of topic-place-task associations. Source: generated by the Collector for ArcGIS using ESRI cartography 

a student feels that the team passes a place of interest, he or she stops the group to find a suitable task. This is where the task inventory comes into play. The team member responsible for the topic selects two task templates from the inventory and discusses with the others what task variant would best match the topic. The team member then documents at least two task variants from two different templates and the group moves on. The exploration stops when the topic inventory is exhausted or the maximum time planned for place storming (see step 6 of Box 6.2) has elapsed. 

Some of the parameters, of course, depend on the game mechanics. From our experience with place storming for **CityPoker** , we recommend for that game to have a topic inventory of ten items and a task inventory of just four items listing three variants for each. With 20 players in total, the teams are of size 10 and each team member takes care of exactly one topic. For an urban area with the dimensions of 500 m · 500 m, we recommend a maximum time limit for place storming of 120 min. In contrast to the place filtering process covered in the next section, place storming needs little technological assistance, if any. We found a tool such as the Collector for ArcGIS[1] helpful for documenting the topic-place-task associations (Fig. 6.4). Convenient features of a documentation tool are that it logs place coordinates automatically and stores the task descriptions on a server. 

> 1 http://www.esri.com/products/collector-for-arcgis. 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

123 

We conclude the description of place storming with a remark on the cognitive demands of the tasks generated by student designers using that method. While most tasks will be as simple as the one shown in Table 6.2, designing the task is more complex even when a template is given since it involves metacognitive reasoning. Students will have to ask selves: Would I be able to solve the task at that place with the knowledge and skills acquired in the geography class? Note that the revised Bloom taxonomy of learning objectives considers metacognitive reasoning being a highly complex competence (Krathwohl 2002). Generally, the place storming tends to require higher order cognitive processes (analyzing, evaluating, creating) whereas the learning objectives of the play phase, that is, those of the tasks designed by the students, mostly relate to lower order skills (remembering, understanding, applying). Since each student engages in both, the designing and the playing phase, a broad range of learning objectives can be addressed. 

## **6.6  Ludic Design: Game Flow Balancing Through the CityPoker Game Designer** 

The second phase of place design selects a suitable set of POG among the POI generated by the place storming method. This place filtering process differs in several respects from place storming: it is an in-class instead of an out-of-class activity and it is centered on spatial analysis instead of in-situ brainstorming. Most importantly, while place generation finds place-related tasks that match the learning objectives, place filtering tries to improve the balancing of the game flow. 

Game research has studied the computational balancing of geogames because play testing the games in the geographic environment is extremely costly. Simple game mechanics like that of **GeoTicTacToe** can be analyzed by an exhaustive search of the game’s state space (Schlieder et al. 2006). Probabilistic search is used for mechanics that are more complex. A computational analysis permits to identify place designs that guarantee fairness or prevent trivial winning strategies. Most of the results from game research require methods that are hardly accessible to students of the age range from our learning scenario (12–16 years). However, heuristics based on the findings from the computational analysis are often much simpler. In the remainder of this section we describe our adaptation of a method from computational game research, more specifically, an analysis based on the player model developed by our research group at the University of Bamberg (Kremer et al. 2013; Heinz and Schlieder 2015; Schlieder and Wullinger 2016). 

Our simplified method addresses two fundamental issues of game flow balancing with a heuristic approach. The first issue is the maximum duration of the game and the second is the fair spatial distribution of the game resources. We inform the student designers about both issues and the heuristics used by the software tool we created (Box 6.3). The two heuristics constitute the design objectives for the place filtering process. Although we use analyses that are more sophisticated in our 

C. Schlieder et al. 

124 

## **Box 6.3 Instructions to Designers for the Place Filtering Process** 

As a geogame designer, you select the places of gameplay. You are responsible for ensuring it is possible to play the game with this selection of places. In particular, you should use spatial analysis to check the following two requirements. 

1. Is the playing time acceptable? The average path from the starting point of the game through the places of gameplay and back should not take longer than 2/3 of the maximum playing time. 

2. Is the game well balanced? The distance between two places of gameplay with strong playing cards should not be significantly smaller (<1/10) than the average distance between any two places of gameplay. 

research, the heuristics give the student designers a good idea about the type of optimization that place design aims at. 

Both heuristics are specific to **CityPoker** . However, the first is based on an observation that is valid for other geogames, too: the time players spend on locomotion dominates the time spent on other in-game tasks (Schlieder and Wullinger 2016). Designers generally want to minimize locomotion time. **CityPoker** is played with 5 POG, the places where the playing cards are hidden. Each team should have the opportunity to visit all 5 caches. Since the visit order depends on the team’s plan as well as on the actions of the opponent team, we consider all possible 120 = 5! visiting orders. The upper diagram in Fig. 6.5 shows a typical distribution of locomotion time for the 120 visiting orders, which are ranked from the shortest to the longest. Note that the solution to the classical travelling salesperson problem is found at rank 1. The heuristic is based on the median of the locomotion times and requires that it should not exceed 2/3 of the planned maximum playing time leaving at least 1/3 of the time for the place-related tasks. If the maximum playing time is 60 min, the student designers have to choose the POG in such a way that the median of the locomotion times is 40 min or less. 

The second heuristic relates to the spatial distribution of the playing cards. The cards considered strong and how this perception affects the game depends upon the strategies adopted by players. We used an agent-based simulation framework (Heinz and Schlieder 2015) to explore the effects of the strategies on different placements of the cards. Figure 6.5 shows a snapshot of a simulation run with the POG represented by pink polygons and the two player agents by green dots. The heuristics avoids putting strong playing cards in nearby places. 

At this point, the students have completed the place generation phase and compiled an inventory of POI. This inventory lists at least ten places together with their topic-place-task associations and serves as a starting point for selecting the five POG needed for CityPoker. The **CityPoker Game Designer** or **CityPokerGD** , is a web-based application, which guides the student designers through the process of 

125 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

**Fig. 6.5** Locomotion time and agent-based modeling 

place filtering. We created the web application for use in the classroom, thus the students access the **CityPokerGD** using their preferred web browser on a  notebook or tablet computer. The application guides the students through all phases of the place filtering process explaining the steps of the analysis and providing help functionality. 

In **CityPokerGD** , we decomposed the process into a sequence of manageable subtasks that implement an iterative improvement process. The student designers start with selecting an initial configuration of POG from the inventory of POI. Depending on the results of the analysis of the initial configuration, the students discuss changing some of the places. If changes are necessary, the procedure restarts for the modified configuration of places and iterates until the spatial analysis returns a satisfying result. At the end of the place filtering process, when the students have identified the POG for the game, the **CityPokerGD** generates a descrip- 

126 

C. Schlieder et al. 

**Table 6.3** Subtasks of place filtering 

|**Table 6.3**|**Table 6.3**Subtasks of place filtering||
|---|---|---|
||Subtask definition|CityPoker Designer|
|1|_Geographic framing_: define the geographic environment of the<br>game|Start point|
|2|_Place selection_: Choose a configuration of POG from the POI<br>inventory|Cache placement|
|3|_Resource selection_: assign playing cards to the POG; define<br>distractor locations|Card distribution<br>Distractorplacement|
|4|_Task selection_: assignplace-related tasks for each of the POG|Cache field data|
|5|_Game field review_: reiterate steps 2–6 if the POG configuration<br>needs improvement|Game field|



**Fig. 6.6** User interface of the CityPoker Game Designer 

tion of the game. This is a configuration file for the game server or a PDF document for players who want to play the paper and pencil version. 

Table 6.3 shows the subtasks supported and the titles given to them by the tool. The table lists the subtasks in the order that the tool guides the students through the process of place filtering. It is important to note that the decomposition into subtasks does not impose a strictly linear workflow. Students may address the subtasks 3–5 in a different order. They can also switch back and forth between the subtasks before having completed them. In practice, most students follow the suggested ordering of tasks in their first iteration, but move more freely in subsequent iterations. 

The user interface of the **CityPokerGD** supports the subtasks with a specific input and feedback mode. Three elements define the interaction: an instruction panel, an interaction panel, and a feedback panel (Fig. 6.6). The instruction panel 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

127 

explains the interface elements that are visible as well as the actions the students have to take to complete the subtask. The students use the interaction panels to communicate decisions to the application and to input data. In the example of Fig. 6.6 it is an interactive map that serves as the interaction panel. Finally, the feedback panel informs designers of unresolved design problems. In many cases, it communicates the results of a spatial analysis that the **CityPokerGD** runs in the background. The feedback panel also informs about the state of completion of a subtask. Color- coded information boxes show at a glance which data has been provided completely (green) or partly (yellow), and which data is still missing (red). 

_Geographic framing_ : On opening the **CityPokerGD** , the users see a welcome screen, which explains the purpose of the application and provides a link to the rules of the **CityPoker** geogame. The students first define the geographic region of the game. They do so by either entering a city name, specifying a latitude and longitude, or clicking on a position of a web map. The first subtask also involves defining the start and end point of the game, a single place both competing teams move from at the beginning of the game and return to when the game is finished. Like all other design decisions, the position of the starting point can be revised at a later stage. 

_Place selection_ : In this subtask, the student specifies the configuration of places that he or she wants to use as POG for **CityPoker** . The places are input by locating them on an interactive map. As soon as a place is specified, the application performs several background computations. First, it computes the shortest pedestrian routes between the new place and the places that are already part of the configuration of POG. The application displays the routes on a map to help understanding the effects of the choice (see Fig. 6.6). With the visualization, the student can check the accessibility of the place for pedestrians, for instance. The second piece of information from the spatial analysis is the estimated playing time. Using the heuristics described at the beginning of this section, the application computes an upper and a lower bound, which is then displayed to the student designer. The application computes new routes and time bounds whenever the designer moves one of the POG to a new location. By giving immediate visual feedback, the **CityPokerGD** encourages playing around with different spatial configurations. This helps the students to anticipate which of the places from the POI inventory will actually improve the gameplay. 

_Resource selection_ : In **CityPoker** , the game resources are the playing cards hidden in caches located at the POG. The student designer assigns two playing cards to each of the POG. Once the cards are assigned, the **CityPokerGD** applies the heuristics for evaluating whether the game is balanced (Fig. 6.7). The application warns the student designer if extremely strong pair of cards are located too close to each other. In addition, distractors need to be defined. Although distractors are geographic locations, they are more similar to resources than places, and they are required for the hierarchical spatial search pattern that our game uses. The distractors are always located in the vicinity of a POG, and their exact position does not have a big effect the gameplay as far as the heuristic evaluation from Box 6.3 is concerned. With respect to the distractors, the application checks that the student designer has defined them all. 

C. Schlieder et al. 

128 

**Fig. 6.7** Card distribution 

_Task selection_ : This subtask can be seen as mere data input step since it does not involve decisions that affect the balancing of the game. The student just copies the task description from the POI inventory into a **CityPokerGD** and assigns possible results of the task to the POG and the distractors. A design decision is taken only in cases where the POI inventory contains alternative tasks associated to a place. Even in such a case, the decision will affect the game play but not the spatio- temporal balancing. 

_Game field review_ : In this last step, the student designing the game reviews all of the game data. He or she decides whether to continue improving the place design or to finalize the geogame. 

Although the students could work independently with the **CityPokerGD** , working in groups stimulates discussions and generally produces better results. Based on our experience with the design process, we recommend that each of the two design teams splits up in groups of 3–4 students. The games produced by the groups of one team will generally differ in the choice of the POG as well as in the task associated with the POG. In a final team meeting, the members decide which of the results becomes the team’s geogame that is going to be played by the other team. 

## **6.7  Discussion and Outlook** 

We have covered quite a lot of ground in this chapter. For the final discussion, let us return to our starting point: designing a geogame in the classroom. While teachers have used geogames in a variety of learning contexts in secondary education, they generally avoid letting the students themselves design the game because of the 

6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task 

129 

alleged complexity of the task. In this chapter, we have identified an important part of the geogame design process, namely game relocation and, more specifically, place design, which is at the same time sufficiently challenging and not too complex to be of interest in an educational context. We provided the methodological and technical means for addressing place design in the classroom. 

Now that we have detailed our approach, it is apparent how the three geogame design principles to enhance student learning stated at the beginning of the chapter are implemented. The first principle asked for starting with a rule set known to produce a well-balanced game. We did this by applying place design to the **CityPoker** geogame. The second principle consisted in letting the students explore the geographic environment of the game. With the place storming method, we provided a solid basis for this phase of the design process. Finally, we showed how to optimize the game flow as stated in the third principle. We formulated heuristics for spatial analysis and we created a software tool, the **CityPokerGD** , to implement the heuristics. 

All of these elements together provide a blueprint for a class on geogame design. This has been our primary goal. However, our analysis also contains material that is neither specific to a particular geogame nor to geogame design education. We are convinced that the design process model we presented will prove useful in other application scenarios, too. Most importantly, the model helps to understand the importance of place design in game relocation. Game relocation has evolved into a topic of active research, and is also addressed by other chapters of this book. However, as described in this chapter, place design has received much less attention. Place design is especially challenging because designers cannot look exclusively at the spatial constraints of the problem. In moving a successful game from one geographic environment to the other, there are other aspects to consider, most notably, social and cultural constraints. This relates place design to the recent research activities on place-based GIS, which also aim at capturing the social meaning of spatial entities. 

**Acknowledgments** This research has been funded in part by ESRI Inc. within the Geogames and playful Geodesign project. 

## **References** 

Adams E, Dormans J (2012) Game mechanics. Advanced game design. New Riders, Berkeley, CA Althoff T, White RW, Horvitz E (2016) Influence of Pokemon go on physical activity: study and implications. J Med Internet Res 18(12):e315. Preprint arXiv:1610.02085 

> Anderson K, McGonigal J (2004) Place storming: performing new technologies in context. In: Proc. Nordic conf. on human-computer interaction. ACM Press, New York, pp 85–88 Björk S, Lundgren S, Holopainen J (2003) Game design patterns. In: Raessens J, Copier M, Goldstein J, Mäyrä F (eds) DiGRA-03: conference on digital game research. Digital Game Research Association, Utrecht, NL 

> Celtek E (2010) Mobile advergames in tourism marketing. J Vacat Market 6(4):267–281 

C. Schlieder et al. 

130 

- De Gloria A, Bellotti F, Berta R (2012) Building a comprehensive R&D community on serious games. In: VS-GAMES-12, proceedings of international conference on games and virtual worlds for serious applications, pp 1–3 

- de Souza e Silva A (ed) (2009) Digital cityscapes. Merging digital and urban playspaces. Lang, New York, NY 

- Heinz T, Schlieder C (2015) An agent-based simulation framework for location-based games. AGIILE-16 proceedings of international conference on geographic information systems. https:// agile-online.org/conference_paper/cds/agile_2015/shortpapers/114/114_Paper_in_PDF.pdf 

- Hodson H (2012) Google’s ingress game is a gold mine for augmented reality. New Scientist 216:19 

- Klopfer E (2008) Augmented learning—research and design of mobile educational games. MIT Press, Cambridge, MA 

- Krathwohl D (2002) A Revision of Bloom’s Taxonomy, Theory into Practice 41(4):212–264 

- Kremer D, Schlieder C, Feulner B, Ohl U (2013) Spatial choices in an educational geogame. In: Proceedings of VS-Games 2013 (5th international conference on games and virtual worlds for serious applications) 

- Kristiansen E (2009) Computer games for the real world: designing a design method for sitespecific computer games. PhD thesis. Roskilde University. pervasivegames.files.wordpress. com/2010/05/ekfinal2.pdf 

- Kristiansen E, Pries-Heje J, Baskerville RL (2014) Designing scientific creativity. In: Proceedings of Scandinavian conference on information systems. Springer, Berlin, pp 44–57 

- Lude A, Schaal S, Bullinger M, Bleck S (2013) Mobiles, ortsbezogenes Lernen in der Umweltbildung und Bildung für nachhaltige Entwicklung (in German: Mobile, locaton-based learning in environmental education). Schneider Verlag, Baltmannsweiler 

- Montola M, Stenros J, Waern A (eds) (2009) Pervasive games. Theory and design. Morgan Kaufmann Publishers, Burlington, MA 

- Schaal S, Grübmeyer S, Matt M (2012) Outdoors and online-inquiry with mobile devices in preservice science teacher education. World J Educ Technol 4(2):113–125 

- Schlieder C, Kiefer P, Matyas S (2006) Geogames: designing location-based games from classic board games. Intell Syst IEEE 21(5):40–46 

- Schlieder C, Kremer D (2014) Geogames: Schüler entwickeln ein ortsbezogenes Spiel (in German; Geogames: students develop a location-based game). Praxis Geogr (7/8):31–35 

- Schlieder C, Wullinger P (2016) Reducing locomotion overhead in educational geogames. In: Gartner G, Huang H (eds) LBS-16, proceedings of international conference on location based services. ACM, New York, pp 228–232 

- Sintoris C (2015) Extracting game design patterns from game design workshops. Int J Intell Eng Inf 3(2-3):166–185 

- Sinton D, Lund J (eds) (2007) Understanding place understanding place: GIS and mapping across the curriculum. ESRI Press, Redlands, CA 

- von Borries F, Walz S, Böttger M (eds) (2007) Space, time, play: computer, games, architecture, and urbanism. Birkhäuser, Zürich
