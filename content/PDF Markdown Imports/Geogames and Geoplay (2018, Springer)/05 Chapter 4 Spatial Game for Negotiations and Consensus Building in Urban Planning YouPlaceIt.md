---
title: "Chapter 4 Spatial Game for Negotiations and Consensus Building in Urban Planning: YouPlaceIt!"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 4 Spatial Game for Negotiations and Consensus Building in Urban Planning: YouPlaceIt!** 

## **Alenka Poplin and Kavita Vemuri** 

## **4.1  Introduction** 

Striving to reach consensus about the use of resources is crucial in spatial planning. Civic engagement and participatory planning support activities of negotiation and consensus building. Negotiation, as considered in this work, is a process of communication in which parties exchange their messages, opinions, or statements in order to influence the other party (Fisher 1991). In simple terms, negotiation is a discussion between two or more disputants who are trying to work out a solution to their problem. Many situations in urban and regional planning require negotiations and consensus building. Some examples may include questions like where to locate a new road; how to design the newly created park; and what is the best location for a new shopping mall. A negotiation can be interpersonal where several individuals negotiate, or inter-group in which groups negotiate among themselves. It can include different stakeholders: the residents of the planned area, various government departments, real-estate developers, industry, and non-governmental organizations (NGO’s). Reaching a consensus among different stakeholders is a challenging task which often needed to involve compromises among all involved parties. These negotiations take place because the stakeholders and individuals wish to create something new or resolve a problem or dispute. The problem usually arises when there are conflicting interests involved on how to use natural resources, land, 

A. Poplin ( * ) Iowa State University, Ames, IA, USA e-mail: apoplin@iastate.edu 

K. Vemuri International Institute of Information Technology, Hyderabad, India e-mail: kvemuri@iiit.ac.in 

63 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_4 

64 

A. Poplin and K. Vemuri 

buildings and/or how to revitalize and further develop cities and landscapes. One of the big challenges faced by planners that facilitate participatory planning and civic engagement represents the process of consensus building in which the parties can present their conflicting points of view with the goal of arriving at an agreement. 

This chapter explores the possibility to use an online game-based approach for negotiations and consensus building in urban planning. In general, the geo-location could be anywhere in the world, and the game implementation might result in a spatial game, sometimes referred to as a geogame (Schlieder et al. 2006; Ahlqvist 2011; Ahlqvist et al. 2012; Poplin 2012b, 2014) or location-based game (Schlieder et al. 2006). In our case study we selected one of the largest low-income areas in Mumbai (India), which is called Dharavi. The area is inhabited, at a conservative estimate, by around 3,000,000 residents. Most of them are employed in the service sector or run their own small enterprises. Even though this is considered a lowincome community, the small-scale enterprises and the skills of the people play a crucial role in the economy of the whole city. Over the last three decades, several re-development plans for the area have been proposed by the Dharavi Redevelopment Agency (DRA n.a.), real estate developers, and non-governmental organizations such as the National Slum Dwellers Organization (NSDO n.a.). Many of the plans faced resistance from the local residents who are the primary stakeholders. The governmental and city organizations did not attempt to organize a process of consensus building with local residents (Arputham and Patel 2010), but rather moved forward to with preparations to present the new master plan. This caused additional problems because some of the stakeholders were not willing to accept the suggested re-development plan. 

The development of Dharavi is an interesting case study for our novel approach of using an online game-based application for consensus building; the process of exchange and negotiation within the game brings different stakeholders together to listen to different points of view. The main goal of the game **YouPlaceIt!** presented in this chapter is to enable stakeholders to communicate and resolve urban planning issues. The challenges arise when there are different and conflicting ideas about and how to revitalize and further develop cities and landscapes and how to use natural resources, land, and buildings. This game assumes that the stakeholders wish to redevelop the area, create something new, and resolve problems or disputes, and thus parties wish to negotiate. One of the main tasks of the consensus building process is to enable information exchange, communication, and the ability to express views without the fear of backlash from the community or from the powerful parties involved in the negotiation process. In a broader sense, we would like to contribute solutions which could contribute to a more sustainable way of living and co-creation of cities in which everybody feels heard and accepted. 

Drawing from existing literature on negotiation and serious games for urban planning, our goal is to assess whether it is possible to develop a game that can bring different stakeholders together who are facing urban planning challenges. Section 4.2 reviews previous work related to collaborative planning and consensus building, negotiation models, communication in physical vs. digital environment, Public Participation Geographic Information Systems (PPGIS), and digital serious spatial 

65 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

games for urban planners. Section 4.3 introduces the complexity of urban planning process in the selected study case of a slum area Dharavi in Mumbai, India. It suggests game-based negotiation and consensus finding as a possible solution which could potentially bring different stakeholders together. Section 4.4 describes the implemented game **YouPlaceIt!** while Sect. 4.5 provides results of testing on a small sample of potential users of the game and suggests further research and implementation directions. Section 4.6 concludes the chapter with an overview and a discussion about the findings. 

## **4.2  Previous Work** 

## _**4.2.1  Collaborative Planning and Consensus Building**_ 

Collaborative planning is an interactive process of consensus building among different stakeholders and public engaged in planning activities. Collaborative planning requires participation and engagement at the bottom, or grass roots level, and a strong political and professional support at the top (Fischer 2006). The main shift towards collaborative planning happened in the 1990s and was based on communicative action theory (Innes 1995). The role of planners, the public, and stakeholders gradually changed; planners became facilitators and mediators, considering the different opinions and positions of the parties involved in collaborative planning processes (Brooks 2002). Additionally, Fischer (2006) describes active participants as empowered, participatory citizens that can effectively participate in shaping public programs and policies. An empowered citizenry is achieved when the citizens provide their input related to the topics discussed and the government intentionally pursues their input and provides the needed resources and knowledge for the citizens to participate and influence public decisions and planning policies. Communicative action or collaboration is the theoretical model for planning, while consensus building or capacity building are techniques within those models. 

Consensus building in urban planning is a complex process with several stakeholders involved in planning, re-development, and decision-making. These groups are often driven by self-interest, following an agenda that can conflict and contradict the goals of other involved groups and individuals. Most proposed development plans by either government or private real-estate developers are prone to distrust by the local community. This is especially the case when the local community (a) does not have access to all data/information, (b) experiences a lack of transparency in information sharing, (c) are not involved in the planning and negotiations about the development plans which affect them, and/or (d) are not involved in decision-making. 

In the process of consensus building, all opinions and concerns must be considered and seriously assessed by all involved parties. Such consensus building processes depend on the involvement of a diverse range of stakeholders and individual citizens. During the consensus building process, the involved parties can gather a 

66 

A. Poplin and K. Vemuri 

variety of information about planning activities and alternative solutions and exchange their opinions about the discussed topics. The expressed opinions and experience can be used to create plans, evaluate the effectiveness of systems and projects, and adapt the processes to meet ever-evolving goals (Innes and Booher 2002). The consensus building process can be organized on a virtual platform or in a face-to-face environment. The facilitator/planner may design the process and mediate among the parties. In this way, the involved parties can explore planning alternatives, learn about them, and finally arrive at a solution which they could all agree upon (Innes 1996). 

Collaborative planning can facilitate creation of sustainable communities that can effectively deal with the complex issues facing cities today (Innes and Booher 2002; Roseland 2005). This chapter will explore whether a consensus building process can be facilitated with the help of a computer-based application, and the possible implementations that could support effective information exchange and online negotiations. 

## _**4.2.2  Negotiation Models**_ 

Negotiation is a process of communication and some researchers distinguish between linguistic and non-linguistic approaches. The social-psychological perspective considers negotiations as a way to satisfy the needs of the parties involved in the negotiation process. Negotiation is also studied as a strategic behaviour (Donohue et al. 1984; Putnam and Jones 1982; Fant 1992). Sokolova and Lapalme 2012 distinguish between the means of interaction (face-to-face, email, chat), communication modes (synchronous or asynchronous), and interaction modes (one-toone, one-to-many). Negotiation models exemplify human behavior like decision-making processes of the parties involved in the negotiation and consensus building, conflict resolution and cooperation. Which negotiation models can be applied in a serious game and how can they best be implemented? Some possible behavior models that can be applied in a game include the Nash equilibrium, Quantal response equilibrium QRE (McKelvey and Palfrey 1995), cognitive hierarchy (Camerer et al. 2004), or the level-k (Costa-Gomes et al. 2001; Nagel 1995). 

The level-k model may enable to model strategic thinking and the possibility to adopt an optimal response of a player to the beliefs about other players and their activities. This model attempts to depict the closest to real-life conditions and situations. It can capture the essence of each role the player has in the game. One of the variants or conditions of the Nash equilibrium is the zero-sum game, which translates to one party wining at the cost of the other, a proposition that could have disastrous implications in many urban development plans. The level-k model combined with a game play that strives or forces people to reach mutually beneficial or agreeable consensus can be achieved by principled or integrative negotiation models, as implemented in the case study discussed in this chapter. 

67 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

## _**4.2.3  Communication in Physical vs. Virtual Space**_ 

While consensus finding in urban planning occurs mainly in the physical space through face-to-face discussion among various stakeholders trying to reach a solution; urban planning games can constitute an interesting alternative in a virtual space. These games can allow for e-negotiations through multiple channels; players can take on different roles, and varied solutions can be simulated and analyzed through a visualization of the urban space under consideration. Firth makes a distinction between activity and encounter in negotiations. He distinguishes between a _negotiation encounter_ , which is physically defined as the location where the conflicting parties convene, and a _negotiating activity_ , which refers to the communicative interaction of the parties involved and their aim to reach mutual alignment. The two aspects are not regarded as the same thing and furthermore are not interdependent. 

Sokolova and Lapalme (2012) show that the use of electronic means changes the way people communicate during negotiations. In face-to-face negotiations, information can be gained through a non-verbal body language such as gestures and movements as well as language characteristics such as tone of voice and pauses. Language also plays an important role in text-based electronic negotiations, offering insights in the negotiation process (i.e. conditions of bargaining, introduction and closure) as well as in the social aspects. An analysis of the informativeness of messages exchanged by negotiators based on linguistic signals (i.e. the presence or absence of degree, scalar and comparative word categories) shows correlations with negotiation success or failure (Sokolova and Lapalme 2012). The use of text-based forms of communications such as online messages boards, email, instant messages and text messages, and their impact in the communication process, have been extensively analysed in the literature (Naquin et al. 2010); Clark and Brennan 1991). Considerably less attention has been devoted to the embedding of these media within (online) games (i.e. in-game chat). Instead, they have been addressed mainly in the educational context, especially with respect to language learning (Kardan 2006). 

## _**4.2.4  Public Participation Geographic Information Systems (PPGIS)**_ 

Several recent developments aim to offer alternative online participatory options. Public Participation Geographic Information Systems (PPGIS) utilize a geographic information system (GIS) as the base technology that stores spatial data and enables spatial analysis and spatial queries. The user interface is based on interactive maps displaying the area which is the main subject of participatory process. Participatory functionalities are added to the main GIS user interface; they aim to enable the stakeholders to express their opinions, participate in public debates and contribute the discussion about currently relevant issues in their neighborhoods, cities or states. 

68 

A. Poplin and K. Vemuri 

PPGIS was conceptually developed in the 90s, followed by example implementations in the mid-90s. The term PPGIS was coined in 1996 at the National Center for Geographic Information and Analysis (NCGIA) Workshop, Orono, Maine, July 10–13, 1996 (Schroeder 1996). The concepts of PPGIS and its possible implementations has been intensely discussed by many researchers (Pickles 1995; Schroeder 1996; Rinner 1999; Talen 1999; Kingston et al. 2000; Al-Kodmany 2001; Basedow and Pundt 2001; Carver 2001; Jankowski and Nyerges 2001; Craig et al. 2002; Schlossberg and Shuford 2005); Georgiadou and Stoter 2010). In the mid-90s, PPGIS promised a novel way of citizens’ involvement into decision making enabled by online, interactive maps and included participatory functions. These participatory functions allowed posting online comments related to spatial objects, which lead to the concept of argumentation maps introduced by Rinner (1999, 2001, 2005, 2006). They enabled online chats, comments, discussions, sketches, and exchanges of opinions related to the issues in question. The citizens were able to send their annotated maps to the planning authorities (Steinmann et al. 2004) or leave a comment directly on the online maps (Rinner 1999; Al-Kodmany 2001; Rinner 2005, 2006; Poplin 2012a, 2015). These comments were then stored in a GIS database. A GIS enabled to display them according to the criteria needed for spatial analysis. Figure 4.1 shows an example of a PPGIS applications developed to discuss ways inhabitants of Wilhelmsburg, in the city of Hamburg, use their canals (Poplin 2012a). The three pencils on the right hand side of the map enable them to draw paths they use for walking, jogging, walking their dog, biking, and other activities. 

The idea of PPGIS resulted in a variety of implemented applications aiming to enhance participatory processes with novel digital visualization possibilities. An 

**Fig. 4.1** PPGIS for Wilhelmsburg, Hamburg, Germany (Poplin 2012a) 

69 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

intense debate in the scientific research community lasted about 15 years (90s to mid-2000s). In 2006, Sieber published her paper providing a thorough overview of the research contributions looking back at more than fiftheen years of research effort. The positive aspect of PPGIS development was summarized by Shuford (2005) as follows; “PPGIS represents a broad notion that the spatial visualization and analysis capacities inherent in GIS present a unique opportunity for enhanced citizen involvement in public policy and planning issues.” Other advantages are related to the data. Data presented and collected online is georeferenced, stored in a digital format and easier to process and analyze than data collected at the traditional public participatory meetings (Kingston et al. 2000). It can be shared easily online (Thompson 2000) and is accessible by many at the same time from anywhere with an internet connection. 

The critique of PPGIS focuses mostly on the usability of these complex and technically advanced systems (Haklay and Tobón 2003). Steinmann et al. (2004) and Poplin (2015) report on the complexity of the applications and the problems users might have while using them. The idea and the conceptual model did not result in many practically successful PPGIS applications. The problem of complexity of PPGIS implementation and the lack of their user-friendliness lead to novel ideas such as serious digital geogames, often referred to as spatial or location-based games. These terms will be used interchangeably in this chapter. Serious spatial games aim at overcoming the issues of PPGIS, especially due to the complexity of the user interface introduced to the users, while still using GIS as the technology that enables visualization of interactive environments. 

## _**4.2.5  Digital Serious Games for Urban Planning**_ 

Digital serious games may enable online experimentation, online exploration of the urban planning situation, visual and interactive representation of the key issues that are being discussed in the planning process, and alternative ways of collecting data and involving citizens into planning for the future of their cities. With their focus on serious issues, they can be categorized as serious games, games designed for “more than just fun”, “entertaining games with non-entertainment goals”, or games for change. They may aim to facilitate learning (Gee 2004, 2005; Lemke 1998) and problem solving (Abt 1970). Learning in such games can be facilitated with the help of experimentation (Lemke 1998); several alternatives can be tested in the game environment without serious consequences, which would happen in the case of a non-game, real-world experience. The players may learn, study the information given to them, in the order that suits them and at the speed and pace that can be optimal for their own personal experience. Digital serious games can come in “any form of interactive computer-based game software for one or multiple players to be used on any platform that has been developed with the intention to be more than entertainment” (Ritterfeld et al. 2009, p. 6). 

Recently this area of research gained more attention due to a possible combination of GIS and games. Several digital serious games for urban planning have been 

A. Poplin and K. Vemuri 

70 

developed. Gordon and Manosevitch (2010) describe a pilot project “Hub2”, which took place in Boston, Massachusetts from June to August 2008. Devisch (2011) focuses on Second life and its possible use for urban planning. Poplin (2012b, 2014) introduces the NextCity and B3-Design your Marketplace! games, which aim to facilitate public participation in urban planning. None of these games focused on negotiations and consensus building. They mostly aim to support civic engagement and explore the possibilities for the implementation of game-based, playful civic engagement in urban planning. We are interested in how consensus building can be implemented in a game-based online system. Can serious spatial games for urban planning enable and facilitate consensus building in civic engagement situations? How can they best support consensus building processes? The next section introduces the study case Dharavi and the main requirements for an online game-based negotiation and consensus building. 

## **4.3  Negotiation for Building Consensus Among Stakeholders: Case Study of Dharavi** 

## _**4.3.1  The Selected Study Site: Dharavi in Mumbai, India**_ 

Our specific focus is on the situation of Dharavi, one of the biggest slum areas in India. It was declared by the Slum Rehabilitation Agency (SRA) as one of the most difficult areas to revitalize due to many conflicting interests about how this site should be further developed. Dharavi is embedded into the city of Mumbai, and is located between the Sion Hospital on the south, surrounded by three major roads on the north-east and east (Fig. 4.2). It is accessible from both Western and Central railways. With the advantageous location neighbouring the business district in Mumbai, the land of Dahravi is of premium interest among builders. 

Dharavi offers home to more than three million residents who can be described as self-sufficient people. The inhabitants of Dharavi are also known for their entrepreneurial spirit. They create job opportunities on their own, which range from small shops to the citizens involved in recycling activities (Fig. 4.3a, b). Dharavi is home to more than 15,000 small-scale home businesses. The recycling units of Dharavi generate revenue by turning around the discarded waste of not only Mumbai’s 21 million citizens, but from all around the country and abroad. However, the government does not recognize these industries as it would have to start giving subsidies (Chandan 2014). 

## _**4.3.2  The Issues of Civic Engagement in Dharavi**_ 

The redevelopment project of Dharavi was first announced in 2004, followed by the presentation of the new master plan. The main goals of the redevelopment plan can be summarized as follows: formulate sustainable development master plan, 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

71 

**Fig. 4.2** Google satellite image of the study area of Dharavi in Mumbai, India with proposed new road expansion plans 

**Fig. 4.3** ( **a** and **b** ) Small entrepreneurs of Dharavi (Chandan 2014) 

rehabilitate all the slum families/businesses, retain all eligible existing rehabilitated families/businesses, rehabilitate non-polluting industries, and integrate slum dwellers with the main stream residents (Mehta 2010). In 2007, global tenders were invited to submit an expression of interest to be part of the redevelopment activities. Slum Rehabilitation Agency (SRA), together with consulting teams, offered high incentives to the citizens and other stakeholders to comply with the solutions 

A. Poplin and K. Vemuri 

72 

proposed in the master plan. Over 200 PowerPoint presentations that promoted the presented master plan were shown across the area. They were organized for the local inhabitants, local leaders, political leaders, and leading entrepreneurs. About 70,000 pamphlets and 500 posters were distributed in Dharavi to inform the stakeholders about the planned activities. The organizing institutions/organizations included Maharashtra Housing and Development Authority (MHADA), Slum Rehabilitation Agency (SRA)—the proposed rehabilitation and implementation agency at that time, the Local Corporators implementations agency at that time, the Municipal Corporation of Greater Mumbai (MCGM), Mumbai Metropolitan Regional Development Authority, Assistant Director of Town Planning, the Chairman of the co-operative societies of Dharavi, the NGO’s operating in Dharavi, Department of Housing/Government of Maharashtra, Department of Urban Development, Department of Finance, the Chief Secretary/GoM, and the representatives of the Planning Commission. The process considered by government agencies has been to make unilateral decisions. Politically and socially this lead to a sense of distrust by the community and individual owners, exclusion of many stakeholders, and many disagreements about how the space should be used, re-vitalized, and further developed. 

Following the global real-estate crisis in 2008, five executing companies exited the project in 2009, citing lack of clarity and delays in the implementation. Some of the key-stakeholders and bidding companies withdrew from the project as a result of dissatisfaction, lack of transparency, lack of information sharing, and support of the plan by the local inhabitants (Mehta 2010). Of 14 bidders, only seven submitted the Memorandum of Understanding they signed with their foreign partners. In the same year, a survey report claimed that 63% of Dharavi residents are ineligible for houses defined within the project. In spite of all the talks, presentations, flyers, and posters, only 15% of Dharavi was restructured and redeveloped in the period of 15 years. The local developers kept building poor quality housing in this area with negligible benefits to the local citizens, entrepreneurs, landowners, and government. Even as the state government finally begun to work on the Dharavi redevelopment project, residents of the area lacked clarity about the status of the project; they did not feel informed about the redevelopment plan. 

## _**4.3.3  Novel Approach for Civic Engagement in Dharavi**_ 

The entrepreneurial spirit of Dharavi and the active inhabitants of this redevelopment area may be attracted by fresh approaches to citizens’ engagement and public participation in urban planning. Novel digital technologies can enable creation of online platforms for discussions, debates, and a method of consensus building by inclusion of all stakeholders. In our approach we suggest a development of a serious, online, digital spatial game which may focus on sharing the information about the redevelopment of Dharavi and enable the stakeholders to communicate and 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

73 

exchange their positions on the important issues and decisions to be made in the redevelopment process. The users of a game may be the inhabitants of Dharavi, and organizations and agencies such as Maharashtra Housing and Development Authority (MHADA), Slum Rehabilitation Agency (SRA), the Local Corporators implementations agency, the Municipal Corporation of Greater Mumbai (MCGM), Mumbai Metropolitan Regional Development Authority, the Assistant Director of Town Planning, the Chairman of the co-operative societies of Dharavi, the NGOs operating in Dharavi, the Department of Housing/Government of Maharashtra, the Department of Urban Development, the Department of Finance, the Chief Secretary/GoM, and/or the representatives of the Planning Commission. The digital technology may enable information sharing and dialogue among the involved stakeholders. 

Our suggested approach includes a development of a prototype for an online game that may enable negotiations related to the planned activities in Dharavi or any other selected place/neighborhood. The communication may be based on the use of language and creation of online, digital environments that may enable consensus building. Can we create an online serious geogame that will enable negotiations? Can such a game bring people of Dharavi and involved stakeholders together? Which negotiation algorithms can be used in such situations and how can they be implemented within a game? What are possible limitations of this approach? 

## _**4.3.4  The Main Requirements for the Negotiation and Consensus Building Game for Dharavi**_ 

The main requirement for a negotiation game for Dharavi focuses on bringing all parties interested in redevelopment of Dharavi together. The game aims to serve as a platform for an exchange of information, an exchange of opinions, and often contradicting ideas about the use of space in Dharavi. The main goals of the game are to enable the users to communicate, exchange their opinions about the proposed projects, negotiate about the proposed projects, and view the progress of discussions and the implementation of the redevelopment plan. 

The requirements for the game design process may include the following guidelines: 

- The game represents a specific, concrete area that exists in the real world: Dharavi can serve as a very specific example where civic engagement and public participation are needed in order to discuss and view the redevelopment plans. 

- Relation to the real-world issues/area represent the “serious” part of the game: The visualization of Dharavi should be realistic in order to enable focused discussions about very specific projects and redevelopment plans. 

- Fun to play: The game aims to attract many different stakeholders. The fun aspects of the game can be implemented in a variety of different ways. The game can offer fun characters, elements of competition, a budget to be invested 

A. Poplin and K. Vemuri 

74 

in projects, or just the possibility to build a community focused on topics users care about. 

- Game is online and uses geospatial technology: The online accessibility of the game is attractive due to the availability of smart phones owned by many inhabitants of Dharavi. It can also be attractive for many small entrepreneurs due to the flexibility of the time when the game can be used/played 24/7 with internet connection. 

- Option to negotiate integrated in the game: The negotiation mechanisms can provide an opportunity for an exchange of opinions related to the very specific projects suggested by the stakeholders. 

- Negotiation language integrated in the design and implementation of the game: The language enables the users to express their opinions in a more natural way, in the way that feels appropriate in case of conflicting positions. The language expression may be combined with more specific, quantitative measures such as the amount of money that can be invested in a project. 

- Supports collaboration among the players: The collaboration can be achieved in a form of a dialogue in which conflicting parties exchange their opinions. This dialog can be supported by additional facts about the planned project such as the budget available, the land use regulations, and others contributed by the experts in a collaborative discussion with the inhabitants of Dharavi. 

- Disagreements among parties can be resolved by negotiations: The ability to exchange opinions and facts can provide a platform for a serious, fact-oriented discussion in which everybody involved feels appreciated and heard. 

A negotiation game aims to support building and co-creating sustainable cities which may enable everybody involved to express his/her wishes, explore about the possibilities for changes, and learn about the consequences of implementations while co-creating living environment together. 

## **4.4  Serious Digital GeoGame for Negotiations and Consensus Building: YouPlaceIt!** 

Our main goal is to explore possibilities for the design and prototype implementation of an online game that can enable online negotiations and consensus building in urban planning. We implemented a test version of an online gametitled **YouPlaceIt!** . It was implemented by the team at the International Institute of Information Technology. The game is one of a kind; we are not aware of any similar product on the market. It falls into a similar genre presented in **B3-Design Your Marketplace!** game (Poplin 2014), which enables the players to design their own urban space by using different objects such as benches, trees, lights, fountains, etc. By placing these objects in 2D or 3D game space, they can develop their own spaces, just the way they would like them to be in the real-world. 

75 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

## _**4.4.1  Goal of the Game**_ 

The main goal of the game is to enable negotiations about the future use of space and provide the needed transparency for the decision-making process in urban planning. It aims to support the exchange of opinions related to a specific building project expressed by different stakeholders. The stakeholders involved are individuals living in this particular area, builders, contractors, urban planners, and other public officials. The game aims to enable an exchange of player’s/user’s views, opinions, suggestions for changes, and focuses on the negotiation algorithms. Additionally, the goal of the implementation was to create a digital online prototype of the game; a digital platform that allows for testing of the user interface, the gameplay, different scenarios for changes in the environment, and to validate the responses submitted by the players. 

## _**4.4.2  Premise**_ 

The premise of the **YouPlaceIt!** game focuses around a road construction process. Imagine different stakeholders having their self-interest driven utilization ideas on how a certain space/piece of land in a city can be used. They have their own interests where the new road should be constructed, how much money should be invested into this particular project, and who will the involved parties be. These ideas can be in conflict or contradiction with the ideas of other stakeholders involved into the gameplay. Stakeholders can invest a selected amount of money into a road construction project; the involved players can respond to that with their evaluations of the worth for this particular investment. Some other players might completely oppose to the project, find it too expensive, or disagree with the proposed location of the road construction project. The players can negotiate the price for buying/selling properties that lay along the planned road. The main idea is to enable an exchange among the players, facilitate negotiations about the monetary value of the building project, and to reach a consensus, a win-win outcome for all involved in the discussion. The gameplay is limited to a road construction project, but can be expanded for other kinds of projects. 

## _**4.4.3  Game Elements**_ 

**Space/Environment** . The space represented in the game can be any space one wishes to visualize as raster data; in this case satellite images. In order to illustrate the complexity of the planning process, we present the aforementioned case study of Dharavi, an area of about 230 hectares (approximately 557 acres) with a contentious urban planning history. Figure 4.2 shows the area on a satellite image zoomed in from Google maps in a 2D representation. 

76 

A. Poplin and K. Vemuri 

**Players** . Presently a two-player game is implemented; in the future we intend to implement a multi-player game. One of the players can take on the role of a local community representative who can tag the sites as residential, religious structures, playgrounds, hospitals, or schools. With tagging, the player can identify the main buildings in the area. The player can also enter the expected sale price per sq meter and the margin for negotiation around which the discussions and negotiations evolve. The second player can take on the role of a road developer, which in this case could be a government agency or a contractor entrusted with the construction. We envision the game to be played by the actual inhabitants and the government agencies entrusted with the road development. These players possess the local knowledge required to be able to play the game. 

**Objects** . The current version of the game focuses on road objects and the possibility to tag the objects, to build new roads, and renovate/change the existing roads. The objects representing the properties are also included in the game. These objects can be tagged by color-coded pins classified as either government (hospitals, schools, or parks), non-governmental (places of worship), or private (houses or shops). The color codes for each categories of property in this version are as follows: NGO property use (pink tag), government property (green tag), and private property (blue tag). The road object can be visualized on the satellite image. In addition, there are other objects that represent various categories of existing urban structures which cannot be moved, demolished, or tagged by the player playing the local community representative. An additional object includes a drop-box for selecting the property for negotiation, input the price, and a chat-box for informal discussions. 

**Resources** . Current resources in the game are money and space. Money is limited by the budget available to the players in their negotiation process. The game starts with this budget suggested by a player. The suggested budget can be allocated to the cost of building a newly suggested road. Space is limited by the ability to build the road in certain areas, but not in others. 

## _**4.4.4  Gameplay**_ 

The game starts with the road developer indicating the available budget for the road construction project. Figure 4.4 shows the user interface for inserting the initial suggested budget. The initial budget is not limited by any means; the player can insert any number he/she finds reasonable for the planned project. The player taking the role of the road planning agency can suggest a new road to be built by selecting the path of the road on the satellite image. The suggested road construction can be changed or deleted later in the process of finding the optimal route for the new road. 

Figure 4.5 presents the pop-up box that enables to insert the shape of the buffer zone, name of the property and type (hospital, temple, or school), radial distance (only if the shape selected is a circle), the selling rate per square meter, and the negotiation margin. The negotiation margin can be inserted in percentage. For each 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

77 

**Fig. 4.4** User interface for inserting the allocated budget for constructing the new road 

**Fig. 4.5** The pop-up text box that enables basic input 

of the property types, a perimeter/radial distance is specified as a buffer zone, which ensures that a road is not constructed too close to the buildings such as hospitals, schools, or religious structures. A per square meter price of the land for acquisition is also specified plus the negotiation margin in percentage. 

The road planner can indicate the tagged area on which he/she would like to build a road (Fig. 4.6). The player can than draw a path connecting two points indicating the proposed road position by selecting the ‘draw path’ option on the menu bar. Considering that the area is densely populated, the road can be constructed only 

A. Poplin and K. Vemuri 

78 

**Fig. 4.6** Places identified as different types of properties 

after the property has been acquired. The player taking on the role of a the local community representative can label buildings and open spaces like parks and places of worship on the satellite image. Each of the properties can be owned/represented by a non-governmental agency (temples, hospitals, or schools), a private owner (residential, hospitals, or schools) or a government owned property (schools, hospitals, power stations, water distribution control centers, etc.). The color code for each categories of property are: NGO property use (pink tag), government property (green tag), and private property (blue tag). Figure 4.6 shows the places identified as NGO property, government property, and private property. The patch in red is the buffer zone marked by the player around the property. 

Figure 4.7 shows a set of tags selected over the Dharavi area where three large government properties are tagged. At the end of the tagging and selection process, the major properties in the indicated area are tagged, and a table with the inputs on price is generated and a buffer-zone area is created for further calculations. 

To mark the buffer zone around the property, a rectangle or circular region of interest can be drawn. A rectangular shape with latitude/longitude coordinates or a radius in meters for a circular shape can be selected. A drawing tool is provided for a player to trace the path of the planned road. An algorithm to calculate the cost for land acquisition based on the property prices can be run by selecting the ‘process path’ toolbar button. The total cost of all acquisitions can be viewed by selecting the ‘construction cost’ button. A pop-up displays the acquisition cost, the initial budget outlay and the number of negotiations remaining (Fig. 4.8). 

The green tags on Fig. 4.8 indicate two government properties close to or on the pathway and the red patch represents the buffer zone. In order to be able to acquire these properties, the budget required for the transaction is displayed by selecting the 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

79 

**Fig. 4.7** Six governmental properties are tagged 

**Fig. 4.8** The proposed road path shown as a black line with red/yellow intermediary markers 

A. Poplin and K. Vemuri 

80 

**Fig. 4.9** The proposed alternate road segments are displayed as ‘white’ markers 

‘construction cost’ button. The ‘construction cost’ button appears as a pop-up text box on the top right corner. The road planner is given two options. The first option: No negotiation—that is, consider the optimal path generated by the system. This can be done by selecting the ‘safe path’ button. An equation considers the buffer zone areas input by the other player and suggests localized diversions, that is, small changes in measured in meters or feet from the original path to circumvent the costs or social issues for removing an existing structure like places of worship or a public utility building/space. The construction budget can also be increased by clicking on the ‘increase budget’ button. The second option: Price negotiations can be initiated if the initial pathway is most optimal and localized diversions would lead to future issues, which could be other property owners who have objections or conflicts within government agencies like the waterworks department or utilities department. 

Figure 4.9 shows the alternative paths and displays them as ‘white’ markers. The broad ‘red’ strip is the buffer zone around small residential houses, the ‘black’ line is the path for the road drawn by the road planner, and the ‘green’ tags are labeled properties with their corresponding buffers. Based on buffer parameters provided, the system calculated small detours the path should take to avoid a conflict in land use or price escalation. 

## _**4.4.5  Negotiation and Communication**_ 

**YouPlaceIt!** online digital platform focuses on enabling a dialogue among playing parties involved in negotiations and consensus building processes. The game is designed around the concept of _principled negotiation_ , in which the players are 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

81 

**Fig. 4.10** Negotiation box on the _top right_ and the chat box _below_ for informal messages 

encouraged to close the deal with mutually beneficial financial positions. The negotiation is based on fixed margins suggested by the negotiation parties. The negotiation model is based on the premise that all stakeholders desire a change in present conditions of living and are willing to reach a consensus, which is possible if the players understand the beliefs and optimal decisions the other player will make. In order to enable a free dialogue and text exchange among negotiating parties, we implemented a chat box. The input given by the players can further enable a more complex analysis of the negotiation and consensus building processes. 

Figure 4.10 shows the implemented negotiation box. The negotiation box on the right side of the user interface allows the player to input a price he/she is willing to pay for the property tagged in ‘green’. The price negotiation can start by clicking on the ‘negotiate’ option on the menu bar, which opens a panel on the right-side of the screen. A drop-down box lists the number of properties requiring price negotiations and the road player can select them one at a time and enter a price that he/she is willing to pay. A price as per the market rate and a profit expectation of the community player is calculated from the per square meter cost input which also includes the buffer zone. For example, if the per square meter cost was 100,000 and the buffer area was 50 m[2] than the starting price of this property will be “area × cost-per-sq meter” in this case 5,000,000. If the road planner inputs a price lower than the cost of acquisition of the above property, the new price is calculated from the negotiation percentage provided by the property owner. For example, if the margin was 10%, than the new cost will be calculated as follows: actual_cost × profit margin/100. This new value of the property will be displayed on the right-side window panel. This negotiation process can continue until the road planner agrees on the sale price proposed. 

An informal chatbox is included for the player who tags the properties and for the road planner. It enables them to exchange informal messages in the form of a 

A. Poplin and K. Vemuri 

82 

free text. An analysis of these chats can provide interesting data that can enable a better understanding of the language-based (qualitative) negotiations in addition to the price-based (quantitative) negotiation. 

## **4.5  Testing YouPlaceIt! Game and Reflections About the Implementation** 

The game was developed according to the user-centered design approach placing the user in the center of the development. During the initial prototyping phase it was tested in Utrecht, Hyderabad, and Ames, with internal researchers working on the project. Several revisions were made in the process of **YouPlaceIt!** game development. The second phase of testing was executed in Hyderabad with a limited number of players. 

## _**4.5.1  User Experience Tested with the Selected Players**_ 

A focused testing was executed with two architects and a civil engineering consultant. The number of test players was small, but gave enough feedback for the revision of the game to achieve an improved version of the game prototype. The majority was accomplished in an open interview with the players summarized in this section. 

The two selected architect users/players included a female with 5 years of experience and a male with 10 years of experience in their profession. The civil engineering consultant was a male with 20 years of academic experience and experience in industry consultancy, mostly in construction. All three of them are regularly involved in urban planning activities and processes. They were given access to the online platform **YouPlaceIt!** and the possibility to experiment with it. We  prepared ten questions with yes/no/maybe being possible answers to these questions. The results of this testing are not representative but can indicate certain trends, open up questions for a discussion, and give us directions for our future explorations and research. The questions with their corresponding answers are summarized in Table 4.1. 

From the small set of answers followed up with open discussions about **YouPlaceIt!** communication and negotiation game we can infer that an online tool that allows access to the information, includes options for exploration, and an exchange of opinions is certainly needed. Another positive aspect was the perception of transparency and the feeling of fairness that can be conveyed via such applications. Reflecting upon the use of informal chat-box negotiations, one of the participants noted that deciphering language, especially in cultures like India where every regional language is complex and differs from other regions, might confuse 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

83 

**Table 4.1** Questions with corresponding answers 

||Question|Architect<br>1|Architect<br>2|Civil engineer<br>consultant|
|---|---|---|---|---|
|1|Are you able to understand the aim of<br>the application?|Yes|Yes|Maybe|
|2|Have you played games which have a<br>sole aim of teaching/instructing on a<br>specifc concept? (example: frst-aid<br>methods, fre-evacuation, culture<br>trainingetc.,)|Yes|No|No|
|3|Can public participation in urban<br>planning contribute to a more inclusive<br>development of the city/nation?|Yes|Yes|Yes|
|4|Do you consider online public medium<br>like simulation games as serious/<br>valuable online instruments for the<br>collection of citizen’s opinions,<br>desires?|Yes|Yes|Maybe|
|5|Do you prefer negotiation on real-<br>estate matters by electronic medium?<br>5a. Do you prefer face-to-face<br>negotiation?|Maybe|Yes|No<br>5a. Do you prefer<br>face-to- face negotiation?<br>_Social conditions can be_<br>_better gauged in_<br>_face-to-face. Inclusion_<br>_of video/audio chats._|
|6|Can the process of a property owner<br>(NGO’s, private, government) tagging<br>their property and indicating a sale<br>price lead to transparency in real-estate<br>deals?|Yes|Yes|Maybe|
|7|Is the process of each property owner<br>(NGO’s, private, government) tagging<br>their property and indicating a sale<br>price lead to property owners getting<br>fair deals for thegovernment?|Yes|Yes|Maybe|
|8|From a cultural perspective, do you<br>think a medium such as the one<br>proposed would be considered<br>seriously by government agencies and/<br>or citizens?|Yes|Maybe|Maybe|
|9|Do you think inclusion of informal<br>discussion by chatbox between<br>stakeholders can increase the<br>engagement?|Yes|Yes|No._Consider the_<br>_language used which_<br>_can differ from_<br>_participant to_<br>_participant, sometimes_<br>_the chat cannot be_<br>_moderated, the informal_<br>_chats might confuse_<br>_some stakeholders and_<br>_lead to legal litigations._|
|(continued)|||||



A. Poplin and K. Vemuri 

84 

**Table 4.1** (continued) 

|**Table**|**4.1**(continued)||||
|---|---|---|---|---|
||Question|Architect<br>1|Architect<br>2|Civil engineer<br>consultant|
|10|List the major changes required to<br>make this an acceptable tool? (These<br>should not be suggestions on user-<br>interface or navigation as in the current<br>prototype).|_a. Embed already labeled and tagged property_<br>_information from government agencies and_<br>_citizens._<br>_b. Include other exercises which facilitates_<br>_better coordination between intra-_<br>_governmental agencies—road works,_<br>_telecommunications, water works, etc._<br>_c. Include a moderator of the discussion/_<br>_negotiation_|||



the players and lead to intransparent negotiation processes where several possible languages could be used in one negotiation topic/process. The role of a moderator was discussed; a moderator of the discussion/negotiation could additionally clarify questions and lead the discussion in cases which might not be clear to some of the participants/players. In the later stages of implementation, a discussion and focused attention will be devoted to this suggestion. 

The replies from the participants to locational queries focused on a particular project/topic of interest were evaluated as positive; they can initiate discussions among involved stakeholders and, stored into a digital database, they would be relatively easy to analyse. There was a general consensus among the three testers that validation of the inputs accomplished by the property owners is required which should be provided by a neutral body like a regulator or environmental protection agency. A game is a playful approach that can reach many stakeholders. Due to the serious matter discussed, a validation procedure needs to be included in the process to assure the accuracy of the inserted data. Several additional, more playful  elements may be added to the current concept of the game and may include fun characters, random events, levels, and/or scoring mechanisms. 

In the future we intend to test the game with different user’s groups in an international setting and explore how the game design, game mechanics and user interface influence the gameplay. Testing may lead to further suggestions for the improvements of the game implementation. The implementation as presented here is the first version of the operational online, multi-player geogame which aims to enable negotiations and facilitate consensus building in urban planning projects. We did not come across any similar online application and consider this approach very innovative and one of a kind at the moment. 

## _**4.5.2  Discussion About YouPlaceIt! and Further Research and Implementation Directions**_ 

The communication and negotiation in the **YouPlaceIt!** game is based on the exchange of the price tags and the use of language as a communication tool. A context that is perhaps closer to the one sketched in our game is the one presented in 

85 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

Rusaw, in which the linguistic practices of a community involved in the online game **World of Warcraft (WoW)** are analysed with a special focus on the discourse strategies. The main method of communication in **WoW** is a real-time text chat that is being employed to negotiate the in-game social world. Each player has an access to multiple text chat channels (from temporary to relatively permanent) which range in size from two players to several ones, therefore each player is a member of multiple simultaneous conversations. Such multiple communication channels could be potentially implemented in the **YouPlaceIt!** game in the next version of the prototype. 

Further research of interest is related to the intercultural use of English as a foreign language in communication, often used in negotiations in some countries (examples include India, and also Europe). In India, for example, English is often used as the official language for public communications, in spite of not being a native tongue for many of possible involved negotiators/players. In Zeng and Takatsuka 2009), user chat logs within a virtual world are analysed and the concept of Negotiation for Action is introduced to explain how interaction between native and non-native English speakers allow for language acquisition. In particular, communication tools such as chat and email as well as 3D avatar interaction in a virtual space are employed by intercultural dyads which enable the players to negotiate and solve content related problems in English. Thus interactions involve negotiations related to the meanings, which are exchanged in a collaborative setting. The main goal is concentrated around language learning. This creates several interesting research issues related to the use of language in negotiations, the meaning of different words, and language-based exchange, which can be useful for further development of the **YouPlaceIt!** game. 

The role of power is another interesting research area. Does a game like **YouPlaceIt!** support and empower one group over the other? How is negotiation modeled and implemented? Much of the discourse that takes place among the players in **YouPlaceIt!** focuses on reaching solidarity/consensus within the group involved in order to share their history, knowledge and a sense of belonging. At the same time, the solidarity of the in-group can be used to generate power over the larger number of members that are part of the out-group: power can be thus generated almost entirely by linguistic means. This is reflected also in the chat style where leaders take turns that are usually longer than normal and follow power language more likely to gain influence, expressing a more authoritative role as the information providers. Language is thus more important in this type of online game than in the real world since it is fundamental in the creation of roles and online identities of the players. Further research is needed in order to understand how is language used in **YouPlaceIt!** and whether its implementation might lead to power expressions and overpowering one player or groups of players over others. 

In the future version of **YouPlaceIt!** we intend to enable multilingual chats. Multilingual text and voice chats and icons can be used as a way of communication among players in the process of reaching consensus. This set of qualitative “soft data” can be analysed to assess how the language and a dialog among the players can be employed to better understand social roles and social groups within the 

86 

A. Poplin and K. Vemuri 

game. In particular, we aim at analysing whether the mechanics of the game and the identities of the “real world” have an impact in determining social roles. We plan to investigate whether there are differences and similarities in the language communication within the digital and the physical urban context setting. Language can play an important role in identifying cultural differences between social formations, groups, and individuals. This seems to be the case also for digital games in which social roles are created through language with the support provided by the dynamics of the game, while the physical identities one has in the real world play a marginal role. 

Online consensus building games can be of relevance in assessing whether certain spatial configurations (physical vs. virtual) can support negotiation and consensus finding better than others so that communication and knowledge exchange can be facilitated. It is important to take into account how virtual activities influence new conceptions of physical layouts and the impact that this new vision of the physical space can have on the innovation process. More specifically, it becomes possible to analyze whether there are differences in the nature of the negotiating actions that arise in the physical space vs. the 2D or 3D virtual representation implemented in a digital online game. 

## **4.6  Conclusions** 

This chapter introduces the **YouPlaceIt!** Game, which aims to support negotiations and consensus building in complex urban planning situations. The complexity arises from the variety of different stakeholders involved in the collaborative planning process, the complexity of the spatial issues related to the land use, communication with a variety of educational, income, or nationality backgrounds in the community, and sometimes unsolved/unknown property ownerships. The case study for **YouPlaceIt!** is taken from India and focuses on a very diverse slum area called Dharavi. The complexity of the situation can be additionally increased by the heterogeneous players of the game representing their own interests and visions of how this study area can be revitalized. The game introduced in this chapter is based on the idea that a game, with its playful and experimental environment, can provide a “safe space” in which people/players can experiment with different realities, interventions, and changes in the represented space. In this way they can collectively reflect upon these changes, get involved in negotiations with other players, and with this contribute to the consensus building process. The next prototype of the game may introduce additional playful elements including levels, fun characters, and internal measures of success and building the community which may enable the players to continuously keep on returning to the game. 

Introducing negotiation and the use of language in negotiation is central to **YouPlaceIt!** . The game constitutes the shared space for the negotiation encounter with the 2D representation of the urban planning context on satellite images representing the context of the place to which comments refer to. Text-based chatboxes 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

87 

are used to enable the negotiating activities and dialogues among the involved stakeholders. They set the basis for the emergence of new identities and roles that are created through the language used in negotiations. The channels of communication (i.e. digital game) can influence the shape that the conversational process can take on. The main challenge in this research is to relate the reality of negotiations with a simulated world and modeled algorithms of negotiation. Bringing fun elements into the game and combining them with a more serious situation is an additional inspiration and a challenge at the same time. 

The work presented in this chapter opened up some very interesting research challenges and topics including: the role of language in spatial games and its power in creating coalitions and power relations, the role of negotiations in spatial games and in consensus finding participatory processes, modelling negotiations in spatial games, the issues of serious aspects and how to combine them with playful and experimental elements of the game, the forms and implementations of collective reflections about the urban planning issues and how can they be facilitated by a spatial game, and characteristics of spatial games that can successfully support community planning and civic engagement processes. These questions emerged during discussions about the design and implementation of the **YouPlaceIt!** game. 

In the future we plan on working on these issues and organizing our continuous testing of the latest prototypes of the **YouPlaceIt!** game. We believe that this is just the beginning of our interesting journey, which opens up several very inspiring research challenges, and contributes to creating smart, resilient cities in which everybody can get involved in the co-creation process. 

**Acknowledgments** The authors appreciate and acknowledge Karan Damle and Jayesh Lahori, undergraduate students at the International Institute of Information technology, Hyderabad, India who developed the complete game application. This research would have not been possible without their effort. A special thanks to the local NGO, be the locals, working in Dharavi for giving insights into locals’ perceptions or real-experiences when it comes to development and importantly for articulating the aspirations. The serious game development was partially funded by Department of Information Technology, Govt. of India under the National Program on Perception Engineering project Phase II, where the second author of this chapter is a principal investigator. Thank you to Brandon Klein, Iowa State University, for the language improvements of this text. 

## **References** 

Abt CC (1970) Serious games. University Press of America, New York 

Ahlqvist O (2011) Converging themes in cartography and computer games. Cartogr Geogr Inf Sci 38(3):278–285 

> Ahlqvist O, Ramanathan J, Loffing T, Kocher A (2012) Geospatial human-environment simulation through integration of massive multiplayer online games and geographic information systems. Trans GIS 16(3):331–350 

Al-Kodmany K (2001) Online tools for public participation. Gov Inf Q 18:329–341 

Arputham J, Patel S (2010) Recent developments in plans for Dharavi and for the airport slums in Mumbai. Environ Urban 22(2):501–504 

Basedow S, Pundt H (2001) Braucht bürgerbeteiligung in der planung GIS-funktionalitäten?, CORP conference, Vienna, Austria 

A. Poplin and K. Vemuri 

88 

Brooks MP (2002) Planning theory for practitioners. Planners Press, Chicago, IL 

- Carver S (2001) The future of participatory approaches using geographic information: develop- 

   - ing a research agenda for the 21st century. ESF-NSF meeting on access and participatory approaches in using geographic information, Spoleto, Italy 

- Clark HH, Brennan SE (1991) Grounding in Communication Excerpt: from Perspectives on Socially shared Cognition, Resnick LB, Levine JM, Teasley SD (eds) American Psychological Association, p. 127–149 

- Craig WJ, Harris TM, Weiner D (2002) Community participation and geographic information systems. Taylor and Francis, London 

- Camerer CF, Ho TH, Chong JK (2004) A cognitive hierarchy model of games. Q J Econ 119(3):861–898 

- Chandan V (2014) Dharavi: not a slum, but Asia’s largest small-scale industry, Web. http:// www.thealternative.in/society/photo-story-dharavi-not-a-slum-but-asias-largest-small-scaleindustry/, 22 Jan 2014. Accessed 8 March 2016 

- Costa-Gomes M, Crawford VP, Broseta B (2001) Cognition and behavior in normal-form games: an experimental study. Econometrica 69(5):1193–1235 

- Devisch O (2011) Sollten Stadtplaner Computerspielespielen? In: Bauwelt 24.11, Hasselt. p 26–30 

- Donohue WA, Dies ME, Hamilton M (1984) Coding naturalistic negotiation interaction, Human Communication Research 10(3):403–425 

- DRA n.a. Dharavi redevelopment agency, Web. www.sra.gov.in/pgeDharaviUpcoming.aspx. Accessed 22 Feb 2016 

- Fant LM (1992) Analyzing negotiation talk – authentic data vs. role play in A. Grindsted A, Wagner J (eds) Communication for Specific Purposes, Tuebingen, Gunter Narr Verlag, p 164–175 

- Fisher R (1991) Negotiating power: getting and using influence. In: William Breslin J, Rubin JZ (eds) Negotiation theory and practice. Program on Negotiation Books, Cambridge, pp 127– 140. 128 

- Fischer F (2006) Participatory governance as deliberative empowerment: the cultural politics of discursive space. Am Rev Public Admin 36(1):19–40 

- Gee JP (2004) Situated language and learning: a critique of traditional schooling. Routledge, London 

- Gee JP (2005) Why video games are good for your soul: pleasure and learning. Common Ground, Melbourne 

- Georgiadou Y, Stoter J (2010) Studying the use of geoinformation in government—a conceptual framework. Comput Environ Urban Syst 34(1):70–78 

- E, Manosevitch E (2010) Augmented deliberation: merging physical and virtual interaction to engage communities in urban planning. New Media Soc 13(1):75–95 

- Innes J (1995) Planning theory’s emerging paradigm: communicative action and practice. J Plann Educ Res 14(3):183–189 

- Innes J (1996) Planning through consensus building: a new view of the comprehensive planning ideal. J Am Plann Assoc 62(4):460–472 

- Innes JE, Booher DE (2002) Collaborative planning as capacity building: changing the paradigm of governance. Paper prepared for the Association of European Schools of Planning Conference 

- Jankowski P, Nyerges T (2001) Geographic information systems for group decision making. Taylor and Francis, London 

- Kardan K (2006) Computer role-playing games as a vehicle for teaching history, culture and language. Sandbox Symposium Proceedings, July. Boston, MA 

- Kingston R, Carver S, Evans A, Turton I (2000) Web-based public participation geographical information systems: an aid to local environmental decision-making. Comput Environ Urban Syst 24:109–125 

- Lemke JL (1998) Metamedia literacy: transforming meanings and media. In: Reinking D, Labbo L, McKenna M, Kiefer R (eds) Handbook of literacy and technology: transformations in a posttypographic world. Lawrence Erlbaum Associates, Hillsdale, NJ, pp 283–301 

4 Spatial Game for Negotiations and Consensus Building in Urban Planning… 

89 

- Mehta M (2010) Dharavi redevelopment project. World conference—India, remaking sustainable cities in the vertical age, CTBUH 2010 conference, Mumbai, India, February 2010, presentation slides 

- McKelvey RD, Palfrey TR (1995) Quantal response equilibria for normal form games. Games Econ Behav 10(1):6–38 

- Nagel R (1995) Unraveling in guessing games: an experimental study. Am Econ Rev 85(5):1313–1326 

- Naquin CE, Kurtzberg TR, Belkin LY (2010) The finer points of lying online: E-mail versus pen and paper. Journal of Applied Psychology 95:387–394 

- NSDO n.a. National slum dwellers organization, Web. www.sdinet.org. Accessed 13 Jan 2016 

- Pickles J (1995) Representations in an electronic age: geography, GIS, and democracy. In: Pickles J (ed) Ground truth: the social implications of geographic information systems. Guilford Press, New York, pp 1–30 

- Poplin A (2015) How user-friendly are online interactive maps? Survey based on experiments with heterogeneous users. Cartogr Geogr Inf Sci 42(4):358–376. https://doi.org/10.1080/15230406. 2014.991427. Taylor & Francis, ISSN: 1545-0465 

- Poplin A (2014) Digital serious game for urban planning: B3—design your marketplace! Environ Plann B Plann Des 41(3):493–511 

- Poplin A (2012a) Web-based PPGIS for Wilhelmsburg, Germany: an integration of interactive GIS-based maps with an online questionnaire. Special Issue J Urban Regional Inf Syst Assoc (URISA) 25(2):71–84 

- Poplin A (2012b) Playful public participation in urban planning: a case study for online serious games. Comput Environ Urban Syst (CEUS) 36(3):195–206. Elsevier, Web. http://www.sciencedirect.com/science/article/pii/S0198971511001116 

- Putnam LL, Jones TS (1982) The Role of Communication in Bargaining, Human Communication Research 8(3):262–280 

- Rinner C (1999) Argumentation maps—GIS-based discussion support for online planning. GMD research series No. 22. GMD German National Research Center for Information Technology, Sankt Augustin, Germany 

- Rinner C (2001) Argumentation maps—GIS-based discussion support for online planning. Environ Plann B Plann Des 28(6):847–863 

- Rinner C (2005) Computer support for discussions in spatial planning. In: Campagna M (ed) GIS for sustainable development. Taylor and Francis, London, pp 16–80 

- Rinner C (2006) Argumentation mapping in collaborative spatial decision making. In: Balram S, Dragicevic S (eds) Collaborative geographic information systems. Idea Group, Hershey, PA, pp 85–102 

- Ritterfeld U, Cody M, Vorderer P (eds) (2009) Serious games: mechanisms and effects. Routledge, New York 

- Roseland M (2005) Toward sustainable communities: resources for citizens and their governments. New Society Publishers, Gabriola Island, Canada 

- Schlossberg M, Shuford E (2005) Delineating “Public” and “Participation” in PP GIS. URISA Journal 16(2):16–26 

- Schlieder C, Kiefer P, Matyas S (2006) Geogames—designing location-based games from classic board games. IEEE Intell Syst 21(5):40–46 

- Schroeder P (1996) Report on Public Participation GIS Workshop, NCGIA Technical Report 96–97, Scientific Report for Initiative 19 Specialist Meeting 

- Sieber R (2006) Public participation geographic information systems: a literature review and framework. Ann Assoc Am Geogr 96(3):491–507 

- Sokolova M, Lapalme G (2012) How much do we say? Using informativeness of negotiation text records for early prediction of negotiation outcomes, Group Decision and Negotiation, Springer Netherlands, p. 363–379 

A. Poplin and K. Vemuri 

90 

Steinmann R, Krek A, Blaschke T (2004) Can online map-based applications improve citizen participation? Lecture notes in computer science, TED on e-government 2004. Springer Verlag, Bozen, Italy 

Thompson MM (2000) GIS technology and data sharing, planning into the next millennium. Cornell J Plann Urban Issues 15:20–33 

Zeng G, Takatsuka S (2009) Text-based peer–peer collaborative dialogue in acomputer-mediated learning environment in the EFL context, System 37, p. 434–446, Elsevier, Ltd.
