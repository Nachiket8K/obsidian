---
title: "Chapter 2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic Information and Thinking"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic Information and Thinking** 

**Ola Ahlqvist, Swaroop Joshi, Rohan Benkar, Kiril Vatev, Rajiv Ramnath, Andrew Heckler, and Neelam Soundarajan** 

## **2.1  Introduction** 

In 2008, the National Science Foundation (NSF) released the report “Fostering Learning in the Networked World: The Cyberlearning Opportunity and Challenge”. NSF argued in this report that the heavy investment and focus on Cyberinfrastructures must be complemented by a parallel investment in Cyberlearning, “…learning that is mediated by networked computing and communications technologies.” (Borgman et al. 2008). The rationale was that information and communication technologies had reached a critical tipping point where high-end computing, cyberinfrastructures and mobile technologies were readily available for billions of users, but it was still unclear what affordances they could bring to learning in structured classroom settings and more informal learning environments. 

As a consequence of the report recommendations, NSF created the Cyberlearning program within the Division of Information and Intelligent Systems (IIS) directorate which began funding a broad collection of projects, ranging from the exploration of new ideas to project implementation and scaling-up of thoroughly tested technologies. A separate Center for Innovative Research in CyberLearning (CIRCL) was also established to support and amplify the funded projects, and the Center website http://circlcenter.org provides plenty of information on the ongoing research. 

A common theme found in these projects is the desire to help leverage new cyber-technologies for learning. Important questions are raised: what are entirely 

O. Ahlqvist ( * ) 

Department of Geography, The Ohio State University, 1049B Derby Hall, 154 N Oval Mall, Columbus, OH 43210, USA e-mail: ahlqvist.1@osu.edu 

> S. Joshi • R. Benkar • K. Vatev • R. Ramnath • A. Heckler • N. Soundarajan Ohio State University, Columbus, OH 43210, USA 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_2 

19 

O. Ahlqvist et al. 

20 

new opportunities that these cyberinfrastructures provide that could support learning? How does learning happen with these technologies? Are there generalizable theories that could support designers of future cyberlearning environments? 

The work we report on in this chapter was funded by the NSF Cyberlearning program as an Exploration (EXP) project entitled “GeoGames—A Virtual Simulation Workbench for Teaching and Learning through a Real-World Spatial Perspective”. The project ran from 2011 to 2016 and is now in its concluding phase. 

## **2.2  The Genesis of Our Geographic Information SystemsMultiplayer Online Games (GIS-MOG) Idea** 

Our venture into the realm of combining online maps with board games came in the spring of 2007 during an independent study between the lead author and an undergraduate geography student who wanted to design a board game map for the popular game Ticket to RideTM by Days of Wonder. The game objective is to connect cities with railroad lines by collecting cards of various types that can be combined to claim segments along prescribed railway routes. While the original board game was played on a game map of the United States, the popularity of the game ensured that versions for other parts of the world was developed, both as official versions released by the publisher Days of Wonder, and also as unofficial maps created by an active user community. 

The independent study assignment was to design a new game map of Canada. As this work progressed, there were repeated conversations around what type of geographic insights board games like Ticket to RideTM and other popular map-based games could provide. Clearly, many board games do make use of some type of map that can provide various types of geographic learning depending on what is emphasized either through the map itself or other game elements and mechanics that take some grounding in geographic reality. 

While games for geographic learning have existed for a long time, Walford (1981) noted in his review of developments from the 1960s to the 1990s that there was a total lack of systematic evaluation of the learning experiences and outcomes of such games. In the years since, there have been some efforts to that end, but much of what is learned from those studies are typically hard to generalize beyond a particular game and its specific educational context. It is worth noting that this issue is not unique among geographic education studies. The CyberLearning program came as a response to similar concerns about education research across many domains, and the program was specifically interested in projects that would be able to create generalizable knowledge about how and why learning happens with cybertechnology (Borgman et al. 2008). Consequently, in addition to better understand the opportunities and obstacles presented by our GIS-MOG framework for role-play games/simulations, we started an iterative design process to develop an example prototype application and explore the affordances of this new technology platform that uses GIS maps as game boards for geographic learning. Central research questions were: what does this new learning technology provide in terms of authentic 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

21 

experiences, student engagement, and higher-order thinking? And how do the specific technology affordances (access to rich geographic information, particular game mechanics, collaboration opportunities, etc) help or hinder learning? Answers to these two questions will be reported elsewhere. In this chapter we will focus on a third question that we were equally interested in: what is our prototype geogame application representative of, as a broader category, or genre, of learning technologies? Describing the game by specifying key components and functionality can help and guide others to develop similar technology, compare across different implementations, and hopefully allow for the generalization of findings across independent studies of specimen applications. 

Before getting to this description, we will first review how our particular technology for a geogame prototype iteratively evolved, each version incorporating key features of the new learning technology. 

## **2.3  The GIS-MOG Technology Framework** 

In our technology development work we followed a design based research pattern (Barab and Squire 2004) by progressing through a series of five major iterations to incrementally build from our original idea to the current proof-of-concept prototype. 

Our first iteration (Fig. 2.1a) was carried out in 2008 to initially explore real-time interactions in an online mapping environment. At that time, no existing online mapping environment provided such functionality so a custom architecture was built using Openlayers (www.openlayers.org), PHP and MySQL. This demonstrated the viability of a light-weight client solution with cross platform compatibility and near instantaneous (<1s) propagation of user actions between clients. In the next iteration (Fig. 2.1b) we used the first release of the Google Earth browser plugin and associated API to support inclusion of distributed and custom geospatial data in a command and conquer game styled after the board game RISK, while maintaining real-time multi-user interaction through the map interface. 

In the third iteration (Fig. 2.1c) we introduced the support for real-time webservices such as the WMS, WFS, and WPS implementation specifications (see http://www.opengeospatial.org/standards), to demonstrate how this could change the conditions of any new game by providing ever changing condition variables e.g. weather, stock markets, house prices. The next iteration (Fig. 2.1d) sought to create a fully playable prototype for user testing by expanding capabilities to interaction between players through a game lobby, chat room, and discussion board. This platform also implemented all capabilities from previous iterations through an integration of two JAVA based client-application frameworks; NASA’s World Wind (http:// worldwind.arc.nasa.gov/) virtual globe environment and Sun’s Massive MultiPlayer Online gaming platform **Darkstar** . Throughout the development the games were play-tested by researchers (iterations a–c), small focus groups (iteration c and d) and entire class sections (iteration d) at the Ohio State University. For more information about these stages in our development see Ahlqvist et al. (2012). 

O. Ahlqvist et al. 

22 

**Fig. 2.1** The first four major iterations of the GIS-MOG platform. ( **a** ) Using Openlayers for realtime multi-user interaction. ( **b** ) Using Google Earth JavaScript API for geodata integration. ( **c** ) Using web-services for live geodata feeds. ( **d** ) Using World Wind and Darkstar for fully playable integration of geodata and real-time multi-player support 

After the completion of the four experimental prototypes a–d, we identified that the combination of web-based GIS and multi-player game mechanics seemed to offer a novel and powerful learning technology with a unique combination of desired affordances. With these insights we embarked on a longer term design experiment, with the goals of both building a fully GIS-based map game environment and doing repeated experiments to study how and why learning can happen with this novel technology. 

Our current prototype game lets students in an introductory Geography course explore the concept of the Green Revolution from the perspective of a farmer in rural Punjab, India. After a signup process, students get to choose a family and start farming on digital plots of land located in one of the many farming villages in that region. The main game interface (Fig. 2.2) presents users with an aerial photo map of a village in Punjab, where plots of land that players can acquire and farm are outlined on top of the aerial image. 

The game is turn-based and each turn represents a single growing season. During a turn, players can interact with the map by clicking on parcels to identify the size and cost of buying that piece of land. Once owned, a parcel is open for various farming options (Fig. 2.2, #1–3): players can plant parcels with land race or high-yield seeds (#1), apply fertilization at low or high levels (#2), and irrigate the fields after first investing in an irrigation system (#3) that will have varying cost depending on 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 23 

**Fig. 2.2** The GIS-MOG game play interface 

how far away from the river a parcel is. The players have to decide on how to manage each owned parcel before a round is ended (Fig. 2.2, #6). After a turn ends, the yield from each parcel is calculated by a set formula that accounts for the chosen farming choices and a random weather index between 1 (good) and 5 (poor). After the yield has been calculated players can buy and sell any surplus yield (at a randomly set market price) using the market tab (Fig. 2.2, #5), or keep it for future seasons. The next round then ensues where players again have to decide on planting, fertilization, irrigation and possibly buying more land. The game ends after a set number of rounds and winners may be determined based on the value of accumulated assets. 

## **2.4  Defining the GIS-MOG Genre** 

As mentioned above, one guiding question in our research has been to identify how to classify the GIS-MOG game as a more general category or genre of games and learning technologies. It is common to find groupings of games into so-called ‘genres’, for example puzzles, role-play, simulation, sports and more, but until recently these sub-divisions were rather arbitrary and typically not helpful for efforts to generalize research findings from one game to others in the same genre. Building on work by genre theorist Rick Altman, Järvinen (2008) notes in a lengthy analysis of game genres that genres are not stable constructs but evolve over time; A genre is comprised of not just systemic (components of the game system itself) but also thematic, contextual, and rhetorical aspects. In our case, we were developing a very particular game technology motivated by new opportunities in two separate technological realms: Geographic Information Systems (GIS) and Massively 

O. Ahlqvist et al. 

24 

Multiplayer Online Games (MMOG). In the first realm, we identified increasingly cyber-enabled GIS as an emerging paradigm for the provision of access to almost unlimited and multi-faceted information about the world, and powerful and scalable geoprocessing capabilities for analysis, modeling, and simulation of real world processes (Wang 2010; Wright and Wang 2011). In the second realm, we found MMOG as a rapidly emerging space where highly immersive, graphically rich videogames were delivered and played online by large numbers of individuals (c.f. Chan and Vorderer 2006). In order to properly situate and characterize our new learning technology that integrate both realms, we will consider the key geographic concepts and game mechanics, elements, and design patterns identified in the introductory chapter (Ahlqvist and Schlieder, Chap. 1). 

The technology configuration we have developed in this project is an integration of state-of-the-art GIS and online multi-player game technologies. It could be thought of as a board game that is played on top of the online, interactive maps that you find on the web, e.g. Google and Bing maps. The fundamental innovation of the GIS-MOG platform is the ability to design games on a modifiable and interactive geographic game board. The platform integrates a full range of GIS-supported map and processing services with online multi-player gaming affordances, combined into an online map game/simulation environment. 

As we saw in the introductory chapter, there has been a growing interest from academics to define the key characteristics of game genres, including LocationBased Games. Some of the existing genre labels, like pervasive games, ubiquitous games, augmented-, alternate-, and mixed-reality games, mobile games, geogames, and adaptronic games, are often tech-centric, meaning that the terminology would have to constantly change with changing technology (Holopainen 2011, p. 30). Our review in Chap. 1 identified some key geographic concepts and game patterns/elements from the literature that are largely technology agnostic, yet represent a best effort at describing fundamental concepts in each domain. We also demonstrated (Ibid.) a strong alignment between many of these key concepts. While these collections of core concepts are nascent, they hold promise for helping to pin down and create structure in what is currently a rapidly expanding number of heterogeneous geogame and geoplay applications and activities. We invite the reader to review Chap. 1 for an overview of the identified geographic concepts, game patterns and game elements. 

Concurrently, and particularly relevant to this chapter, there have been several efforts to categorize learning technologies (Culatta 2011). One direction that learning research has taken is to describe learning technology in terms of Learning Objects, defined by Churchill (2007) as a representation designed to afford uses in different educational contexts, consisting of six object sub-types: **presentation** , **practice** , **simulation** , **conceptual models** , **information** , and **contextual representation** objects. Recognizing the increasing integration of learning technology with traditional learning approaches, Graham (2005) identified four key dimensions of learning technologies— **Space** , **Time** , **Fidelity** and **Humanness** —to describe how certain affordances are enabled through the learning technology. The Space dimension describes to what degree real life is mixed with virtual reality. 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

25 

The Time dimension describes the immediacy of interactions from real-time to asynchronous interactions with longer lag time. The Fidelity dimension describes the sensory richness of a technology, from involving all senses to only one, such as text only. Finally, the Humanness dimension describes the degree to which the learning technology is part of the learning experience, from more or less absent to being entirely mediated through the technology. 

In the following we will present a characterization of our GIS-MOG technology using the extended set of core geographic concepts from the introductory chapter, Table 1.5. The presentation is organized using a framework provided by Ahlqvist (2017) who identified _Representation_ , _Spatial and Temporal Expansion_ , _Location_ , and _Pervasiveness_ as key dimensions of location-based games. This division has many similarities to the learning technology categories above, but it was developed with a focus on location-based games. Section 2.4.1 considers the way that the game represents (most often digitally) real space and time in an abstract, digital information environment. Section 2.4.2 discusses how location in space- time determines the game systems dynamics. Sections 2.4.3 and 2.4.4 considers the way space and time is scaled, expanded, or compressed. Finally, Sect. 2.4.5 considers the degree to which the game allows participants to move between real and represented environments. 

By describing these four dimensions, using the extended set of core geographic concepts from Chap. 1 (identified in bold face below) and examples from our own geogame prototype, we posit that identifying and classifying the key components, functionality, and affordances of the GIS-MOG framework will help others to develop similar technology, make comparisons, and draw inferences between different geogames. 

## _**2.4.1  Representation**_ 

The representation of geographic information is a long-standing issue that has generated significant academic debates over the past half century or so (Fisher and Unwin 2005). Our GIS-MOG framework allows any representation currently supported by ArcGIS (e.g. feature layer, raster, network) to be part of the game interface. This means that we can use most GIS information (maps, networks, remote sensing imagery, etc.) of the real world for game play. For example, we may choose to incorporate data on climate, soils, water resources, demography, economy, weather, traffic, and other geographic themes, as well as satellite and aerial imagery, Digital Elevation Models, and even dynamic data from real-time weather stations, traffic monitors or social media feeds. As such, GIS-MOGs are agnostic to any specific instantiation of the core geographic concepts of **Object** , **Field** , and **Network** . The GIS-MOG framework is capable of implementing several different representational formats such as square grids, hexagonal grids, Triangulated Irregular Networks, as well as Point, Line, and Area vector objects, with support for various import and export formats. 

26 

O. Ahlqvist et al. 

The simulation and gaming aspect of a GIS-MOG scenario requires that represented game space and time are augmented with game items that use the same core concepts above but only exist in the game world and do not correspond to real world features. Examples of these are objects such as player avatars, non-player characters, tokens, field-type attributes that give certain parts of the environment some type of value in the game, or connections (networks) like virtual portals that allow for jumps across space or time (see Sect. 2.4.4 about space/time warping). This combination of real world and game world is essentially a Hybrid Space (Davidsson et al. 2004) game pattern. 

An important concept related to objects that exert some kind of behavior is **Agency** . Players and game facilitators are obvious examples of game agents that makes decisions and triggers game actions, but agency can also be coded into other game objects as well as the game environment representations. As a geographic concept, agency has emerged as a key concept in order to understand world systems as a combination of spatial structure and agency at different scales (c.f. Flint and Shelley 1996; McLaughlin and Dietz 2008). In a GIS-MOG context, agency will be expressed by the players and possible to embed with other game elements through rules and associated simulations (see Sect. 2.4.4 below.) 

In our current GIS-MOG we have used actual remote sensing imagery serviced form the Esri World Imagery map service (Esri 2017b). This real-world foundation is used as a source for augmenting the game world with a “farm land” feature layer consisting of digitized land plots that roughly correspond to real agricultural plot boundaries surrounding the village on the ground, and a “River” network layer that is digitized from the imagery to roughly match up with an existing river that runs by the village. Each of these layers has added attributes that determine some of the game mechanics. 

## _**2.4.2  Location**_ 

The driving idea behind our GIS-MOG framework is that location in the game is important in the same way that location is important in geography. Space-time location and analysis is at the heart of GIS data management and operations, which means that our GIS-MOG framework is inherently maintaining location information for all game environments/elements through one or more of the Field, Object, and Network representations. Location in the generic sense is always a relation between a figure and some chosen ground (Kuhn 2012). In most games that ground is typically an internal reference system, game board, etc., with no direct correspondence in the real world. In a GIS context the ground is typically some chosen geographic reference system that allows for a direct correspondence between represented features in the system and a true location somewhere in the world. As a consequence, any aspect of the space-time location of GIS-MOG elements, such as players, avatars, tokens, other game objects, and the overall game environment, can be 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

27 

informed by additional information form the real world about that location, and which may in turn affect the game dynamics. This dynamism is central to our GISMOG framework. 

Standard spatial analysis functions in GIS can perform various types of **Distance** and **Neighborhood** operations, as well as a wide variety of **Overlay** , **Spatial heterogeneity** , and **Spatial dependence** operations. These analytical procedures can be used to determine a wide range of possible interactions between game objects and the game environment. These core concepts correspond directly with the locality and proximity game patterns identified in the introductory chapter. Our current GIS-MOG implements a few of these analytical concepts to determine the cost of parcels (area and distance to river), cost to install irrigation (distance to river), water availability (more water upstream in the river network), and neighborhood/connectivity (adjacent land can be irrigated by the same installation). Another possibility that has been considered for our current game is varying the land parcel cost and yield depending on soil quality (Overlay). Most of the analytics necessary to determine those rules and dynamics are inherently supported by the GIS back-end of our technology. 

## _**2.4.3  Spatial Expansion**_ 

Spatial **scale** is a central notion in geography with many meanings. Some of the most important notions are scale as a way to define the spatial extent of a study, the operational scale of spatial phenomena, the degree of detail in spatial information, and the cartographic representational fraction that defines the correspondence between measurements on a map with real measurements on the ground. Despite its fundamental role and a relatively well-defined concept, scale remains a surprisingly active area of geographic research and inquiry (Sheppard and McMaster 2004). In the context of serving as a defining characteristic for geogames as a learning technology, it is particularly relevant to consider perceptual and cognitive scales to specify the spatial extent of a geogame. 

Montello (1993) identified figural, vista, environmental, and geographical space as four cognitively distinct scale-ranges that are qualitatively different in how humans treat and understand them. In our GIS-MOG framework the game environment expands play beyond a room, or a soccer field, to larger geographic spaces like villages, cities, countries and continents. Cognitively, this would correspond to the environmental and geographical spaces. These are too large to be visually apprehended without significant movement and integration of information over time. Consequently, these spaces are particularly amenable to be comprehended through maps or aerial imagery with symbolic or otherwise abstracted representations of reality (see Sect. 2.4.1 above). This is accomplished by scaling the real space down, in a traceable way that maintains a real world connection, to a manageable size (e.g. computer screen or table-top board) for the purpose of game play. 

O. Ahlqvist et al. 

28 

With this restriction it makes our GIS-MOG framework distinct from games with motion-control (e.g. Wii and Kinect) that are played in figural space, and games that are played in vista space like **Pac Manhattan** and **OriGami** , where vision, haptics, head and eye movements are primary sensorimotor systems for interaction with and understanding the game. 

In later work, Montello and Raubal (2013) proposed that there are at least six, partially overlapping categories of spatial-cognitive tasks that people perform regularly and in varying cognitive scale-ranges/spaces. Because our GIS-MOG framework is entirely mediated through a screen interface with no need for the user to navigate or experience the real world in order to play, up to four of these tasks are involved; “Using spatially iconic symbolic representations”, “Using spatial language”, “Imagining places and reasoning with mental models”, and “Location allocation”. The remaining two categories, “Wayfinding as part of navigation” and “Acquiring and using spatial knowledge from direct experience”, requires direct physical interaction with the geographic space and is more associated with previously mentioned location-based games that take place in figural and vista spaces. 

## _**2.4.4  Temporal Expansion**_ 

Time can be scaled up or down in order for the game play to span and represent longer or shorter time intervals than the time it takes to play the game. Some games may even take on a less determined temporal scope and continue even when you sleep or go to work. The part of our GIS-MOG framework that probably required most attention, as it was least supported by existing GI-systems, was the temporal dimension of game play. As described in Chap. 1, the game literature has a rich vocabulary around the actual game play and associated events (actions, events, closures, game time, game mechanics, etc.) 

Based on the definition by Clark et al. (2009), geographic **simulations** would be defined as computational models of real or hypothesized geographic situations or phenomena that allow users to explore the implications of manipulating or modifying parameters within the model. In the Geogame context it is also helpful to distinguish between the separate but interconnected concepts of model and simulation. We think of a geographic model as the digital representation of a real-world phenomenon while simulation is the software framework or architecture within which a model is animated. In this we align with the general definition of a simulation as “…dynamic computer models that allow users to explore the implications of manipulating or modifying parameters within them.” (National Research Council 2011 p. 2). Without going into more detail about what separates a game from a simulation, we follow Salen and Zimmerman (2004) “a system is a set of parts that interrelate to form a complex whole” and Järvinen (2008) to view all games as systems. Viewed this way, a Geogame is a model of a geographic system that, when played, enacts a simulation of that geographic system. 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

29 

A key feature of our GIS-MOG framework, and one that we argue is key to define this particular genre of games, is the integration of computational social or environmental models that can simulate how the geographic (game) system will respond to user actions. As an example, our current farming game implements a simple surface water network model to simulate what will happen to water flow downstream when a player (farmer) in the game starts using river water for irrigation. The system can calculate, based on where in the river network an irrigation system is installed, amount of water flow in the river, and amount of water used for irrigation, how much water is left downstream from the irrigation point. By implementing this model using the framework of stand-alone geoprocessing services (Esri 2017a), we seek to generalize the spatial system components so that each subsystem can be modelled separately and simulated as a sub-component of the entire game system. In doing so, we allow for other designers to author and implement other system behaviors by adding or modifying such models. An example could be designing, authoring and publishing a simple economic model that can be consumed by a GIS-MOG to simulate market prices as an effect of the aggregated farm yield in the game and the supply/demand from other parameters in the game. As such, the GeoGame framework is maybe unique among most other gaming systems in that it allows for the outsourcing of game processes to other, third-party and stand-alone services. 

In this context it is worth noting that most geographic models and simulations are typically aiming at a truthful representation of reality. For example, most people would generally expect that a map shows the true location of roads, cities, rivers etc. In games and game simulation we find a more mixed set of priorities and the focus is often more on the entertainment, imaginary aspects, and about the activity itself (Clark et al. 2009). Certainly, many games embed a certain degree of realism as part of the intrinsic features, but not to the degree that geographic simulations aspire to. Similar to space, it is also common that game time is scaled and warped to allow for game play beyond the real time span e.g. to play through 1 year/decade/century in a short game round, or to do particular sequencing, jumps, and loops in space or time to support particular game rules and dynamics. Our green revolution GIS-MOG compresses time so that one growing season becomes one game round, and game rounds are determined either by users triggering the next round manually or by a desired timer, often set to less than 5 min if the game is played in real time. 

An **Event** as a core geographic information concept is defined by Kuhn (2012) as a change to location, neighborhood, field, object and network. It is typically carved out as a discrete and temporally bounded chunk from continuous processes. In a gaming context, we can think of the game session as the process from which we can identify specific game events. Tangible events can happen as a result of user actions (e.g. moving or manipulating a spatial representation) or system procedures (e.g. turn change). The temporal components identified by Holopainen (2011) suggest additional gaming/simulation-specific event semantics related to play sessions, set-up and set-down. Yet, for the purposes of this chapter, it is unclear in what way a game is best characterized in terms of how it handles events. 

O. Ahlqvist et al. 

30 

A simulation is ultimately governed by **Rules** that specify how for example water dynamics are calculated. Earlier we described how irrigation costs and the cost of buying a parcel are determined by distance and area measures. With a game defined as a system of interrelated parts, the rules are at the heart of defining and regulating how game elements can and will interact (Järvinen 2008 p. 30). As such, the setting up of rules in a geographic system design has many similarities with a long tradition of research on expert systems and artificial intelligence (c.f. Robinson and Frank 1987). There are obviously many ways to determine rules for geogames. We could base rules on empirically tested and verified physical and social dynamics, for example by implementing a well-researched surface water model. It is also possible to develop rules by eliciting knowledge form experts, farmers, or other stakeholders (c.f. Barreteau et al. 2007) who may have knowledge about the workings of a particular dynamic that a game rule seeks to model. Ultimately, these rules need to be defined, coded into the game and communicated with players. 

In our current system, many of the rules are _embodied_ (Järvinen 2008) by the game elements themselves, meaning that the way the game and the user **Interface** is designed will determine significant workings of a game. In our game, despite being played using a browser-based online map that in theory can be navigated to any place in the world, the game environment is restricted to one part of a village in rural Punjab because of the parcel layer limits. It is relatively easy to expand the “game board” by adding more parcels, or set up the game in a different place by digitizing a new set of parcel boundaries on top of the map imagery, but that layer very much determines the boundaries of the game in terms of the number of parcels available, their spatial configuration, sizes, etc. The interface itself also sets limits on how a user can access and control the game, notably through points, clicks and text entry in the browser window. 

Because the current GIS-MOG is a proof-of-concept prototype, many rules that are specific to the particular Green Revolution game have been hard coded, whereas other rules are expressed as modifiable parameters (variables) in the game code. For this, the GIS-MOG framework uses Web Rule, an XML-based ASP.NET and MVC business rules engine that is accessed through a game administrator interface as part of the GIS-MOG system (Fig. 2.3). 

Ultimately, to allow for as much flexibility as possible, most rules would benefit from being modifiable through this interface, but this would amount to also accounting for how to resolve some of the rules that are ‘embedded’ in the actual game interface. As an example, if we were to add a new type of goods that could be traded through the market interface (see #5 in Fig. 2.2), there would have to be a way to automatically, or at least in some easy way, edit the visual interface to include a new icon and organize the display in a functioning way. If we were to change the type of crops to grow, the way fertilization and irrigation is done, or add other possible farming actions, this would also have direct impact on the interface design (see #1–3 in Fig. 2.2). Clearly, this type of flexibility is far beyond the scope of our project, but this example helps to illustrate how embedded certain game rules are with the interface design. 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

31 

**Fig. 2.3** The Question Configuration Page in the game administrator interface, showing the criteria in the Rule Editor that triggers particular questions. Those questions are entered through the Question List editor 

## _**2.4.5  Pervasiveness**_ 

Being primarily concerned with location-based games, Ahlqvist 2017) included Pervasiveness as a key dimension to describe the degree to which the game allows participants to become immersed in the simulation, to move between real and represented environments, and to infer meaning and value from the game. **Interfaces** such as mobile technology, wearable computers, head-mounted displays, sensor networks and other pervasive computing technologies can allow a geogame to mix in with the real world such that the boundary between what is part of the game and not is blurred. However, since the real world is infinitely complex, save for manmade artifacts where each component is entirely known, any representation inevitably causes some amount of abstraction and generalization of the real world. As a way to specify the level of abstraction, geographic representations can most typically be further specified in terms of their **Granularity** (e.g. resolution, minimum mapping unit) and various aspects of **Accuracy** (e.g. spatial, temporal) in order to determine the degree of detail that is represented. These specifications are either an inherent feature of the previous representation concepts (e.g. the resolution of a raster data set) or a separate but complementary feature (e.g. Root mean square error estimates of positional accuracy as part of metadata). Semantic accuracy 

O. Ahlqvist et al. 

32 

(Salge 1995) specifications and using ontologies and folksonomies for geographic information can provide a formal specification of a “perceived reality” that can reconcile different perspectives. Rich semantic descriptions are still not a standard part of spatial metadata, yet it provides critical information about **Meaning** as it helps to answer questions about how to interpret the representations. 

It is important to remember that GIS-MOG games make it easy for the designers and players to situate games in places and cultures far removed from themselves. In some ways this is a benefit and even a reason for using this technology. However, it also raises questions around how our own values and practices are promoted and reproduced through the design and game play. As Mathews and Holden (Chap. 8) point out, we need to involve local stakeholders and multiple perspectives in the design of our games in order to better reconcile how local places, societies, and issues are represented and remediated when players engage in game play. 

Ultimately, the degree to which the abstractions and interface manages to mimic how we understand the real world is important for how players will engage with and understand the game environment. Yet, many abstract ‘game worlds’, such as the grids in the classic games of Tic-tac-toe, Chess, and Go, convey enough meaning to generate highly captivating games. This suggests that it is feasible to use more schematic representations in GIS-MOGs and still produce an engaging experience. Examples of this could be a game that uses subway maps or cartograms that maintain some tractable transformation of the real world into the represented game environment. 

## **2.5  Summary and Discussion** 

Through this overview we have sought to provide a rich and multi-faceted description and definition of a new geogame learning technology genre called Geographic Information Systems-Multiplayer Online Games (GIS-MOG). We did so by discussing how GIS-MOG incorporates 18 (Chap. 1, Table 1.4) core concepts related to games, play, and geographic information and thinking. 

Being built on a GIS foundation, the GIS-MOG framework allows for a variety of game world representations, including most existing spatial data formats supporting object, field and network structures (Kuhn 2012). As a consequence, the GISMOG framework is characterized by a flexible and rich array of location-based information and analytic functionality able to support most locality and proximity game patterns (Ahlqvist and Schlieder, Chap. 1). Our GIS-MOG genre is however prescriptive about the spatial game scale as it primarily engages with environmental and geographic cognitive spaces (Montello 1993), and as a result it is primarily concerned with game activities related to the use of spatial language, spatially iconic symbolic representations, imagining and reasoning about places with mental models, and conducting location-allocation activities (Montello and Raubal 2013). In terms of temporal expansion, the GIS-MOG platform implements all temporal components identified by Holopainen (2011), and it implements a rule set that is not necessarily prescriptive but constrained by the user interface which is primarily a 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

33 

device screen with input mechanisms such as a keyboard and pointing device. Another distinguishing feature of our GIS-MOG genre is the possibility to outsource game functionality to geoprocessing services outside the core game software as part of the simulation and rules, offering a way to build flexible and modular simulations. Game world data in a GIS-MOG either have inherent or supplemental metadata that accounts for the accuracy and granularity of game representations. Probably the most difficult dimension to account for is the pervasiveness as it includes aspects of interface, meaning and value. 

Our current farming game is one instance of an infinite number of games that can be implemented on our GIS-MOG platform. We see a big potential with the possibility for game designers to customize a game, for example by moving the location of an existing farm management game to their own neighborhood, modify the factors involved, or changing some rules to create a new and unique simulation experience. In our most current work we have experimented with a first iteration of what we call a “Game Builder” interface that will allow an administrator to move the current game to any location in the world, or travel back in time using historical maps and data to ‘re-live’ an illustrative historical example, with only a few inputs from the administrator. We also see exciting opportunities in studying the game system, including the decisions made by players. Through the game we get a unique window into aspects of geographical decision making that is hard, if not impossible, to gain by just watching real world geographic systems. 

Implementing multi-player gaming support, the GIS-MOG allows for distributed collaboration between anything from two to thousands of users on the simulation platform. What this means is that we offer an environment that has many similarities with **SimCity** , but where we use authentic, real-world geography and capability to make modifications. We are confident that there are other systems, existing or under development, that have very or somewhat similar characteristics as our geogame. Our hope is that a detailed description like the one we provided in this chapter can help users and designers to identify key similarities and differences that can help guide their use and design of geogame technologies, and compare experiences and findings. We recognize that this is a first-of-its-kind effort to do such a structured description of a geogame technology and we look forward to see further development of the set of descriptive criteria as well the informed use of descriptions like these. Nevertheless, we feel confident that we have investigated this technology to the point that can be considered representative of a unique yet broad genre of learning technology. 

## **References** 

> Ahlqvist O, Loffing T, Ramanathan J, Kocher A (2012) Geospatial human-environment simulation through integration of massive multiplayer online games and geographic information systems. Trans GIS 16(3):331–350. https://doi.org/10.1111/j.1467-9671.2012.01340.x 

> Ahlqvist, O. (2017). Location-Based Games. In International Encyclopedia of Geography: People, the Earth, Environment and Technology (pp. 1–4). John Wiley & Sons, Ltd. https://doi. org/10.1002/9781118786352.wbieg0298 

O. Ahlqvist et al. 

34 

- Barab S, Squire K (2004) Introduction: design-based research: putting a stake in the ground. J Learn Sci 13(1):1–14 

- Barreteau O, Le Page C, Perez P (2007) Contribution of simulation and gaming to natural resource management issues: an introduction. Simul Gaming 38(2):185 

- Borgman CL, Abelson H, Dirks L, Johnson R, Koedinger KR, Linn MC, Lynch CA, Oblinger DG, Pea RD, Salen K, Smith MS, Szalay A (2008) Fostering learning in the networked world: The cyberlearning opportunity and challenge. National Science Foundation, Virginia, p 12. www. nsf.gov/pubs/2008/nsf08204/nsf08204.pdf 

- Chan E, Vorderer P (2006) Massively multiplayer online games. In: Vorderer P, Bryant J (eds) Playing video games: motives, responses, and consequences. Lawrence Erlbaum Associates Publishers, Mahwah, NJ, pp 77–88 

- Churchill D (2007) Towards a useful classification of learning objects. Educ Technol Res Dev _55_ (5):479–497. https://doi.org/10.1007/s11423-006-9000-y 

- Clark D, Nelson B, Sengupta P, D’Angelo C (2009) Rethinking science learning through digital games and simulations: genres, examples, and evidence. In: Learning science: computer games, simulations, and education workshop sponsored by the National Academy of Sciences, Washington, DC. http://sites.nationalacademies.org.proxy.lib.ohio-state.edu/cs/groups/dbassesite/documents/webpage/dbasse_080068.pdf 

- Culatta R (2011) Taxonomies of learning technologies. http://innovativelearning.com/instructional_technology/categories.html. Retrieved 29 Jan 2017 

- Davidsson O, Peitz J, Björk S (2004) Game design patterns for mobile games. Project Report to Nokia Research Center, Finland 

- Esri (2017a) What is a geoprocessing service?—Documentation. ArcGIS Enterprise [Software documentation]. http://server.arcgis.com/en/server/latest/publish-services/windows/what-is-ageoprocessing-service-htm. Retrieved 20 Feb 2017 

- Esri (2017b) World imagery. https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a 7f08febac2a9. Retrieved 23 Feb 2017 

- Fisher, P. F., & Unwin, D. J. (Eds.). (2005). Re-presenting GIS. John Wiley & Sons 

- Flint C, Shelley F (1996) Structure, agency, and context: the contributions of geography to worldsystems analysis. Sociol Inq _66_ (4):496–508 

- Graham C (2005) Blended learning systems: definition, current trends, and future directions. In The handbook of blended learning: global perspectives, local designs. Wiley, New York, p 624 

- Holopainen J (2011) Foundations of gameplay. Doctoral dissertation Series No 2011:02. Blekinge Institute of Technology, Karlskrona, Sweden. http://www.diva-portal.org/smash/record. jsf?pid=diva2:835337 

- Järvinen A (2008) Games without frontiers: theories and methods for game studies and design. Tampere University Press, Tampere, Finland. http://tampub.uta.fi/handle/10024/67820 

- Kuhn, W. (2012). Core concepts of spatial information for transdisciplinary research. International Journal of Geographical Information Science, 26(12), 2267–2276. https://doi.org/10.1080/13 658816.2012.722637 

- McLaughlin P, Dietz T (2008) Structure, agency and environment: toward an integrated perspective on vulnerability. Glob Environ Chang 18(1):99–111. https://doi.org/10.1016/j. gloenvcha.2007.05.003 

- Montello DR (1993) Scale and multiple psychologies of space. In: Frank AU, Campari I (eds) Spatial information theory: a theoretical basis for GIS, vol 716. Springer-Verlag, Berlin, pp 312–321 

- Montello DR, Raubal M (2013) Functions and applications of spatial cognition. In: Waller D, Nadel L (eds) Handbook of spatial cognition. American Psychological Association, Washington, DC, pp 249–264. https://doi.org/10.1037/13936-014 

- National Research Council (2011) In: Honey M, Hilton M (eds) Learning science through computer games and simulations. The National Academies Press, Washington, DC. http://www. nap.edu/catalog.php?record_id=13078 

35 

2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic… 

Robinson VB, Frank AU (1987) Expert systems for geographic information systems. Photogramm Eng Remote Sensing _53_ (10):1435–1441 

Salen K, Zimmerman E (2004) Rules of play: game design fundamentals. MIT Press, Cambridge, MA 

Salge F (1995) Semantic accuracy. In: Guptill SC, Morisson JL (eds) Elements of spatial data quality, vol 1. Elsevier Science Ltd., Oxford, pp 139–151 

Sheppard E, McMaster RB (eds) (2004) Scale and geographic inquiry. Wiley, New York. https:// books-google-com.proxy.lib.ohio-state.edu/books/about/Scale_and_Geographic_Inquiry. html?id=vJiRSeXJ-soC 

Walford, R. (1981). Geography games and simulations: learning through experience. Journal of Geography in Higher Education, 5(2), 113–119. https://doi.org/10.1080/03098268108708808 Wang S (2010) A CyberGIS framework for the synthesis of cyberinfrastructure, GIS, and spatial analysis. Ann Assoc Am Geogr 100(3):535–557 

- Wright DJ, Wang S (2011) The emergence of spatial cyberinfrastructure. Proc Natl Acad Sci U S A 108(14):5488–5491. https://doi.org/10.1073/pnas.1103051108
