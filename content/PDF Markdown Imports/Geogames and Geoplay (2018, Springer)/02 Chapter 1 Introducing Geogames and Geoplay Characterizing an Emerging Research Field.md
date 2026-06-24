---
title: "Chapter 1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field** 

## **Ola Ahlqvist and Christoph Schlieder** 

## **1.1  Introduction** 

Games and play are part of human life, and place, space, and geography take central roles in determining the rules and interactions of games. Consider how integral maps are to the board game RISK, how video game players navigate through a realistic ‘world’ in pursuit of a goal, the millions of Pokemon Go players navigating the real world to find new Pokemon. Even the very abstract maps of Monopoly and Chess are inherently geographical, utilizing basic spatial rules for game play. 

This is a book about games that use real-world information and geographic information technologies. As such it is the first of its kind, which may sound surprising considering the ubiquity of geographic information (GI) technologies and locationbased applications in modern life. We use navigation apps to find our way from A to B, we check in at places with social apps, and digital photographs typically contain the location of each picture as part of the data file. However, this widespread access to mobile information, communication, and geospatial technologies only very recently inspired any significant development of gaming activities that are connected to the real world. Terms for these games began appearing around 2004–2005: pervasive games, ubiquitous games, augmented-, alternate-, and mixed-reality games, mobile games, and adaptronic games. 

We seek to provide a wide umbrella for this first book, and with the title _Geogames and Geoplay_ we consider all games and play that uses real geocontent and is 

O. Ahlqvist ( * ) 

Department of Geography, The Ohio State University, 1049B Derby Hall, 154 N Oval Mall, Columbus, OH 43210, USA e-mail: ahlqvist.1@osu.edu 

C. Schlieder Faculty of Information Systems and Applied Computer Sciences, University of Bamberg, Kapuzinerstraße 16, 96047 Bamberg, Germany 

© Springer International Publishing Switzerland 2018 

1 

O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_1 

O. Ahlqvist and C. Schlieder 

2 

mediated by GI technology. In the following subsections we will elaborate further on this definition, and the chapter concludes with an introduction to the rest of this book. The authors of the book chapters are representative of a diverse community of researchers and designers, a community, we must add, which has not agreed on a standard terminology for describing geographic gameplay so far. We have refrained from asking the authors to commit to a list of technical terms created by the editors because we could foresee that they would return to their preferred terminology in their very next publication. We have taken care, however, that each chapter defines its core concepts. A prominent case is the term “geogame” itself, which some chapters use in a narrower sense than we do here. 

## **1.2  GIS/Spatial Principles and Game Patterns** 

A key motivation for this book was the conception that geocontent, i.e. real-world spatial information, brings something unique to games and play. Many of the terms mentioned above (mobile, location-based, etc.) have become associated with particular technologies, which means that they would be subject to change with constantly changing technology. We therefore seek a more stable and generic way to characterize and define the realm of “Geogames and Geoplay”. 

This calls for an examination of what elements define the geographic dimension and the gaming dimension of geogames. In the following sections we will interrogate some of the existing literature on the core concepts for geographic information and game design. After this, we will provide two different perspectives on how the two realms of Geo and Games map onto each other. 

## _**1.2.1  Core Geographic Concepts**_ 

In an effort intended to support “…a broader use of spatial information in science and society”, Kuhn (2012) sought to provide an understanding of what spatial information is and how it can be used across disciplines and populations in science and society. He identified ten core concepts of _spatial information_ to guide experts, scientists and practitioners across a wide range of disciplines. The ten concepts are: Location, Neighbourhood, Field, Object, Network, Event, Granularity, Accuracy, Meaning, and Value. Although Kuhn and Ballatore (2015) later narrowed this list of core concepts down to seven, eliminating Neighborhood, Meaning, and Value, because we are interested in identifying a comprehensive collection of core concepts, we will consider the original ten in our following discussion. 

Another theory of core geographic concepts related to _spatial thinking_ was developed around the same time, but independently of Kuhn, by Janelle and Goodchild (2011). Their concepts were a synthesis of several previous works and identified the following nine as a foundation for _spatial reasoning_ : Location, 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

3 

Distance, Neighborhood and Region, Networks, Overlays, Scale, Spatial Heterogeneity, Spatial Dependence, Objects and Fields. It should be noted that these two proposals are slightly different in their objectives. While Kuhn’s focus is on spatial information and its properties, Janelle and Goodchild focus on spatial thinking in the social sciences. So, by examining the two proposals side by side (Table 1.1) we find significant overlaps, but also some unique contributions that forms a tentative synthesis of the two perspectives. 

Kuhn does not identify distance per se as a key concept, but rather suggests that “nearness” is “...a natural companion concept to location” and part of his “Neighbourhood” concept. Other than those small nuances, the first halves of the two frameworks, as listed above, largely agree (see Table 1.1). 

Differences are most clear upon reaching Kuhn’s (2012) concept of Event (time), and the non-spatial information concepts of Accuracy, Meaning and Value. Janelle and Goodchild include the analytical concepts of Overlays, Spatial Heterogeneity and Spatial Dependence. It seems clear from Janelle and Goodchild’s presentation that time is considered an integral component of their Fields/Objects concept where they explicitly talk about space-time. The remaining differences are clearly related to the different perspectives taken by each proposition. Accuracy, Meaning and Value are all specific and central to geographic _information_ , whereas Overlays, Spatial heterogeneity and Spatial dependence are all foundational ideas to spatial _thinking_ . 

Thus, we will consider the unified list (right column in Table 1.1) as a preliminary comprehensive list of core concepts for geographic information and thinking. With this conceptual framework in place for the “Geo” realm, we now turn our attention to the “Game” realm. 

## _**1.2.2  Core Game and Play Concepts**_ 

In game design there is no direct equivalent to the core geographic concepts. Game designers have looked, however, for methods and typologies assisting them in reducing the complexity of their task. As in other design disciplines, most notably in architecture and software engineering, a compositional approach has proven successful. This approach describes a design as consisting of interrelated conceptual building blocks, so-called patterns. When Björk, Lundgren, and Holopainen (2003) introduced patterns into game research, they did so by explicitly referring to the already well-established software design patterns of Gamma et al. (1995). Using that perspective, a game pattern describes a generic solution to a specific class of design problems. The high-score list pattern, for instance, solves the problem of instigating competition among players without implementing a full-blown multi- player game flow. Like in software engineering, patterns are associated with trade- offs and design implications, which are included in the pattern description. 

O. Ahlqvist and C. Schlieder 

4 

**Table 1.1** Alignment and differences between core geographic concepts proposed for spatial information (Kuhn 2012; Kuhn and Ballatore 2015) and for spatial thinking (Janelle and Goodchild 2011) 

|2011)|||
|---|---|---|
|Kuhn (2012), Kuhn and<br>Ballatore(2015)|Janelle and Goodchild<br>(2011)|Proposed unifed core<br>geographic concepts|
|**Location**—answers_where?_<br>but should be understood as<br>a relation between fgures<br>located with respect to a<br>chosenground|**_Location_**—formal and<br>informal methods of<br>specifying “where”<br>(locations and divisions of<br>the world)|**Location**—formal and informal<br>ways of specifying_where?_|
||**_Distance_**—relationships<br>between places by<br>measures ofproximity|**Distance**—relationships between<br>places/objects by measures of<br>(space-time) proximity|
|**Neighbourhood**—answers<br>_what is near?_commonly<br>thought of as regions|**_Neighborhood and_**<br>**_Region_**—drawing<br>inferences from spatial<br>context (situations and<br>neighborhood ofplaces)|**Neighborhood**—identifes<br>places/regions in terms of<br>distance and spatial context|
|**Field**—describe continuous<br>phenomena that have an<br>attribute everywhere in a<br>space of interest|**_Fields_**a—phenomena that<br>are continuous in<br>space-time|**Field**—continuous phenomena<br>that have a thematic attribute<br>everywhere in space-time|
|**Object**—describe<br>individuals or elements that<br>have an identity as well as<br>spatial, temporal, and<br>thematicproperties|**_Objects_**a—phenomena that<br>are discrete in space-time|**Object**—individuals that have<br>an identity as well as spatial,<br>temporal, and thematic<br>properties|
|**Network**—connectivity as<br>captured by binary<br>relationships between nodes<br>(objects)|**_Networks_**—linear networks<br>with connections and fows|**Network**—relationships<br>(connections and fows) between<br>objects (nodes)|
|**Granularity**—amount of<br>detail in spatial information|**_Scale_**—level of detail in a<br>geographic dataset|**Granularity/Scale**—extent and<br>amount of detail in spatial<br>information|
|**Event**—an individual<br>portion of a process,<br>bounded in time||**Event**—an individual portion of<br>a process, bounded in time|
||**_Overlays_**—inferring spatial<br>associations by comparing<br>mapped variables by<br>locations|**_Overlays_**—inferring spatial<br>associations by comparing<br>mapped variables by locations|
||**_Spatial heterogeneity_**—the<br>implications of spatial<br>variability|**_Spatial heterogeneity_**—<br>implications of spatial variability|
||**_Spatial dependence_**—<br>understanding relationships<br>across space|**_Spatial dependence_**—<br>understanding relationships<br>across space|
|(continued)|||



5 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

**Table 1.1** (continued) 

|**Table 1.1**(continued)|||
|---|---|---|
|Kuhn (2012), Kuhn and<br>Ballatore(2015)|Janelle and Goodchild<br>(2011)|Proposed unifed core<br>geographic concepts|
|**Accuracy**—difference<br>between spatial information<br>and some reference<br>considered ‘true’||**Accuracy**—difference between<br>spatial information and some<br>reference considered ‘true’|
|**Meaning**—how to interpret<br>terms in spatial information||**Meaning**—how to interpret<br>terms in spatial information|
|**Value**—the roles played by<br>spatial information in society||**Value**—the roles played by<br>spatial information in society|
|aObjects and Fields are presented together as one concept by Janelle and Goodchild|||



Two inventories of game patterns are of special interest to the study of geogames and geoplay. Davidsson et al. (2004) compiled a collection of 74 patterns. It is less comprehensive than the list identified by Björk and Holopainen (2004), but in our context, it has two advantages: First, the patterns are specific to games played on mobile devices, while the more extensive list refers to all kinds of games from precomputer children’s puzzles to survival horror video games. Second, and more important, the identification of the pattern inventory relies on a systematic method in which expert game designers analyze a set of well-known model games. More recently, Sintoris (2015) has identified another inventory of 41 game patterns using a comparable method and focusing on location-based games only (all studied games use some kind of positioning technology and let the players interact with the geographic environment). Detailed pattern descriptions are available on the project’s Wiki (Sintoris 2015). 

In the context of geogames that are not location-based, it is useful to also look at inventories of general, not just spatial, game patterns. Building on earlier works on game patterns, Holopainen (2011) developed a component framework to help navigate and define general design patterns that have been identified. He identified 18 components as the “basic building blocks” of games and grouped them into four categories: (1) Holistic—These components help in defining how gaming differs from other activities and describing how players can join and end a specific game. The holistic components are: **Game Instance** , **Game Session** , **Play Session** , **Set-up and set-down sessions** , and **Extra-Game Activities** that are related to but not directly affecting game play itself. (2) Bounding—These components define purposes for playing the game and permissible game play activities. The bounding components are: **Rules** , **Modes of Play** , **Goals and Sub-goals** . (3) Temporal— These components record the game play by identifying and separating a larger game play activity into temporally separated activities. The temporal components are: **Actions** , **Events** , **Closures** , **End Conditions** , **Evaluation Functions** . (4) Structural—These components describe the basic parts of the game, such as objects representing real-world or imaginary objects, people or creatures, or abstract phenomena like values or attributes. The structural components are: **Game Facilitator** , 

6 

O. Ahlqvist and C. Schlieder 

**Players** , **Interface** , **Game Elements** , **Game Time** —In a similar effort, and also informed by the early work on game design patterns, Järvinen (2008) identified nine Key Game Elements as generic classes of things that make up an entire game system and suggested they could be used for analyzing games. They are: **Components** , **Rule Set** , **Environment** , **Game Mechanics** , **Theme** , **Information** , **Interface** , **Player(s)** , and **Contexts** . While Holopainen’s work primarily uses a game design perspective, the elements identified by Järvinen is derived from a more user oriented perspective. Maybe due to this difference the correspondence of these two typologies are not as apparent as with the previous spatial concepts, but examining them side by side does allow us to assess possible alignments as well as unique ideas, just as we did with the spatial concepts in Table 1.1. 

As we can see in Table 1.2, these two separate efforts display some similarities and overlaps, but also significant differences. Maybe the largest difference is Holopainen’s (2011) temporal components of Game instance, Game session, Play session, Set-up & set-down, Extra game activities, and Game time, which do not have a direct equivalent in Järvinen’s (2008) game elements. Järvinen discusses these in terms of ‘game states’ as temporal reference points, but never raises it to the level of a separate game element. Rather, it is something that his compound ‘Information’ element would capture through query of the system. The benefits of Holopainen’s more specific set of concepts is that we get a vocabulary for talking about a simulation as a closed event with particular sub-components. Similarly, Holopainen provides a more specific vocabulary for the rules, policies, goals and events that emanate from play activities. These are all more or less subsumed by Järvinen’s much broader term “Rule set”, but they identify a collection of unique temporal concepts related to specific aspects of game events and procedures that are ultimately governed by rules. Järvinen’s game elements Contexts and Theme do not have a direct correspondence in Holopainen’s components. This is probably due to Järvinen’s focus on semiotic, rhetorical and cultural aspects of games. As we will see in the next section though, these elements seem to have direct alignments with some of the core geographic concepts identified previously. For the remaining elements and components there seems to be a fairly obvious alignment of concepts related to interface, player actions, and the game ‘world’. 

## **1.3  Reconciling Core Geographic and Game Concepts** 

We are now ready to examine the geographic and game dimensions together, as articulated in the core concepts identified in the previous section. We will first highlight how spatial information processing relates to the game patterns from the inventory of Davidsson et al. (2004) and the inventory of Sintoris (2015), we then provide a complementary perspective on how the core concepts of games and play from Table 1.2 can enrich the geographic core concepts in Table 1.1. 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

7 

**Table 1.2** Alignment and differences between proposed game components (Holopainen 2011) and key game elements (Järvinen 2008) 

|**Table 1.2**Alignment and differences between<br>and key game elements (Järvinen2008)|proposed game components (Holopainen2011)|
|---|---|
|Game components|Key game elements|
|Holopainen(2011)|Järvinen(2008)|
|**Game Instance**—a single completion of<br>game play as a unique confguration of a set<br>of players, the place where it is played, and<br>external circumstances under which it is<br>played<br>**Game Session**—the activity undertaken in a<br>game instance by the game’s players<br>**Play Session**—several distinct periods of<br>game play activity inside a game session<br>**Set-up and Set-down Sessions**—game and<br>play activities that do not constitute game<br>play directly but are required and take place<br>nevertheless<br>**Extra-Game Activities**—any extra activities<br>related to the game but not directly related to<br>playing the game itself.<br>**Game Time**—the timeline of sequentially<br>ordered actions in agame session|**Information**—information about events, agents,<br>objects, and the system state|
||**Contexts**—where, when and why the game<br>encounter takesplace.|
|**Rules**—explicit or implicit policies that<br>dictate the fow of the game<br>**Modes of play**—sections, phases or turns<br>where the interface, available actions, and<br>information for the players—and thus also<br>the activities—are very different.<br>**Goals and sub-goals**—the aim of players’<br>plans and actions in a game<br>**Events**—discrete points in game play where<br>the game state changes<br>**Evaluation Functions**—determines the<br>outcome of an event<br>**Closures**—the completion of a goal or a<br>sub-goal<br>**End conditions**—the game states when<br>closures occur and when the game instance<br>ends.|**Rule set**—procedures that governs game play,<br>permissible actions, etc.|
|**Actions**—discrete or continuous player<br>actions that change the game state|**Game mechanics**—actions that players can<br>engage in as part of playing, e.g. placing,<br>shooting,maneuvering,trading.|
||**Theme**—the subject matter of a game, often<br>used to provide a metaphor for the game system<br>and rule set, e.g. a treasure hunt or a command<br>and conquer historic war scenario.|
|(continued)||



O. Ahlqvist and C. Schlieder 

8 

**Table 1.2** (continued) 

|**Table 1.2**(continued)||
|---|---|
|Game components|Key game elements|
|Holopainen(2011)|Järvinen(2008)|
|**Game Facilitator**—oversees the workings<br>of a game, taking care of the game events,<br>rules and also resolves possible disputes.<br>**Players**—the entities that strive toward the<br>goals in a game by choosing and performing<br>actions.|**Players**—people who play|
|**Interface**—the different types and forms of<br>representations by which players have access<br>to a game|**Interface**—various means, devices and tools<br>that allow players to access and interact with the<br>other game elements, e.g. pen and paper,<br>computer screen, pointingdevice.|
|**Game Elements**—the physical and logical<br>attributes that help maintain and inform<br>players about the current game state|**Components**—the resources for play that are<br>moved or modifed in game transactions, e.g.<br>tokens, tiles, characters, vehicles.<br>**Environment**—the space for play, e.g. a<br>specifc setup, game board, grid, maze, level,<br>world.|



## _**1.3.1  Spatial/Non-spatial Game Patterns and Core Geographic Concepts**_ 

While the game pattern inventories (Davidsson et al. 2004; Sintoris 2015) described in the previous section do not cover the entire field of geogames and geoplay, they nevertheless provide us with an opportunity to assess the role of spatial concepts in an important subfield of spatial game design. We evaluated the pattern descriptions of the two inventories using the core spatial concepts (Table 1.1) occurring in them. Verbatim occurrences (e.g. “proximity”) as well as paraphrases (e.g. “the distance between the player and a certain physical location” for “proximity”) were noted, and patterns, which explicitly referred to at least one core concept were categorized as having a strong spatial component. The analysis of the pattern descriptions from Davidsson et al. (2004), reveals that 23 (31%) of the 74 patterns have such a strong spatial component. The “Strategic Locations” pattern is one example. Its description states: “Mobile games … often make use of strategic locations where players receive special benefits”. A portal in the Ingress game, for instance, constitutes such a strategic location that players must interact with in order to win the game. Most patterns, however, are non-spatial like the “Highscore List” pattern. Interestingly, the analysis of the inventory of Sintoris (2015) produces a similar result. 

Again, a part of the patterns, 13 (32%) from 41, show a strong connection to spatial information. Considering both inventories, we find that, roughly speaking, one third of the game patterns are spatial. To a certain extent, this explains why a designer may get along for some time without caring much about spatial information processing. Location-based geogames are first and foremost games. Spatial information processing is secondary and only involved to the extent needed to support 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

9 

**Table 1.3** Fundamental spatial game patterns 

||Characteristics of the cluster<br>ofgamepatterns|D = Davidsson et al.<br>(2004)|Associated core<br>concepts|
|---|---|---|---|
|||S = Sintoris(2015)||
|**Locality**|entering (or leaving) a place<br>enables specifc game actions|Strategic locations<br>(D 28)|Location object|
|||Spatial structure (S<br>6.4)||
|||Co-locality (S 3.18)||
|**Proximity**|approaching (or gaining<br>distance from) a player or<br>artifact triggers game events|Player-location<br>proximity (D 8)|Distance neighborhood<br>feld overlays|
|||Artifact-location<br>proximity (D 9)||
|||Player-player<br>proximity (D 10)||
|||Artifact-artifact<br>proximity (D 13)||
|||Proximity (S 6.2)||



game design goals. However, with one-third of the patterns being related to spatial concepts, these patterns bear considerable potential to improve a design. This is where the geographic core concepts can demonstrate their utility. They allow us to establish a correspondence between spatial game patterns and the core concepts, which reveals in which respect both inventories are still incomplete. Note that the two inventories (Davidsson et al. 2004; Sintoris 2015) do not identify exactly the same set of spatial patterns. This is not too surprising as they were elicited from two different sets of model games. Since we are interested in a common core of patterns, we used the underlying concepts of spatial information processing to group the game patterns from both inventories into clusters. The grouping is based on the pattern descriptions found in the two inventories. We group together patterns, which predominantly refer to the same core concept. 

At the most basic level, two clusters of patterns emerge: locality and proximity (Table 1.3). Locality patterns refer to places, that is, to geographic positions with a game-specific meaning (e.g. a portal in the Ingress game). Most game designers model such places as objects with spatial boundaries. The spatial position of the player with respect to the places determines the available game actions. Locality patterns require some positioning technology that determines automatically whether the player enters a place and may perform the intended action. Proximity refers to the concepts of distance and neighborhood, and the variation of proximity constitutes a (local) field where the closeness to a location, to another player, to a virtual or a real artifact triggers a game event. Such patterns are based on a gradual decision function, which is why the inventory of Sintoris (2015) associates these patterns with the hot-cold type of feedback given to players. 

O. Ahlqvist and C. Schlieder 

10 

**Table 1.4** Spatial activity game patterns 

||Characteristics of the cluster of<br>gamepatterns|D = Davidsson et al.<br>(2004)|Associated core<br>concepts|
|---|---|---|---|
|||S = Sintoris(2015)||
|**Navigation**|identifying and following a<br>route in geographic space|Physical navigation<br>(D 5)|Network<br>granularity|
|||Path-fnding (S 3.7)||
|**Race**|Reaching a place before other<br>players do|Race(D 31)|Event accuracy|
|||Competition(S 1.3)||
|**Collection**|Identify, locate and get hold of<br>an object|Collection(D 71)|Event value|
|||Collecting (S 3.17)||



The locality and proximity patterns are fundamental in the sense that any location- based game engine has to support at least one such pattern. Other game patterns refer to more complex core concepts like network, granularity, event, accuracy or value. It is possible to identify associated clusters of patterns describing different spatial activities (Table 1.4). We found three such clusters in the two inventories: navigation patterns, race patterns, and collection patterns. Interestingly, some patterns frequently found in location-based games are missing. Two examples are spatial exploration patterns such as hierarchical spatial search and spatial movement patterns such as flock movement or encirclement. It would be extremely helpful for the design of spatial game engines to have a complete list of spatial activity patterns. Anyone attempting to do a complete review of spatial activity patterns should start with a more comprehensive list of model games. We must leave this task to future research. 

Besides the fundamental spatial patterns (Table 1.3) and the spatial activity patterns (Table 1.4) there is a third group of patterns, which we might call spatial interaction patterns. They are more complex in that they involve social conventions and interactions. We will not list them in a table because the inventories mention only a single one: the gaining ownership pattern (No. 29 in Sintoris 2015). The dearth of spatial interaction patterns suggests that the inventories are quite incomplete. 

Although our observations on the importance of the core concepts to game design are restricted to location-based geogames, they may transfer to other geogames, for instance, geographic simulation games. Very likely, an analysis of a set of model simulation games will also reveal the fundamental patterns of locality and proximity. The spatial activity patterns (e.g. race) might be different and the social interaction patterns (e.g. ownership) will most likely be more complex in simulation games than in location-based geogames. 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

11 

## _**1.3.2  Intersection of Core Geographic Concepts with Games and Play**_ 

There are also some direct correspondence or similarity between the game components/elements (Holopainen 2011; Järvinen 2008) and core geographic concepts. In an effort to identify those overlaps and to possibly enrich the core geographic concepts with some of the unique aspects that games embody, we have tried to align the core geographic concepts from Table 1.1 with the two described typologies for game analysis from Table 1.2. Our proposed alignment can be found in Table 1.5 below, where we list the previously proposed collection of unified core geographic concepts in the left column and the game components and elements in the middle and right column. In addition, we tentatively suggest Rules, Agents, Interface, and Simulation as new concepts to be added to the set of core geographic concepts in order for them to capture the particulars of not only geogames but geographic simulations in general. These additional concepts will also be discussed below. 

Some of Järvinen’s elements have close correspondence with the core geographic concepts: **Components** and **Environment** —roughly corresponding to the discrete objects and continuous fields (or tessellations) of spatial information; **Theme** — roughly corresponding to that of thematic maps, determining the subject matter and its meaning. 

A few other elements closely correspond to other well-known geographic concepts, yet these are not listed among the ‘core’ concepts: **Ruleset** —roughly corresponding to rules in spatial simulation and modelling; **Interface** —corresponds with the devices used to interact with the GIS, usually a computer or mobile device; **Players** —roughly corresponds to GIS users with the important caveat that it does not include game designers, hence not including for example GIS programmers, database managers, data producers etc. Although, in a spatial simulation context, players would more likely be equated with agents as in Agent Based Modelling, and Holopainen’s (2011) game components related to game and play sessions closely correspond to the act of running a **Simulation** of a geographic system model. The fact that these are not directly associated with any of the Kuhn and Ballatore/Janelle and Goodchild core concepts suggests that the area of geogames offers an opportunity for identifying important gaps in the set of core geographic concepts. We propose variants of these existing concepts from the game design literature as four new additions, _**Rules**_ , _**Agents**_ , _**Interface**_ and _**Simulation**_ , to enrich the key concepts of geographic information and thinking. 

A cross-cutting element in Järvinen’s (2008) collection is **Information** , indicated by (I) in Table 1.4. This element pertains to all information about objects, events, agents, and the game system that is needed for the game to work. As such, it roughly corresponds to everything in a Geographic _Information_ System that pertains to a particular (thematic) project, including its actors, available information, and constraints. Information is a key ingredient of the core geographic concepts and could therefore potentially help to further specify and organize Järvinen’s Information element. Together with the suggestions in the previous section, this 

O. Ahlqvist and C. Schlieder 

12 

**Table 1.5** Alignment and differences between core geographic concepts and proposals for key game components (Holopainen 2011) and game elements (Järvinen 2008) 

|Proposed unifed and_extended_core<br>geographic concepts|Game components<br>Holopainen(2011)|Key game elements<br>Järvinen(2008)|
|---|---|---|
|**Location**—formal and informal ways of<br>specifying _where?_||(I)|
|**Distance**—relationships between places/<br>objects by measures of (space-time)<br>proximity||(I)|
|**Neighborhood**—identifes_what is near?_<br>in terms distance||(I)|
|**Field**—continuous phenomena that have a<br>thematic attribute everywhere in space-time|Game elements|Environment (I)|
|**Object**—describe individuals that have an<br>identity as well as spatial, temporal, and<br>thematicproperties|Game elements|Components (I)|
|**Network**—relationships (connections and<br>fows)between objects(nodes)|Game elements|Environment (I)|
|**Granularity/Scale**—amount of detail in<br>spatial information||(I)|
|**Event**—an individual portion of a process,<br>bounded in time|Actions (Events)|Game mechanics (I)|
|**Overlays**—Inferring spatial associations by<br>comparingmapped variables bylocations||(I)|
|**Spatial heterogeneity**—implications of<br>spatial variability||(I)|
|**Spatial dependence**—Understanding<br>relationships across space||(I)|
|**Accuracy**—difference between spatial<br>information and some reference considered<br>‘true’||(I)|
|**Meaning**—how to interpret terms in spatial<br>information||Theme|
|**Value**—the roles played by spatial<br>information in society||Contexts|
|**_New_**—**_Rules_**—Procedures that dictate and<br>governs game play (simulation), permissible<br>actions, etc.|Rules<br>Modes of play Goals<br>and sub-goals<br>(Events)<br>Evaluation functions<br>Closures<br>End conditions|Rule set|
|**_New_**—**_Agents_**—Entities that act toward the<br>goals orjust followingrules in agame.|Game facilitator<br>Players|Players (I) (Components)<br>(Environment)|
|**_New_**—**_Interface_**—the different types and<br>forms of representations by which players<br>have access to agame|Interface|Interface|
|(continued)|||



1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

13 

**Table 1.5** (continued) 

|**Table 1.5**(continued)|||
|---|---|---|
|Proposed unifed and_extended_core<br>geographic concepts|Game components<br>Holopainen(2011)|Key game elements<br>Järvinen(2008)|
|**_New_**—**_Simulation_**—dynamic enactment of<br>interrelated objects, agents, and rules in a<br>geographic system model|Game instance<br>Game session Play<br>session<br>Set-up and set-down<br>Extra game<br>activities Game time|(I)|



points at the potential for an enrichment of game design vocabularies using core geographic concepts. 

The correspondence with the remaining two game elements to GIScience concepts is less clear. One is Järvinen’s central concept of **Game Mechanics** that refers to the means by which players interact with game elements to influence game states in order to complete a goal. The 44 game mechanics that Järvinen (2008) identifies are divided into six categories, largely following the previous seven key elements: Component, Environment, Theme, Interface, Physical, and Player mechanics. The reason for this is that the nature of game mechanics is analogous with verbs such as “Arranging”, “Trading”, and “Moving”, and the other elements mainly relate to the subject matter of the game, e.g. the components, environment and players that are involved in doing something. An example parallel to game mechanics in the context of GIS would be a spatial decision making or planning scenario, where one or more stakeholders seek to achieve some identified goal, e.g. optimal location of a new development, by using GIS information, analysis and modelling. An important difference is the richness of detailed mechanics identified for games because of their focus on player actions and interactions with any and all game components and the environment. We find Game Mechanics to most closely align with Kuhn’s (2012) Event and the proposed ‘new’ concept of simulation. Much like the discussion of spatial activity patterns (Table 1.3) revealed, this is an area where much research remains to be done. 

The second of Järvinen’s (Ibid.) game elements that is difficult to match up with existing GIS concepts is **Contexts** , which refers to the time and place a game is played. This may sound like a repeat of the components and environment of the game, but it relates more broadly to a range of factors and relations to audience, cultures, traditions, public opinions, and motivations surrounding the game play. As such, game context seeks to consider social and psychological aspects of game play, and this seems most closely associated with the GIScience literature on cognitive (Nyerges et al. 1995) and societal (Nyerges et al. 2011) aspects of GIS practice. We find this to be most closely corresponding to Kuhn’s (2012) Value concept, and this is another area of increasing importance where there is a lack of research. 

Overall, Table 1.4 has helped us identifying the intersection of games and play with the geographic dimension. It illustrates that the core geographic concepts of location and analysis of space-time distance, neighborhood, overlap, heterogeneity, and dependence provide a specific and well-established vocabulary for defining 

O. Ahlqvist and C. Schlieder 

14 

Geogames and Geoplay as a particular form of games and play that emphasize spatial relationships and patterns. Additionally, the game research vocabularies we have introduced here provide a rich source to draw from as we seek to develop a vocabulary to further describe Geogames, Geoplay, and geographic simulation activities. As we pointed out before, the notion of Rule Sets, and Players have close correspondence with spatial simulation concepts. 

A significant body of GIScience research have pointed at the importance of interface modalities and it seems likely that this has a particularly important place in defining Geogames and Geoplay. In games it is quite common that the interface defines some of the game mechanics and ultimately the game itself (e.g. tennis, pinball, card games). To a certain degree, much recent development of mobile, location- aware devices have paved the way for many new Geogame ideas. Finally, Holopainen’s (2011) temporal components of Game session, Play Session, Set-up and set-down, and Extra game activities have direct relevance to the idea of a spatial simulation. The benefits of Holopainen’s more specific set of concepts is that we get a vocabulary for talking about a simulation as a closed event with particular sub-components. 

The simulation aspect of Geogames and Geoplay is probably one of its most distinctive features. Järvinen (2008) argues that games should be seen as systems, including the dynamic interaction of objects, agents and events. This forms a foundation for using Geogames as instantiations of real-world systems, abstracted to some thematic focus, and able to provide insights into that system’s behavior under the particular context of the game play. 

We hope that this overview, even if it only constitutes a first effort, provides a more unified vocabulary that cuts across the realms of Geo and Games. As such it may provide a helpful foundation for reading this book and potentially for further research in this exciting area. 

## **1.4  Structure of the Book and Research Questions** 

The purpose of this book is to provide a first overview of this highly interdisciplinary field with contributions from researchers, GIS professionals and game designers. Over the past 5 years we have seen a significant increase in the number of initiatives and efforts to build, disseminate and interrogate geogames and geoplay. There is an emerging research community sharing developments and insights in geogames and geoplay: A number of dedicated workshops have been held at international conferences, and funding agencies are now responsive to the emerging opportunities for discovery and societal impacts offered by this field. Slowly, this pioneering work is also beginning to provide the contours of a more comprehensive research agenda. 

The chapters in this book are fairly representative of ongoing work as it cuts across several application areas, types of geogame and geoplay activities, and vary- 

15 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

ing types of research approaches and traditions. The scope ranges from  fundamentals about games and play, geographic information technologies, game design and culture, to current examples and forward looking analysis. Unlike other publications in this area (e.g. Nijholt 2017), where many of the represented perspectives come from planning, architecture, game studies, computer graphics, the perspectives provided in this book come primarily from the geospatial sciences. It therefore serves as an introduction for both geospatial scientists who seek orientation in the spatial gaming field, as well as for the aforementioned disciplines to gain an understanding of how those working in the spatial sciences may approach spatial games. Throughout the chapters, the authors refer to a number of different games. To facilitate citation and access to information on these games, we have compiled a joint ludography. In addition to games, the ludography also lists platforms and frameworks used for creating games. Games and platforms that have an entry in the ludography are identified by bold face. Classical console games are included even if they do not involve geographic gameplay. Traditional board and card games, however, are omitted. The ludography provides pointers to the chapters and, where possible, references to publications or links to websites. 

In Chap. 2, Ola Ahlqvist, Swaroop Joshi and colleagues identify and describe the defining characteristics of a recently developed Geogame concept, a Geographic Information System-Multiplayer Online Game framework (GIS-MOG). This turns digital world maps, similar to Google and Bing Maps, into a game board where any place in the world can be experienced first-hand through board game-like simulations. The authors seek to define what it is about this technology that makes it a unique genre of geogames and learning technologies in general. Using the core concepts discussed in this introductory chapter, they provide a detailed description of how these concepts are incorporated in their geogame technology giving examples from their own game. 

Chapter 3 by Thomas Bartoschek, Angela Schwering, and colleagues addresses the challenges of designing an educational game, **OriGami** , with the goal of improving the spatial orientation skills of young players in the age group of 8–12 year olds. The game can be played on mobile devices in outdoor environments, however, the chapter concentrates on the desktop mode. Their basic idea consists of letting the players solve route-following tasks based on verbal descriptions that mobilize different cognitive skills. An instruction such as “Turn right” may force the player to realign his or her cognitive map with the cartographic representation shown on the screen. The authors take an approach that is special in that it concentrates on a single skill, route following, and carefully analyses the task requirements. Even those who do not go through the details of the empirical study, will realize that the authors address a fundamental issue for the design of any educational game: Is there anything to learn? It is well-known that there are individual differences in spatial abilities and a game task has to be designed in a way that players can improve, in other words, that expertise matters. 

In Chap. 4 Alenka Poplin and Kavita Vemuri presents an application scenario that is situated in collaborative planning and consensus building, negotiation models, communication in physical vs. digital environment, and Public Participation 

16 

O. Ahlqvist and C. Schlieder 

Geographic Information Systems (PPGIS). The chapter describes their work to develop a digital spatial game that can enable negotiations about planned urban projects in a large low-income area of Mumbai, India. Their prototype, called **YouPlaceIt!** , was implemented as a web browser-based game with some basic GIS functionality and a satellite imagery base map for orientation. Their goal is to study the implementation of online place-based negotiations and consensus building and the chapter reports some early findings from initial testing with experienced planning professionals. A key observation in this example scenario is the importance of local/regional languages, especially in cultures like India where many distinct regional languages exist. Planning scenarios in urban areas can present especially complex negotiation processes where many native languages could be involved in one negotiation topic/process. 

Chapter 5 by Byron Antoniou and Christoph Schlieder describes spatial allocation games as a subclass of location-based games suitable for addressing public participation issues. They study the spatial behavior of contributors to **OpenStreetMap** and links it to gamification mechanisms which provide a solution to issues that arise with patterns of participation. More specifically, three issues are identified: (1) high productive contributors show little commitment to return and update geographic features they created, (2) the gap between the accumulated percentage of created features and the accumulated percentage of updated features is widening, (3) there is a significant contrast between areas of high and low mapping activity. Based on an analysis of the geogames **Geographing** , **Foursquare** , **Ingress** , and **Neocartographer** , six common design patterns for the allocation and deallocation of places are identified. They show how the participation issues map onto the game design patterns, and results from an agent-based spatial simulation provides insights into the interaction of the spatial design pattern. 

Chapter 6 presents a second chapter from the same research group. Christoph Schlieder, Dominik Kremer, and Thomas Heinz identify an important part of the geogame design process, namely game relocation, and provide the methodological and technical means for addressing this part of the process in the classroom. While teachers have used geogames in a variety of learning contexts in secondary education, they generally avoid letting the students themselves design the game because of the alleged complexity of the task. In game relocation, the designer adapts a successful geogame to a new geographic environment. The approach taken by Schlieder and colleagues features three components. First, they show how to decompose the game relocation process into a sequence of spatial analysis tasks accessible to students. Second, they present a method, ‘place storming’, which permits students to search the geographic environment for potential places of game actions. Last, they describe a software tool developed to support students solving the spatial analysis tasks involved in game relocation. 

Chapter 7 by Simon Scheider and Peter Kiefer also focuses on game relocation as a core problem in the field of Geogames. While game designers have intuitions helping them to distinguish better from poorer relocations, no concise general quality criteria have been formulated so far. The chapter provides quantitative criteria 

1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field 

17 

for relocation of a generic game model and illustrates them with examples. Although the approach uses formal notation, the basic idea can be stated informally. There are essentially two ways in which a relocation can fail and quantitative criteria should capture both of them. First, the environmental embedding can prevent actions, which the game mechanics would permit to take place. Physical barriers preventing access to a place is a typical example. The second type of failure occurs when the interpretation of game actions in terms of physical actions in the environment leads to inconsistent game states. If ownership of a place is obtained just by moving to that place, cases of multiple ownership of a place may occur. In other words, relocation ties narratives to their physical implementation and these ties may be more or less supportive to the rules of the game. 

A more critical analysis of the relocation issue is provided by Jim Mathews and Christopher Holden in Chap. 8, where they give an extensive review of existing games that elaborate on the affordances of combining geogaming with place-based education. Their main critique of many geogames to date is that they are often simply “dropped onto” places, without much concern for the local context. Instead they argue for the adoption of place-based education practices in order to design games with an emphasis on learning experiences that are situated within a local community. They also argue for small, locally based development of such games as opposed to large scale game-based curriculum design. 

Chapter 9 by Nathaniel Henry is motivated by the relatively large cost to gather very detailed and naturalistic 3-dimensional data from real environments for use in 3D game engines. Henry introduces a workflow that combines low-cost data collection from unmanned aerial vehicles (UAVs), 3D reconstruction methods, and techniques for importing geographic data into a game engine. This approach offers a citizen-centric, low-cost and time-efficient method for Indie geogame designers to capture real terrain for use in a 3D virtual environment where users can navigate from a first-person perspective and view ground objects as they might appear in real life. 

While Chap. 10 by Michael Demers does not deal with a geogame per-se, it discusses some important elements of games and learning in a highly geospatial setting. First, following the widely used Quality Matters rubric, it argues for the importance of identifying and aligning course objectives with assessment, instructional material, activities, and technology among other things. Second, under the Quest-Based Learning approach, it describes different forms of gamification and some of the typical game mechanics that are used to gamify a learning activity. At the center is a description of his own development and implementation of a GIS course that follows a quest-based format. 

Geographic data and the way they are used in game play characterize geogames. In Chap. 11, the final chapter of the book, Cheng Zhang shows that such data is not necessarily limited (as the prefix geo- suggests) to terrestrial environments. A spatial treasure hunt may take place on the moon if terrain models and other scientific data are available. The basic idea explored by Zhang is quite simple: find a suitable mapping between places on the moon and terrestrial places, which permit to explore lunar caches by walking and searching caches on Earth. 

O. Ahlqvist and C. Schlieder 

18 

We recognize that the realm of geogames and geoplay is located in the intersection of two rapidly evolving fields: gaming and GI technology. Any work in this area runs the risk of quickly becoming outdated, unless the focus is on underlying principles and theories rather than the technology itself. We think that the contributions in this book emphasizes the former and therefore will provide a lasting reference for future work. 

## **References** 

- Björk, S., Lundgren, S., & Holopainen, J. (2003): Game Design Patterns. In: J. Raessens, M. Copier, J.Goldstein, and F. Mäyrä (eds.): DiGRA '03 - Proceedings of the 2003 DiGRA International Conference: Level Up (pp. 180–193). Utrecht, NL. Digital Game Research Association. Retrieved from http://www.digra.org/wpcontent/uploads/digital-library/05163.15303.pdf 

- Björk S, Holopainen J (2004) Patterns in game design (game development series). Charles River Media, Newton Centre, MA. http://www.amazon.ca/exec/obidos/redirect?tag= citeulike09-20&path=ASIN/1584503548 

- Davidsson O, Peitz J, Björk S (2004) Game design patterns for mobile games. Project Report to Nokia Research Center, Finland 

- Gamma E, Helm R, Johnson R, Vlissides J (1995) Design patterns: elements of reusable objectoriented software. Addison-Wesley, Reading, MA 

- Holopainen J (2011) Foundations of gameplay. Doctoral dissertation Series No 2011:02. Blekinge - 

- Institute of Technology, Karlskrona, Sweden. http://www.diva portal.org/smash/record. jsf?pid=diva2:835337 

- Janelle DG, Goodchild MF (2011) Concepts, principles, tools, and challenges in spatially integrated social science. In: The SAGE handbook of GIS and Society. Sage Publications, Thousand Oaks, CA, pp 27–45. https://books-google-com.proxy.lib.ohio-state.edu/books?id=7kuS_P70 YhkC&lpg=PA27&ots=HlarnIqihD&lr&pg=PA27#v=onepa ge&q&f=false 

- Järvinen A (2008) Games without frontiers: theories and methods for game studies and design. Tampere University Press, Tampere, Finland. http://tampub.uta.fi/handle/10024/67820 

- Kuhn W (2012) Core concepts of spatial information for transdisciplinary research. Int J Geogr Inf Sci 26(12):2267–2276. https://doi.org/10.1080/13658816.2012.722637 

- Kuhn W, Ballatore A (2015) Designing a language for spatial computing. In: Bacao F, Santos M, Painho M (eds) AGILE 2015. Springer, Cham, pp 309–326. http://escholarship.org.proxy.lib. ohio-state.edu/uc/item/04q9q6wm 

- Nijholt A (ed) (2017) Towards playful and playable cities. Springer, Singapore. http://link.springer. com.proxy.lib.ohio-state.edu/chapter/10.1007/978-981-10-1962-3_1 

- Nyerges TL, Couclelis H, McMaster RB (eds) (2011) The SAGE handbook of GIS and Society. Sage Publications, Thousand Oaks, CA. https://books-google-com.proxy.lib.ohio-state.edu/ books/about/The_SAGE_Handbook_of_GIS_and_Society.html?id=7kuS_P70 YhkC 

- Nyerges TL, Karwan M, Laurini R, Egenhofer MJ (eds) (1995) Cognitive aspects of humancomputer interaction for geographic information systems, vol 83. Kluwer Academic Publishers, Netherlands. https://books-google-com.proxy.lib.ohio-state.edu/books/about/Cognitive_ Aspects_of_Human_Computer_Inte.html?id=cePdBgA AQBAJ 

- Sintoris C (2015) Extracting game design patterns from game design workshops. Int J Intell Eng Inform 3(2–3):166–185. https://doi.org/10.1504/IJIEI.2015.069878
