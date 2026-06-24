---
title: "Chapter 3 OriGami: A Mobile Geogame for Spatial Literacy"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 3 OriGami: A Mobile Geogame for Spatial Literacy** 

**Thomas Bartoschek, Angela Schwering, Rui Li, Stefan Münzer, and Vânia Carlos** 

## **3.1  Introduction** 

Spatial literacy, the skill of learning about and improving interaction with one’s surroundings, is an inherently transdisciplinary competency transcending from STEM to social sciences and arts. Spatial literacy is central in primary and secondary school curricula in many countries, and not only possesses the potentials of individual success but also fosters the importance of spatial information use in society. There is wide agreement on the transdisciplinary power of spatial thinking: Goodchild (2006) pointed out its importance for curricula in all subjects: from STEM[1] , to social sciences and arts. Many tasks in the most recent PISA study (OECD 2014) on general problem-solving refer to spatial problems. The National Research Council (NRC) report “Learning to think spatially” suggests solutions for geographic information systems (GIS) as a support system to think spatially (Committee on Support for Thinking Spatially 2006). Approaches using minimal GIS for all grade levels at school, when particular spatial concepts were used incidentally, follow this direction in several studies (Bartoschek et al. 2010; Battersby et al. 2006; Marsh et al. 2007). Curricula all over the world reflect spatial  competency 

> 1 Short for science, technology, engineering, and mathematics. 

T. Bartoschek ( * ) • A. Schwering Institute for Geoinformatics, University of Muenster, Muenster, Germany e-mail: bartoschek@uni-muenster.de 

R. Li University at Albany-SUNY, Albany, NY, USA 

S. Münzer University of Mannheim, Mannheim, Germany V. Carlos University of Aveiro, Aveiro, Portugal 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_3 

37 

T. Bartoschek et al. 

38 

training, although there are large differences in the way countries implemented this; the spatial tasks, level of abstraction, and learning stage of lessons in spatial literacy differ substantially. 

Technologies such as GPS, tagging technologies, and sensors on smartphones have become widely available at reasonable cost and young people are very eager to use them. Despite their omnipresence, they are still insufficiently integrated into current teaching and learning practices. Spatial literacy is mainly taught in paper and pencil tasks. This is also due to the lack of suitable educational geogames that provide out-of-the box solutions for teachers. Current geogames often lack an educational concept which limits their use in schools. 

Meanwhile, as the ease of access to mobile devices by students increases in many educational settings, the debate around concepts such as Bring Your Own Device—BYOD (Attewell 2015) and Mobile Learning (Clarke and Svanaes 2015; Naismith et al. 2004; Sharples 2006), and their educational potential, gain acuity. Digital games are one of the emerging educational resources which allow students to develop social skills such as teamwork and simultaneously gain experience in the use of digital technologies, in addition to learning about specific content (Prensky 2007). The gamification elements of a given technology should improve enjoyment and engagement for the user (Fudenberg and Levine 1998; Deterding et al. 2011a). 

Baker et al. (2015) report that the knowledge of the educational potential of geotechnologies remains scarce and inconsistent in the field, lacking well-designed, systematic, multidisciplinary and replicable studies despite profuse mentions in the literature regarding the educational potential of geotechnologies. Accordingly, the authors propose a research agenda around four pillars: relations between the geotechnology and spatial thinking; learning geotechnology; curriculum and student learning using geotechnologies; and teacher’s professional development in geotechnologies (Baker et al. 2015). 

This research aims to close this gap and develop a game which is not based on existing GIS. Rather, we adopt an interdisciplinary perspective to support spatial thinking by fostering skills for orientation, wayfinding, and map comprehension. We integrate these skills in a game that adapts concepts of game-based learning to make the learning experience more enjoyable and engaging (Deterding et al. 2011b). Educational geogames—location-based games making use of mobile and geotechnologies that train spatial literacy through spatial tasks—are entertaining and support the development of spatial skills and competences (Schlieder 2014). This is especially true for mobile geogames, which are based on the movement of the player through real environments. These games have an impact on the user’s perception of his or her environment and support the development of spatial competencies (Schwering et al. 2014). 

In this chapter we present our app **OriGami** (Orientation Gaming), which is a game to support users to enhance their map comprehension, orientation, and wayfinding skills. According to developmental stage theories (Newcombe and Huttenlocher 2000; Piaget and Inhelder 1975), and the description of spatial competency development in most curricula (German Association for Geography (DGFG) 2007; Republic of Rwanda MoE 2006), our target user group is children 

3 OriGami: A Mobile Geogame for Spatial Literacy 

39 

ages 8–12, and young adults. The app developed within this project follows the curricular requirements (“spatial orientation”) and practical requirements, since schools do not concentrate on outdoor activities for classes of geography (Hemmer et al. 2007, p. 74) where spatial competencies can be fostered. We tested the underlying concept of **OriGami** in a study, where a map-based route-following task (a variant of the game) was examined with respect to the spatial perspective of verbal route instructions. Moreover, we investigated the relation between game performance and spatial abilities. Based on these findings, we develop a complete concept of the educational game **OriGami** . 

In the remaining sections of the chapter, we give an overview of spatial competencies in school curricula from different countries, from which we develop curricular requirements for geogames and discuss how existing geogames meet these requirements (Sect. 3.2). We introduce our prototypical implementation of **OriGami** and its educational concept (Sect. 3.3) and present an empirical study evaluating **OriGami** as educational geogame (Sect. 3.4). The final part of the chapter outlines the implications from the empirical study for the development of geogames and describes the complete concept of **OriGami** (Sect. 3.5). 

## **3.2  Related Work: Spatial Ability, School Curricula and Geogames** 

## _**3.2.1  Individual Differences in Spatial Abilities**_ 

Spatial abilities relate to a person’s cognitive, perceptual, and informationprocessing capacity that characterizes individual differences in performance involving spatial information (Allen et al. 2004). Researchers such as Linn and Petersen (1985) have suggested three major categories of specific abilities that compose spatial abilities comprehensively. _Spatial visualization_ describes having skill in solving spatial tasks that involve multiple steps using both visual and verbal strategies. _Mental rotation_ refers to skill in imagining how a figure or object would look when rotated in two- or three-dimensional space and _spatial perception_ , which is representing an object’s orientation in the appropriate frame of reference despite competing perspectives or reference frames. In these following paragraphs, we explain how a specific category of spatial abilities is related to the spatial literacy that we address. 

Spatial visualization, defined as the ability to store and manipulate mental visual- spatial representations (see Steck and Mallot (2000) for a review)—plays an important role for learning from external visualizations. Visual-spatial abilities were found to be an important predictor of spatial configurational learning in previous studies if the to-be-learned environment was actively or passively studied from visual media (OECD 2014; Hegarty et al. 2006; Waller 2000). Walking an unknown route through a real, unknown building was related to the ability to encode visual- spatial information as measured with the hidden patterns test 

T. Bartoschek et al. 

40 

(Münzer and Stahl 2011). The route was studied from different visualizations shown on a tablet computer (maps, pictures of decision points, animation of the route through a virtual building) at the entrance of the building. It is thus expected that reading a map for following a route would be associated with spatial abilities, i.e., participants with lower abilities would make more errors in a route-following task. 

**Perspective taking and mental rotation** . Following a route on a map may involve corrections for misalignment if route instructions utilize the egocentric perspective (e.g. “on the next intersection, go left” when the current orientation following the route is to the south). Thus, following a route on a map may require shifts of spatial perspective from the allocentric into the egocentric perspective. Perspective taking is a particular spatial mental transformation that can be measured (Couclelis 1996; Burigat et al. 2006). It might be expected that participants with lower perspective taking ability will make more errors in the route-following task. Alternatively, mental rotation ability might play a critical role. Mental rotation is a mental spatial process that has been described as “analogous” because the mental process seems to resemble an overt rotation of an object in space. The mental rotation process can best be demonstrated with chronometric measurement in which reaction times are related to disparity angles (Shepard and Metzler 1971). It has already been shown that the alignment effect when learning schematic (simple) maps is dependent on mental rotation ability (Schlieder 2014). However, the alignment effect and its relation to spatial abilities have not been studied yet in the context of following a route while reading a naturalistic, ecologically valid map. 

**Encoding** . Individuals may differ in their ability to encode spatial information from a visualization that is shown on a computer screen. A map can be considered a complex visualization. Verbal route instructions require search processes on the map that may focus on particular aspects while ignoring others. A test that measures the ability to encode a spatial figure and recognize this figure in a more complex visual pattern may capture this requirement. 

## _**3.2.2  Spatial Competencies in School Curricula**_ 

Spatial competencies are part of (probably) all school curricula in the world. Table 3.1 reviews curricula in four different countries and lists the spatial competencies and/or tasks that students have to perform at different ages to demonstrate comprehension of basic concepts of cartography and map use. Tasks to train spatial literacy include localization of common places (e.g. home or school) and areas (e.g. neighborhoods or countries) at different scale and orientation in real space. Most tasks concentrate on maps, such as teaching map-making by sketching a map or drawing the route on a map and understanding cartographic principles. While the tasks are similar—typical tasks are to locate different places such as home, school, town, country on a map, navigate to/from school, represent different objects of the surrounding on maps, and tasks reflecting basic cartographic principles such as scale and orientation—the age at which children are supposed to study the spatial 

3 OriGami: A Mobile Geogame for Spatial Literacy 

41 

|Brazil|•<br>Concepts of scale and their<br>importance for spatial<br>analyses in geography<br>•<br>Use of cardinal points,<br>referencing in maps;<br>•<br>Cartographic orientation<br>•<br>Geographical coordinates<br>•<br>Use of maps for Orientation<br>in daily life<br>•<br>Localization and<br>representation in maps<br>•<br>Localization and<br>representation of positions<br>in the class room, at home,<br>in the city<br>•<br>Creating, organizing and<br>reading of map legends<br>|•<br>Concepts of scale and their<br>importance for spatial<br>analyses in geography<br>•<br>Use of cardinal points,<br>referencing in maps;<br>•<br>Cartographic orientation<br>•<br>Geographical coordinates<br>•<br>Use of maps for Orientation<br>in daily life<br>•<br>Localization and<br>representation in maps<br>•<br>Localization and<br>representation of positions<br>in the class room, at home,<br>in the city<br>•<br>Creating, organizing and<br>reading of map legends<br>|•<br>Analysis of thematic maps<br>on city, state and Brazil level<br>•<br>Analysis of different kinds<br>of maps (topographic,<br>touristic, climate,<br>vegetation…)<br>•<br>Sketching simple maps for<br>analyzing information and<br>realizing correlation<br>between facts|
|---|---|---|---|
|Portugal|[Environmental studies]<br>•<br>Identify basic elements of the<br>surroundings<br>•<br>Represent own home<br>•<br>Represent own school<br>•<br>Represent own itineraries<br>•<br>Locate relatively to a reference<br>point<br>•<br>Trace own route on the<br>neighborhood plant|•<br>Locate at the Map of Portugal<br>•<br>Locate on the map the towns in<br>the district<br>•<br>Map the country's capital.<br>•<br>Locate on the map the district<br>capitals|[History and Geography of Portugal]<br>•<br>Identify different forms of<br>representation<br>•<br>Defne map<br>•<br>Interpretate maps<br>•<br>Interpret the concept of scale<br>through observation and<br>comparison of maps with<br>different scales.<br>•<br>Use the directions of the<br>compass for guidance|
|Germany (NRW)|•<br>Explore way to school and school<br>environment<br>•<br>Explore important facilities in<br>hometown<br>•<br>Orientate along points of interest<br>and traffc signs<br>•<br>Draw way to school|•<br>Use maps and other media<br>(compass, sun) for orientation<br>•<br>Explore and describe regional<br>structures (agriculture, rural<br>areas, cities, industry)<br>•<br>Explore and describe changes in<br>geographic space on all scales|•<br>Basic orientation knowledge at<br>different scales<br>•<br>Familiar with basic raster and<br>orientation systems<br>•<br>Determine location in real space<br>with aid of map + other aids for<br>orientation<br>•<br>Move in real space with the aid of<br>maps + other aids for orientation|
|Rwanda|•<br>Locate home + village<br>•<br>Describe main components<br>of way to school.<br>•<br>Draw route from home to<br>school<br>•<br>Locate school<br>•<br>Identify main components<br>of school environment|•<br>Locate sector on map of<br>the province<br>•<br>Draw simple sketch map<br>to show district and its<br>neighboring districts.|•<br>Locate the Province on the<br>map of Rwanda.<br>•<br>Use longitudes and<br>latitudes to locate Rwanda<br>on the map of East Africa<br>•<br>Draw a map highlighting<br>the features identifed.|
||**_1 + 2_**<br>**_Grade_**|**_3 + 4_**<br>**_Grade_**|**_5 + 6_**<br>**_Grade_**|



T. Bartoschek et al. 

42 

concepts differ. The educational standards show growing levels of abstract spatial competences, from understanding children´s daily lives and surroundings, to absolute and relative location, and further to the representation of phenomena. 

## _**3.2.3  Curricular Requirements for Geogames**_ 

After reviewing primary and secondary school curricula and educational guidelines in relation to spatial competencies in various countries, we identified the following curricular requirements with respect to spatial literacy for educational games. 

**Requirements with respect to spatial literacy** . Orientation and map comprehension are the most central competencies mentioned in all reviewed curricula. Thus, educational geogames need to train these competencies. An educational geogame should include the following components with respect to orientation and map comprehension: 

Orientation: 

- Localizing oneself 

- Relating the map to the real world 

- Aligning the map with the real world or mental rotation 

Map comprehension: 

- Understanding cartographic basic principles such as abstraction through categories, symbols/legend, scale, or coordinate systems) 

- Understanding coordinate systems and the concept of map scale 

- Describing spatial characteristics of the environment 

Tasks with different degrees of difficulty can reflect the children’s differential learning stages in different grades. Mobile, digital visualizations allow for adapting the degree of difficulty, for example using the compass heading to auto-rotate maps to facilitate the task of orientation or using GPS coordinates to automatically visualize a player’s location to facilitate localization Another example might be changing the symbols on a map from abstract to example-based photo-realistic 3D objects to facilitate the understanding of map categories. Being able to adapt games to the player’s learning stage has an effect on how spatial tasks are realized, thus it is a requirement from a spatial literacy perspective, and also from a game perspective. 

**Requirements with respect to game based aspects** . A successful educational game motivates students while training on spatial competencies. Digital gamebased- learning can be understood as “a marriage of educational content and computer games” (Prensky 2007). From the digital game-based-learning community, we identified several requirements that educational games have to account for: _Game Elements_ 

- Teamwork—How many players are supported; can their actions be coordinated 

- Competition—Players either compete against each other or build teams to solve a joint task 

43 

3 OriGami: A Mobile Geogame for Spatial Literacy 

- Game Type—Type of game e.g. the goal of the game, temporal properties such as real-time, and spatial properties such as the size of the game area 

- Adaptability/Customization—Adapting the task to different complexity levels is an important aspect in educational games to adjust the game to the individual learning stage of the player 

In schools, spatial competencies are trained with paper maps. Using geospatial technologies allows us to incorporate different didactic concepts: _Technological aspects_ 

- Mobility—Being mobile should be reflected in the overall goal and logic of the game. 

- Real Time/Environment—Real time and real environment games enable pupils to experience and comprehend orientation and map comprehension tasks in more realistic situations than in the class room, thereby increasing student motivation. 

- Positioning—Positioning techniques allow us to localize the user. Games can make use of positioning techniques to support user localization by giving hints or feedback and to develop an interesting game design. 

- Mobile Device Compatible—Mobile devices are a practical pre-requisite for the game being played in real environments, thus the game must be mobile device compatible. In the mobile context, low energy consumption is beneficial. 

## **3.3  Overview and Analysis of Geogames** 

Mobile geogames are based on orientation and movement of players in a geographic environment. This section introduces popular mobile geogames and reviews them with respect to the requirements and their relation to spatial competency training. We first give a general introduction of each game and then summarize their characteristics. 

**Ingress**[2] is a massive multiplayer game based on an augmented reality map, which shows a player’s own position. Players have to choose a faction from two, and control augmented “portals” by physically moving to their virtual position in the real world. While it meets the majority of the gaming requirements (except the access to customization), it lacks some educational concepts of supporting spatial literacy such as systematic tasks to align the map with the real environment and competency of understanding map concepts such as changing scales and map symbols. 

**Actionbound**[3] is an interactive geogame-app for mobile devices based on the classical geocaching principle of using GPS coordinates to find a place or item of interest. It displays the position of the gamers’ devices on the base map (google 

> 2 https://www.ingress.com/. 

> 3 https://en.actionbound.com/. 

T. Bartoschek et al. 

44 

maps) using GPS and motivates users to playfully discover the environment by accomplishing tasks related to history, politics, and culture by taking pictures. Regarding critical aspects of supporting spatial literacy, some major aspects such as adapting the degree of difficulty in aligning maps with real environment, understanding map concepts such as map symbols are missing. 

**MapAttack**[4] is an open-source multi-player geofencing game. Geofencing games create virtual barriers or ‘fences’ for players to keep within or outside of. The game’s goal is to rapidly collect virtual points on a map comparable to the old arcade game Pac-Man. This game has its merits of training teamwork and spatial strategic relating to how to finish the game quickly. However, it does not adequately support spatial competency in map comprehension and adaptation to individual learning stages regarding orientation and map reading. 

**GeoTicTacToe**[5] (Schlieder et al. 2006) allows two players or teams of players to compete. Each player tries to outperform the opponent in a mapping contest by being the first to contribute a piece of information about a geographic location. As a game specially designed for map reading, finding the geographic location under time-pressure increases competition and trains fast map reading. It addressed majority of aspects in training spatial competency while missing only map orientation and map scale in the game. 

**City Poker**[5] (Schlieder 2005) is a real-time game with the aim to get the best cards in a round. Cards are hidden as geocaches in a game area, displayed on mobile devices. A player’s position is acquired through the device’s GPS receiver and thus orientation in the real environment is facilitated. The players search for the caches to change cards at hand. Hints and multiple choice quizzes allow a better location precision of caches. Each team knows which cards the other team possesses as well as which cards are hidden which motivates teams to compete. While acknowledging its merits in gaming design and motivational aspects through competition, we did not find strong support in spatial literacy training such as map orientation and map comprehension. 

**Neocartographer**[5] is a geogame project for high school students with a main objective to understand the spatial decision of gamers (Feulner and Kremer 2014). It combines learning content and real presentation on game board. Teams conquer areas by occupying and solving spatial tasks to extend their background knowledge about a geographic location. The game board is based on a street map with an overlay of virtual areas, showing also the occupied areas of the opponents. This game supports spatial literacy in some ways. For example, a good strategy and map reading as well as communication are necessary to win the game. Some aspects such as map orientation and map comprehension are not reflected in this game. 

**Feeding Yoshi** (Bell et al. 2006) lets players collect fruits (i.e. virtual points) to feed to the character Yoshi. Fruits are displayed on a map, and are representations of nearby wireless networks. Regarding the inclusion of gaming concepts, one consid- 

> 4 mapattack.org. 

> 5 http://www.geogames-team.org/. 

45 

3 OriGami: A Mobile Geogame for Spatial Literacy 

eration is that in obtaining food for Yoshi, players will not walk their usual daily route. Additionally, since there is no competition designed in this game, players may get bored after a while. However, it does support spatial literacy through individual training of orientation competency and map comprehension. 

Table 3.2, lists the specific review of each games corresponding the requirements of spatial literacy and gaming design. 

In general, most games will meet the requirements in the gaming aspects but lack systematic consideration of aspects that support spatial literacy. For instance, most games are based on the collection of points and other scoring mechanisms. They are instantly playable, allow for multiple players or teams and are being played in real time. The games’ purposes range between data collection, leisure and education. Maps are the core elements in all games, mostly street maps at a city/neighborhood level. Regarding supporting orientation competency, most games, except Feeding Yoshi, have enabled a localizing module so that players are aware of their current location. Players can relate themselves to other objects on the map such as streets, crossings, buildings to establish spatial orientation. All games, however, do not consider training explicitly a player’s map orientation competency and map comprehension. Map orientation trains a player to utilize mental rotation to align a map in games with the current environment while completing a game. Map comprehension includes skills of understanding map elements such as scale and symbols. However, in most cases, maps are just used as a platform for games instead of as an educational concept. Consequently, we do not find that typical spatial competencies taught in schools are well-supported by these existing games. 

## **3.4  Educational Concepts for Training and Measuring Spatial Literacy** 

## _**3.4.1  The OriGami Prototype**_ 

To study the educational concept of map reading, we implemented a prototype of the **OriGami** game. We implemented different navigation tasks where people follow a route on a map guided by verbal instructions. The task is intended to foster orientation competence with maps. The implementation is based on the ESRI Java Script API and IONIC Framework mobile app development. The game is implemented as an app for browsers or tablets. Depending on the platform it can be used in mobile condition with GPS or in stationary condition. It consists of a simple base map and displayed route instructions of varying complexity, for example using egocentric directions, cardinal directions, landmarks and distances. The instructions can be provided and edited by the teacher or the game leader in an online editor. 

Feedback, hints and game elements allow the user to orientate and find reference points in the map and in the real world. A blue circle in the map indicates the current 

46 

T. Bartoschek et al. 

|Neocartographer|_Spatial Literacy Aspects: Orientation and Map Comprehension_|X|X|–|Street map|–|Game area|–|_Game-based Aspects (Game Elements and Technological Aspects)_|Multi-player|X|–|speed, time, points|Learn environment|Ca. 45 min|Real-time|Variable,<br>city-level|ArcGIS Online|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Feeding<br>Yoshi||X|X|–|Street<br>map|–|Fruits|–||Multi-<br>player|Chat|–|Points||Unlimited|Real-time|City-level|–|–|
|CityPoker||X|X|–|Street map|–|Five regions|–||2 players/<br>teams|–|–|Speed/Best<br>cards|Speed/strategy|Variable|Real-time|Variable (city<br>level)|Game editor|–|
|GeoTicTacToe||X|X|–|Street map|–|9 boxes|–||2 players|–|–|Speed, time|Strategy|Short|Real-time|Variable|–|–|
|MapAttack||X|X|–|Street map|X|Points to be<br>collected|X||Multiplayer|Yes|Score<br>system|Speed,<br>points|Speed|short|Real-time|Variable,<br>street level|Create<br>game board|–|
|Actionbound||X|X|–|Satellite, Street<br>map, topographic|X|–|–||Both|X|Score system|–|Learn environment|Variable|Real-time|Variable, city level|Create own bounds|–|
|Ingress||X|X|–|Streets visualized<br>as lines|–|Portals, links|X||Multi-player|X|Score system|Speed, points|strategy|Unlimited/ongoing|Real-time|global|–|X (portals)|
|||Localizing yourself|Orientation aids|Mental rotation/alignment|Type of map /cartographic<br>elements|Alternative map type|Virtual elements/augmentation|Auto rotation||Single/multiplayer|Coordination of actions|Classical video game elements|Competition (speed/points)|Main focus|Game time/duration|Real time or turn based|Size of game area|Adaptability/customization|Change/add elements by player|



3 OriGami: A Mobile Geogame for Spatial Literacy 

47 

position located by the device or selected by the user by clicking on the map. A smiley face provides feedback on the current walking direction: It changes color and friendliness (smile or scowl) to give intuitive hints about whether the player is moving or clicking in the direction of the next waypoint. Each time the player reaches a waypoint (in the browser version there is a tolerance distance for clicking, depending on the zoom level), the app signals this by playing a sound and visually via a happy smiley and a text message. The next wayfinding instructions are automatically displayed at the bottom of the screen. A trumpet sound and a text at the end of a route give users feedback, that they have reached the goal. The interface design is kept extremely simple, choosing the map as the main element covering the screen (Fig. 3.1). 

**OriGami** is a game but at the same time a measurement tool to evaluate the spatial literacy and learning progress of a player. The app has several possibilities to record the user interactions for analysis in terms of usability or learning. The tablet version records the GPS-Track, the touch coordinates and gestures, the zoom level of the map and the time required for each route. For optional thinking-aloud tests it can also record sound and allow further usability analysis. The browser version records the time from loading the route to successfully finishing it by reaching the goal, each click coordinate, the distance to the actual waypoint and the zoom level of the map at each click. These designs allow the use of the app and its recorded data as a variable in tests on spatial learning. 

**Fig. 3.1** Screenshot of the **OriGami** App in the browser version 

T. Bartoschek et al. 

48 

## _**3.4.2  Evaluating the Educational Concept behind OriGami**_ 

The goal of the **OriGami** game is to train spatial competencies. For this study we selected different aided navigation tasks and tested the performance of students in different conditions of map-based route-following tasks with the browser-based **OriGami** prototype in a lab environment. As explained below, we assume that spatial abilities have an effect on the performance and the effect depends on the frame of reference used for the route instructions. 

Our target user group is children at the age of 8–12 as well as young adults in accordance to the developmental stage theories (Newcombe and Huttenlocher 2000; Piaget and Inhelder 1975) and the description of spatial competency development in most curricula (German Association for Geography (DGFG) 2007; Republic of Rwanda MoE 2006). The app follows the aforementioned curricular requirements of teaching spatial literacy and game-based requirements, and since schools usually use indoor activities for geography lessons (Hemmer et al. 2007, p. 74) we provide the browser-based version. 

Before conducting a long-term study on training effects, we evaluate (1) whether different conditions of the game reasonably impose different levels of difficulty, (2) whether individual differences of spatial ability are related to initial performance, and (3) whether different levels of map reading expertise affect performance. The present study pursues these goals. Studies like these help us to explain different performances and interpret learning progress of individuals for different ways to communicate about space with different reference frames (allocentric, egocentric, landmark-based). Examples of these three types of instructions are shown in Table 3.3. They also help to understand which user groups **OriGami** should address. This study does not measure the effect **OriGami** has on spatial literacy. A study measuring the learning progress while playing **OriGami** would require a long-term study and a procedure to measure spatial competencies, which is still future work. 

## _**3.4.3  Spatial Perspective in Route Following on a Map**_ 

The level of difficulty of the game varies with the spatial perspective of the verbal route instructions, because the perspective might require particular cognitive processes. The present study investigated performance in the map-based learning game in different route instruction conditions. Participants were asked to follow a route by clicking waypoints that were verbally described. Route instruction conditions differed mainly with respect to the spatial perspective of route instructions adopted for the game (allocentric route instructions, egocentric route instructions, and landmarkbased route instructions). Route instructions using the allocentric perspective directed players to an object location based upon the position of other players. In this type of route instruction, the cardinal directions e.g. south, north were used but a person’s location was not used. Route instructions given using the egocentric 

3 OriGami: A Mobile Geogame for Spatial Literacy 

49 

**Table 3.3** Examples (translated from German) for an initial instruction at the start point and for an instruction at a waypoint in all three conditions (landmark, egocentric, allocentric) 

||Landmark|Egocentric|Allocentric|
|---|---|---|---|
|**Initial instruction**<br>**for orientation**|On your right you see<br>the Sacred Heart Church.<br>On your left you see the<br>Old Postman Pub. Go to<br>the nextjunction.|You are looking in the<br>direction of “Cologne<br>Street”. Go straight<br>until you reach the<br>nextjunction.|Go south until<br>you reach the<br>next junction.|
|**Instruction at a**<br>**waypoint**|Turn and go to the Art<br>house.|Turn right and walk<br>along the street until<br>you reach the second<br>junction|Turn north and<br>walk until you<br>reach the<br>secondjunction.|



perspective directed players to the destination object with respect to its relative direction to a person’s standing position. The route utilized relative direction such as left or right in this type of instruction. In the land-mark-based route instructions, all instructions were created through the interrelation between landmarks. Terms such as “toward” were used to indicate the direction. 

Since maps are typically studied with the particular north-on-top orientation, judgments of relative directions from memory are more difficult if they require reorientation, e.g., imagining another position and orientation than the orientation from which the representation has been studied. Mental representations of spatial configurations are thus thought to be orientation dependent (Schwering et al. 2014; Baudisch and Rosenholtz 2003; Flügel 2014; Bitgood 1991; Robinson 1928). The orientation specificity effect is also termed alignment effect. Alignment effects are considered robust (Schwering et al. 2014; Feulner and Kremer 2014). They occur both with large and small layouts (Flügel 2014). The effect can be experienced in everyday spatial activities such as navigation. For instance, misaligned you-arehere maps impede orientation in a real environment (Deterding et al. 2011b; Li et al. 2014; Gunzelmann and Anderson 2006). This suggests that alignment plays a role in map reading when planning a route and not only for retrieval from memory. In the present study, naturalistic maps were utilized in different route instruction conditions. It was expected that an instruction that describes the route from an egocentric point of view would cause alignment problems when participants try to follow the route. 

## **3.5  Empirical Study on the Educational Concept** 

The goal of the game is fostering map reading competences. A precondition of this goal is to establish a difference in performance between experts and non-experts in map reading when they play the game initially. Experts are those who are familiar with geospatial concepts such as location, distance, or direction and who have received training in map reading, map projection, or coordinate systems in 

50 

T. Bartoschek et al. 

curriculum, while non-experts are those who have not received those trainings in their curricula. This difference would show that the game reflect differences in expertise with its tasks. Therefore, the present study compares two groups of participants. The expert group comprises participants who study geoinformatics, computer science, and landscape ecology. These participants are expected to have more experience with spatial processing, more prior knowledge about maps and higher map reading skills than participants in the non-expert group. The non-expert group comprises participants who study education and teaching, mathematics, psychology, or history. It is expected that the experts group will outperform the non-experts group in the route following tasks of the game, particularly in the most difficult condition. 

Additionally, map reading to follow the route requires search processes and corrections for alignment, particularly in the egocentric route condition. These processes may depend on spatial abilities and on acquired competencies. The ego-centric route condition was therefore expected to be more difficult because mental processes of perspective taking were inevitable. 

## _**3.5.1  Methodology**_ 

**Participants** . Forty-eight participants took part in the experiment, 26 of whom were female (n = 48). They were students at the university of Münster or at the University of Mannheim, Germany, and studied education and teaching (n = 20), geoinformatics (n = 15), psychology (n = 6), landscape ecology (n = 6), computer science (n = 2), history (n = 1) and mathematics (n = 1). The average age was M = 24.3 (SD = 4.9). Participants received course credit or remuneration for participation. 

**Materials** . Following our introduction of spatial abilities, we utilize the following psychometric tests that correspond to specific aspects of participant’s spatial abilities: the hidden patterns test for spatial visualization; the perspective taking tests for spatial perception, and mental rotation test for mental rotation ability. 

The hidden patterns test (Guay 1976) measures encoding and recognizing a simple figure which is embedded in a more complex line drawing (Fig. 3.2). Twohundred items were shown on four pages. Participants answered by marking answer boxes below the items. The overall processing time was restricted to 3 min. In the scoring procedure, the number of incorrectly marked answers was subtracted from 

**Fig. 3.2** Sample item of the hidden patterns test 

51 

3 OriGami: A Mobile Geogame for Spatial Literacy 

**Fig. 3.3** _Left_ : Perspective taking test map: The answer is marked on the _circle_ . _Right_ : Example symbols presented on Chronometric mental rotation test 

the number of correctly marked ones. A reliability of 0.91 is reported for this test (Guay 1976, p. 11). 

In the perspective taking test (Couclelis 1996; Burigat et al. 2006), participants are asked to make directional judgments based on a map which shows a spatial configuration of seven objects (Fig. 3.3). Participants imagine themselves standing at a particular position (e.g., at the traffic light), facing a particular second location (e.g., the stop sign), and pointing to another location (e.g., the flower). The directional judgment is indicated by a position to be marked on the answer circle. The map is visible during answering. The test requires estimating directions from  imagined positions with orientations that deviate from the “upright/north” orientation of the map typically more than 90°. Participants process 12 items, all utilizing the same map. The score of the participant is the average angular error calculated from the items that the participant attempted to solve within the given time of 5 min. Reliability estimates between 0.79 and 0.85 (Cronbach’s alpha statistic) are reported for this test (Couclelis 1996). 

A computer-based test on mental rotation ability including reaction time measures was created after a description provided by Gustafson et al. (2008), using PMA symbols (Krukar and Conroy Dalton 2013). For each item, an original symbol and a comparison symbol was shown on the screen (Fig. 3.3). The comparison symbol was rotated with an angular disparity of 0°, 45°, 90°, and 180°. The comparison symbol either was identical to the symbol on the left, or it was mirrored. Participants were asked to determine as quickly as possible whether the two symbols were identical or not. The test included 60 items. Reaction times as well as accuracy (number of wrong answers) were measured. Jansen-Osmann and Heil (2007) estimated reliability with the Odd-Even method and reported r = 0.91 for the reliability of this test. 

**Materials: Route Instructions** _._ We selected three routes in three different urban locations in Germany for the route-following task using the **OriGami** prototype described above. The three routes are comparable in complexity: ten instructions had to be executed to reach the goal. The routes contain eight turns at waypoints and 

52 

T. Bartoschek et al. 

in-between waypoints. For each route we created landmark-based, egocentric and allocentric route instructions (Table 3.3). 

The landmark-based route instructions used solely landmarks to give directions. All landmarks were visible on the highest and second-highest zoom level. They were represented either via a symbol, a label, the footprint of the landmark, or a combination. Egocentric instructions used only egocentric turn directions. Only for the initial orientation at the start point a landmark was used. The allocentric instructions used only allocentric turn directions. All three route instructions used the terms junction, round-about, and footpath to refer to special features of the street network on the map. 

**Procedure** . Participants were administered the spatial ability tests first (hidden patterns test, perspective taking test, mental rotation test). Subsequently, participants completed three route-following tasks corresponding to the three instruction conditions in the browser-based version of **OriGami** . All participants completed the route-following tasks in all of the three instruction conditions (allocentric, egocentric, and landmark-based route instruction condition). The order of the route instruction conditions was balanced across participants. The three different route instruction conditions were specific to three different actual routes based on three different city maps such that each participant received the three route instructions with three different routes. Each actual route was equally presented with a particular route instruction. As introduced in the description of the prototype, each participant would follow the instruction on the screen (allocentric, egocentric, or landmark- based depending on the condition) to click the waypoint on the screen. Each time the player reaches a waypoint (in the browser version there is a tolerance distance for clicking, depending on the zoom level), the app signals this by playing a sound and visually via a smiley and a text message to indicate its accuracy. The next wayfinding instructions are automatically displayed at the bottom of the screen. A trumpet sound and a text at the end of a route gives the user feedback, that a participant has reached the goal. Participants were tested in small groups of 2–5 participants in a multimedia laboratory with separate work spaces. The experiment lasted about 40 min. 

## _**3.5.2  Results and Discussion**_ 

Due to a technical error, the data of four participants were lost for the mental rotation test and the measurement of the landmark-based route instruction condition. These four cases were removed from the data set. 

The data set was screened for outliers which were defined as values above 2.5 standard deviations from the mean ( _M_ and _SD_ calculated with original data). In the perspective taking test, the average angular error of one participant exceeded 2.5 _SD_ . In the mental rotation test, reaction times to correctly solved rotatable items exceeded 2.5 _SD_ in two cases. These three values were replaced by the respective means. Furthermore, numbers of errors (false clicks, i.e. clicks not on the next way- 

53 

3 OriGami: A Mobile Geogame for Spatial Literacy 

point on the map) were inspected in the allocentric, in the egocentric and in the landmark condition. Extremely high numbers of errors were found in two cases in the allocentric condition, in three cases in the egocentric condition, and in one case in the landmark condition. Errors represent clicks on the map that are placed outside a predefined area around the correct intersection or location. A closer inspection revealed that these participants obviously clicked on the complete route (i.e., they simulated walking along the streets by clicking “along” the streets). Moreover, this behavior could only be observed if the respective route instruction condition was the first of the three conditions accomplished by the participant. Thus, the incorrect clicks were attributed to a misunderstanding of the experimental instruction rather than to a particular difficulty. Therefore, the respective values were replaced by the mean of the respective variable. If a participant made an extremely high number of errors, then the time needed to complete the condition increased accordingly. Therefore, corresponding times were corrected (replaced by the mean of the respective variable) for the six cases in which the number of errors had been replaced. 

Based on their main subject of study at university, participants were assigned to either an expert group or a non-expert group. The expert group comprised participants whose majors were geoinformatics, computer science, and landscape ecology ( _n_ = 20, four participants in this group were female). These participants were those who have taken geospatial curricula in the institute of geoinformatics in which basic spatial concept and map concepts were addressed. Because of their curricular trainings, participants in this group were expected to have more experience with spatial processing, more prior knowledge about maps and higher map reading skills than participants in the non-expert group. The non-expert group comprised participants whose major were education and teaching, mathematics, psychology, or history ( _n_ = 24, 18 participants in this group were female). They were recruited through an introductory psychology classes and have not had geospatial trainings in their curricula. 

Table 3.4 shows descriptive data for the spatial abilities tests, the number of errors (false clicks) in each condition, and the time (seconds) needed to complete each condition, separated for the expert and the non-expert group. Experts outperformed non-experts in the perspective taking test, _t_ (42) = −3.088, _p_ < 0.01, as well as in the hidden patterns test, _t_ (42) = 3.910, _p_ < 0.001. However, mental rotation ability (as indicated by the time needed to assess rotatable items in the chronometric mental rotation test) did not differ between groups, _t_ (42) < 1, _ns._ 

Table 3.5 shows the correlations between the measured variables. Intercorrelations between the spatial abilities tests were in the medium range ( _r_ = 0.38 and _r_ = 0.45). Mental rotation ability predicted the numbers of false clicks in the allocentric and in the egocentric condition significantly. Moreover, mental rotation predicted the time to complete the allocentric condition specifically. The hidden patterns test only predicted the time to complete the allocentric condition. The perspective taking test did not correlate significantly with any of the route performance measures. Within a route condition, correlations between the numbers of errors and the time to complete the route were substantial ( _r_ = 0.61 in the allocentric condition, _r_ = 0.77 in the egocentric condition, _r_ = 0.55 in the landmark condition), suggesting that more 

54 

T. Bartoschek et al. 

errors caused longer completion times. Between route conditions, numbers of errors in the allocentric and in the egocentric conditions were related ( _r_ = 0.45), but errors in the landmark condition were unrelated to the other two conditions. Times to complete the route conditions were not interrelated. 

In order to analyze effects of route condition and group, two repeated-measures analyses of covariance were performed, separately for errors and times. In these analyses, route condition was included as the within-subject factor with three levels, and group was included as the between-subject factor with two levels. In addition, mental rotation (time) and hidden patterns (test score) were included as co-variates. Both covariates were centered. (Perspective taking ability was not included as a covariate, because the correlations had shown that perspective taking did not predict performances in the route tasks). 

In the analyses of the errors, a Mauchly test indicated violation of sphericity (Mauchly-W = 0.80, _p_ < 0.05). Therefore, the Greenhouse-Geisser correction was applied. The analysis revealed a main effect of route condition, _F_ (1.66,66.44) = 3.377, _p_ < 0.05, partial eta squared = 0.08. More errors were made in the egocentric route condition (adjusted mean 16.04, _SE_ = 2.47) than in the allocentric route condition (adjusted mean 9.84, _SE_ = 1.44), _p_ < 0.05. Errors in the landmark condition were similar to the allocentric condition descriptively (adjusted mean 10.97, _SE_ = 1.4), but did not differ significantly from the other two route conditions. 

Furthermore, a main effect of expert group was found, _F_ (1,40) = 6.798, _p_ < 0.05, partial eta squared = 0.15. Adjusted means suggest that non-experts (16.42 errors, _SE_ = 1.9) made about twice as much errors as experts did (8.14 errors, _SE_ = 2.13). The main effect was qualified by a marginally significant interaction of route condition and expert group, _F_ (1.66,66.44) = 3.115, _p_ = 0.06, partial eta squared = 0.08. Descriptive data (Table 3.4) and a marginally significant post-hoc t-test suggested that the difference between experts and non-experts might be have been most substantial in the egocentric route condition, _t_ (42) = −2.002, _p_ = 0.052, whereas differences between groups were not significant in the allocentric and in the landmark condition. 

**Table 3.4** Descriptive data for spatial abilities and performance in the route following game in the expert and in the non-expert group (errors are the number of false clicks, times are provided in seconds) 

|seconds)|||
|---|---|---|
||Experts (_n_= 20)<br>_M_ (_SD_)|Non-experts (_n_= 24)<br>_M_ (_SD_)|
|Perspective taking (average angular error)|17.09(9.29)|32.82(21.11)|
|Hiddenpatterns(test score)|245.70(37.75)|195.46(45.97)|
|Chronometric mental rotation(time in ms)|2747.39(961.57)|2622.92(711.42)|
|Errors in allocentric route condition|7.35(6.51)|12.42(11.91)|
|Errors in egocentric route condition|10.95(12.86)|21.67(20.84)|
|Errors in landmark route condition|8.75(8.94)|13.00(9.47)|
|Time to complete allocentric route condition|217.80(114.33)|231.33(104.79)|
|Time to complete egocentric route condition|221.40(100.84)|286.58(166.11)|
|Time to complete landmark route condition|316.50(117.54)|293.33(108.14)|



55 

3 OriGami: A Mobile Geogame for Spatial Literacy 

The analysis also revealed a main effect of mental rotation ability _F_ (1,40) = 7.637, _p_ < 0.01, partial eta squared = 0.16, and a significant interaction of route condition and mental rotation ability, _F_ (1.66,66.44) = 5.390, _p_ < 0.05, partial eta squared = 0.12. This means that the relation between mental rotation ability and errors was not the same in each route conditions. Correlations (Table 3.5) show that mental rotation predicted errors in the allocentric route condition and in the ego-centric route condition, but not in the landmark route condition. 

Results for times to complete the route following task showed a main effect of route condition on times, _F_ (2,80) = 5.844, _p_ < 0.01, partial eta squared = 0.13. However, the pattern differed from that found for errors. Participants seemed to need more time in the landmark condition specifically (adjusted mean 306.45 s, _SE_ = 16.83), compared to the allocentric condition (adjusted mean 226.28, _SE_ = 14.87) and to the egocentric condition (adjusted mean 252.49 s, _SE_ = 21.06). However, only the allocentric condition differed significantly from the landmark condition, _p_ < 0.01, whereas the egocentric condition did not differ from the other two conditions. 

A main effect of expert group was not obtained (adjusted means for experts 259.27 s, _SE_ = 19.63, for non-experts 264.27 s, _SE_ = 17.53), however, there was a significant interaction between route condition and expert group, _F_ (2,80) = 3.757, _p_ < 0.05, partial eta squared = 0.09. Whereas single comparisons between the expert and the non-expert groups did not show significant differences in any of the route conditions, descriptive data seem to suggest that experts needed more time to complete the landmark condition than the non-experts. The reverse was true for the allocentric and the egocentric conditions. The significant interaction might correspond to this inconsistent pattern. 

Spatial abilities (hidden patterns test score, mental rotation times) did not affect times to complete the route following tasks. Neither main effects nor interactions with route conditions were found. 

In summary, route condition, expertise (group) and mental rotation ability affected errors (false clicks). The effect size of route condition was in the medium range, whereas effect sizes of expertise and mental rotation ability were large. Corresponding to errors, times were affected by route condition. However, times were neither affected by expert group or nor by spatial abilities. Results suggest that the landmark route condition differed in requirements remarkably from the allocentric and the egocentric route condition. First, numbers of errors suggested that the egocentric condition was the most difficult condition. However, participants needed most time in the landmark condition. (Furthermore, experts seemed to need even more time than non-experts to complete this particular condition, in contrast to the other two conditions.) Second, the pattern of correlations (Table 3.5)—corresponding to the interaction between mental rotation ability and route condition—shows that mental rotation ability did not play a role for the number of errors made in the landmark condition. It is therefore possible that cognitive processing requirements were quite specific in the landmark condition. 

56 

T. Bartoschek et al. 

|**Table 3.5**Correlations between spatial abilities tests and performance measures in the route following game in three conditions (allocentric, egocentric, and<br>landmark condition)|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|Perspective<br>taking<br>Hidden<br>patterns<br>Mental<br>rotation<br>Errors<br>allocentric<br>Errors<br>egocentric<br>Errors<br>landmark<br>Time<br>allocentric<br>Time<br>egocentric<br>Hidden Patterns<br>−0.38*<br>Mental rotation<br>−0.01<br>−0.45**<br>Errors allocentric<br>0.00<br>−0.27<br>0.31*<br>Errors egocentric<br>0.13<br>−0.23<br>0.37*<br>0.45**<br>Errors landmark<br>0.25<br>−0.29<br>0.07<br>0.28<br>0.16<br>Time allocentric<br>0.13<br>−0.42**<br>0.39**<br>0.61**<br>0.22<br>−0.01<br>Time egocentric<br>0.10<br>−0.14<br>0.21<br>0.45**<br>0.77**<br>0.06<br>0.26<br>Time landmark<br>0.13<br>−0.18<br>0.18<br>0.02<br>0.13<br>0.55**<br>0.14<br>0.09<br>Note. *_p_< 0.05, **_p_< 0.01. Errors are numbers of false clicks in the respective route condition. Time means the duration in seconds to complete the route<br>following task in the respective condition|
|---|---|---|---|---|---|---|---|---|---|
||Time<br>egocentric||||||||0.09|
||Time<br>allocentric|||||||0.26|0.14|
||Errors<br>landmark||||||−0.01|0.06|0.55**|
||Errors<br>egocentric|||||0.16|0.22|0.77**|0.13|
||Errors<br>allocentric||||0.45**|0.28|0.61**|0.45**|0.02|
||Mental<br>rotation|||0.31*|0.37*|0.07|0.39**|0.21|0.18|
||Hidden<br>patterns||−0.45**|−0.27|−0.23|−0.29|−0.42**|−0.14|−0.18|
||Perspective<br>taking|−0.38*|−0.01|0.00|0.13|0.25|0.13|0.10|0.13|
|||Hidden Patterns|Mental rotation|Errors allocentric|Errors egocentric|Errors landmark|Time allocentric|Time egocentric|Time landmark|



57 

3 OriGami: A Mobile Geogame for Spatial Literacy 

The study shows a successful evaluation of the route-following task in **OriGami** . The task (1) varies in difficulty due to particular spatial processes, such as correction of misalignment, (2) correlates with spatial ability (mental rotation) and (3) demonstrates performance differences which plausibly depended on expertise. Build upon these results, the **OriGami** game can be extended to train more spatial competencies. The study also brought more detailed questions regarding the cognitive processes associated with the tasks which can be systematically explored in an extended version of **OriGami** . In particular, the cognitive requirements of the landmark condition seemed to differ from the egocentric and the allocentric condition. Moreover, individual differences in spatial encoding and perspective taking did not play important roles in accomplishing the tasks. 

## **3.6  Spatial Literacy Training with OriGami** 

Based on the study results with our first prototype presented above and based on the requirements we draw from curricula, we developed a comprehensive concept of the **OriGami** game that supports the acquisition of better spatial competencies while playing the game through a series of navigation and orientation tasks. Like in the prototype version, the player is equipped with a smartphone or tablet (which provides positioning technologies). The goal is to navigate to a certain location where you have to solve a task. Those routes are created beforehand by a game master /teacher in the inbuilt editor. The following features have being included in the final conceptualization of the game. 

## _**3.6.1  Navigation**_ 

Two different navigation types can be distinguished: an aided navigation task or a path planning task. In the aided navigation task, the player receives route instructions to the next waypoint. Instructions are given either allocentric, egocentric or landmark-based. Based on the given route instruction the player has to move in the real environment and find the next waypoint to receive the next instructions which successively lead her to the destination. In the path planning task the player receives a map of the environment and the destination visualized on this map. The player has to locate him or herself on the map and determine the best route to the destination. 

Once arrived at the destination, the user has to solve a task. This task can be defined by the teacher. In principle these tasks can relate to any subject from STEM to social sciences and arts. In the following sections, we describe tasks training orientation and map comprehension. Students solve one task at each destination, but the teacher can define different task for each destination. 

58 

T. Bartoschek et al. 

## _**3.6.2  Orientation Task**_ 

The user has to georeference a photo (in more detail: the position from where the photo was taken) and add spatial or thematic data to the map that can be derived from the photo. Depending on the subject and the degree of difficulty, the photo might show different things, e.g. in case of historical photos, the scenery might have changed. New houses might occlude houses that are visible on the historic photo. The photo might show underground supply circuits that are not visible either. This way we can create tasks with different levels of complexity challenging the player’s ability to read and interpret a map. 

## _**3.6.3  Map Comprehension Task: Cartographic Basics**_ 

To make abstract concepts such as coordinate systems more concrete, teachers design tasks that help to experience coordinate systems in practice. For example, students are asked to walk along longitudes, latitudes, certain degrees or angles, or walk to the most northern/southern point of the destination region (e.g. a school ground, a park, a square). 

## _**3.6.4  Map Comprehension Task: Spatial Learning**_ 

The task to draw a map from home to school is classical in most curricula. Thus, the same task can be integrated in **OriGami** . Students are asked to draw a sketch map of the route they travelled, take a picture of the sketch map, and upload it to the system. Other players of the game travelling the same route can rate previously created maps. The teacher can use this material also in an after-game class to analyze typical cartographic concepts. 

## _**3.6.5  Spatial Competency Testing and Training**_ 

The navigation task fosters different spatial competencies. Depending on the configuration of the app, we visualize a player’s own location (determined via GPS) with differing degrees of precision or we do not visualize it. This way players have to determine the own position on a map. The app can be used for map alignment tasks, if the automatic alignment to users' movement direction is switched off. Cartographic basic principles such as map scale are trained by navigational aids referring to objects visible only at certain scales (e.g. local 

59 

3 OriGami: A Mobile Geogame for Spatial Literacy 

landmarks along the route or global landmarks off the route), which requires the player to change the scale of the map. 

The georeferencing and mapping task also fosters spatial competencies: In the photo georeferencing task, the player has to relate objects in the map to objects in the reality. She has to align the map or apply mental rotation with different degrees of complexity (occlusion of objects, 2D and 3D rotations). The data collection task trains the player in understanding symbols and cartographic elements in maps. Different degrees of complexity range from collecting data falling in an existing thematic category to collecting data that forces the player to create new categories. Here, new thematic categories with suitable symbols and visualization need to be identified. In contrast to many other games, this app supports different map types that involve not only street networks as background map but also other map types (different providers like OSM, topographic maps or satellite images). Different map types shall point children to the advantages and disadvantages of different maps for certain tasks. 

## _**3.6.6  Game-Based Aspects**_ 

The game can be played in different modes depending on the settings that are chosen by the teacher. 

**Environment** : The game can be played in the real environment (which ensures real experiences for the player) or in a stationary class-room mode. 

**Adaptability/customization** : The routes in the navigation task and the task at the destination are set-up by the teacher. Furthermore, the teacher can choose different settings for the game that lead to different complexity levels when playing the game. This way the teacher can adapt the game to the learning stage of the students. An editor is provided to define routes and tasks (e.g. the upload of photos). The route instructions can be provided and edited by the teacher or the game leader. 

**Teamwork** : **OriGami** can be played as single-user or multi-user game. In the multi-user setting, we aim for two different modes: In the collaborative mode, we focus on team aspects. It incorporates the same orientation tasks as in the basic game but adds collaborative and competitive elements where one player is the editor describing routes and the other is the scout following the instructions. This mode was inspired by game shows where a game master guides the players/teams through competitions. 

**Game Element** : The user receives instant feedback via a smiley for his or her actions. Feedback and hints allow the user to orientate and find reference points in the map and in the real world. In general playing digital games develops soft skills of the user. Students are expected to be better at working in teams and gain experience in using geospatial technologies. ICT (Information and Communication Technologies) skills are practiced playing digital games. 

60 

T. Bartoschek et al. 

## **3.7  Conclusion** 

In this chapter we review curricula specifications regarding spatial competency and spatial literacy training in an educational context. We evaluate the state of art for geogames that focus on training spatial competencies and identified a lack of tools fostering spatial competency and spatial literacy for children and young adults. Many spatial competencies are studied theoretically in school. Geogames allow users to experience many of these theoretical concepts in the real world, e.g. experience map alignment and orientation in a goal-directed wayfinding task or experience the concept of a coordinate system and cardinal directions in the real world. 

The geospatial technologies required for such games exist and are robust enough to be used in educational games. Therefore, we propose **OriGami** , an educational game fostering spatial literacy. **OriGami** allows users to train specific spatial competencies through a set of tasks and measure performance in these tasks. By relating it to the user’s spatial abilities, it allows teachers to individually select training tasks for specific competencies. In the empirical study, we showed the relation of spatial abilities and performance to support the need for comprehensive, curriculum- based geogames. 

Future work addresses the further development of the **OriGami** game according to the game concept above. Afterwards, we intend to conduct studies where spatial literacy and competency development is measured over a longer term period to show the effect of **OriGami** . 

**Acknowledgments** This work was supported by the Erasmus+ grant VG-SPS-NW-14-000714-3. Furthermore, we would like to thank Matthias Pfeil for the software development and ESRI Inc. for their financial support. 

## **References** 

Allen G, Kirasic K, Rashotte M, Haun D (2004) Aging and path integration skill: kinesthetic and vestibular contributions to wayfinding. Percept Psychophys 66(1):170–179 Attewell J (2015) BYOD bring your own device: a guide for school leaders. European Schoolnet, Brussels, Belgium 

Baker TR, Battersby S, Bednarz SW, Bodzin AM, Kolvoord B, Moore S, Uttal D (2015) A research agenda for geospatial technologies and learning. J Geogr 114(3):118–130 

Bartoschek T, Bredel H, Forster M (2010) GeospatialLearning@PrimarySchool: a minimal GIS approach. In: Sixth international conference on geographic information science, extended abstracts. University of Zürich, Zürich, Switzerland 

Battersby SE, Golledge R, Marsh M (2006) Incidental learning of geospatial concepts across grade levels: map overlay. J Geogr 102:231–233 

Baudisch P, Rosenholtz R (2003) Halo: a technique for visualizing off-screen objects. In: SIGCHI conference on human factors in computing systems. ACM, New York 

Bell M, Chalmers DJ, Barkhuus L, Hall M, Sherwood S, Tennet P, Brown B (2006) Interweaving mobile games with everyday life. In: CHI—SIGCHI conference on human factors in computing systems. Montréal, Canada. ACM, New York, pp 417–426 

3 OriGami: A Mobile Geogame for Spatial Literacy 

61 

- Bitgood S (1991) Common beliefs about visitors: do we really understand our visitors? Visitor Behav 6(1):6 

- Burigat S, Chittaro L, Gabrielli S (2006) Visualizing locations of off-screen objects on mobile devices: a comparative evaluation of three approaches. In: 8th conference on human-computer interaction with mobile devices and services. ACM, New York 

- Clarke B, Svanaes S (2015) Updated review of the global use of mobile technology in education. Techknowledge for Schools, London 

- Committee on Support for Thinking Spatially, The Incorporation of Geographic Information Science Across the K-12 Curriculum, National Research Council (2006) Learning to think spatially. National Academies Press, Washington, DC 

- Couclelis H (1996) Verbal directions for way-finding: space, cognition, and language. The construction of cognitive maps. Springer, Berlin 

- Deterding S, Dixon D, Khaled R, Nacke LE (2011a) From game design elements to gamefulness: defining gamification. In: 15th international academic MindTrek conference: envisioning future media environments. ACM, New York 

- Deterding S, Dixon D, Khaled R, Nacke LE (2011b) From game design elements to gamefulness: defining gamification. In: Mindtrek 2011. ACM Press, Tampere 

- Feulner B, Kremer D (2014) Using geogames to foster spatial thinking. Herbert Wichmann Verlag, Heidelberg 

- Flügel K (2014) Einführung in die Museologie, 3rd edn. WBG Verlag, Darmstadt 

- Fudenberg D, Levine DK (1998) The theory of learning in games. MIT Press, London 

- German Association for Geography (DGFG) (2007) Educational standards in geography for the intermediate school certificate. Deutsche Gesellschaft für Geographie (DGfG), Germany 

- Goodchild M (2006) The fourth R? Rethinking GIS education. ArcNews 28(3):5–7 

- Guay R (1976) Purdue spatial visualization test. Purdue University, West Lafayette, IN 

- Gunzelmann G, Anderson JR (2006) Location matters: why target location impacts performance in orientation tasks. Mem Cogn 34:41–59 

- Gustafson S, Baudisch P, Gutwin C, Irani P (2008) Wedge: clutter-free visualization of off-screen locations. In: SIGCHI conference on human factors in computing systems. ACM, New York 

- Hegarty M, Montello D, Richardson AE, Ishikawa T, Lovelace KL (2006) Spatial abilities at different scales: Individual differences in aptitude-test performance and spatial-layout learning. Intelligence 34:151–176 

- Hemmer I, Hemmer M, Neidhardt E (2007) Räumliche Orientierung von Kindern und Jugendlichen—Ergebnisse und Defizite nationaler und internationaler Forschung. In: Geiger M, Hüttermann A (eds) Raum und Erkenntnis. Aulis Verlag Deubner, Köln 

- Jansen-Osmann, P., & Heil, M. (2007). Suitable stimuli to obtain (no) gender differences in the speed of cognitive processes involved in mental rotation. Brain and Cognition, 64(3), 217–227. doi:http://dx.doi.org/10.1016/j.bandc.2007.03.002 

- Krukar J, Conroy Dalton R (2013) Spatial predictors of eye movement in a gallery setting. In: Eye tracking for spatial research, proceedings of the first international workshop (in conjunction with COSIT 2013). Scarborough, UK 

- Li R, Korda A, Radke M, Schwering A (2014) Visualising distant off-screen landmarks on mobile devices to support spatial orientation. J Locat Based Serv 3:166–178 

- Linn D, Petersen A (1985) Emergence and characterization of sex differences in spatial ability: a meta-analysis. Child Dev 56(6):1479–1498 

- Marsh M, Golledge R, Battersby SE (2007) Geospatial concept understanding and recognition in G6-College students: a preliminary argument for minimal GIS. Ann Assoc Am Geogr **97** (4):696–712 

- Ministério da Educação DdEB (2001) Currículo Nacional do Ensino Básico—Competências Essenciais 

- Ministério da Educação e do Desporto SdEF (1998) Parâmetros Curriculares Nacionais. Terceiro e Quarto Ciclos do ensino fundamental de geografia., Brasilia 

62 

T. Bartoschek et al. 

- Ministry of Education RoR (2006) National Curriculum Development Centre (Ed.) In: Social studies curriculum for the basic education programme 

- Münzer S, Stahl C (2011) Learning routes from visualizations for indoor wayfinding: presentation modes and individual differences. Spat Cogn Comput 11(4):281–312 

- Naismith L, Lonsdale P, Vavoula GN, Sharples M (2004) Mobile technologies and learning. Futurelab, Malaysia 

- Newcombe N, Huttenlocher J (2000) Making space: the development of spatial representation and reasoning. MIT Press, Cambridge, MA 

- Nordrhein-Westfalen (2008) Richtlinien und Lehrpläne für die Grundschule in NordrheinWestfalen: Deutsch, Sachunterricht, Mathematik, Englisch, Musik, Kunst, Sport, Evangelische Religionslehre, Katholische Religionslehre. Schule in NRW, Ritterbach, Frechen 

- OECD (2014) PISA 2012 results in focus: what 15-year-olds know and what they can do with what they know. OECD, Paris 

- Piaget J, Inhelder B (1975) Die Entwicklung des räumlichen Denkens beim Kinde Gesammelte Werke 6 (Studienausgabe), 3rd edn. Klett-Cotta/J. G. Cotta’sche Buchhandlung Nachfolger, Germany 

- Prensky M (2007) Digital game-based learning. Paragon House, St. Paul, MN 

- Republic of Rwanda MoE (2006) Social studies curriculum for the basic education programme, grades 1–6 

- Robinson ES (1928) The behaviour of the museum visitor. The American Association of Museums, Washington 

- Schlieder C (2005) Representing the meaning of spatial behavior by spatially grounded intentional systems. In: GeoSpatial Semantics. Springer, Berlin, pp 30–44 

- Schlieder C (2014) Geogames–Gestaltungsaufgaben und geoinformatische Lösungsansätze. Informatik-Spektrum 37(6):567–574 

- Schlieder C, Kiefer P, Matyas S (2006) Geogames—designing location-based games from classic board games. IEEE Intelligent Systems, Special Issue on Intelligent Technologies for Interactive Entertainment. p 40–46 

- Schwering A, Münzer S, Bartoschek T, Li R (2014) Gamification for spatial literacy: the use of a desktop application to foster map-based competencies. In: AGILE workshop geogames. Utrecht University, Netherlands 

- Sharples M (2006) big issues in mobile learning: report of a workshop by the kaleidoscope network of excellence—mobile learning initiative. The University of Nottingham, UK 

- Shepard RN, Metzler J (1971) Mental roation of three-dimensional objects. Science 1(71):701–703 

- Steck SD, Mallot HA (2000) The role of global and local landmarks in virtual environment navigation. Presence 9:69–83 

- Waller D (2000) Individual differences in spatial learning from computer-simulated environments. J Exp Psychol 6(4):307–321
