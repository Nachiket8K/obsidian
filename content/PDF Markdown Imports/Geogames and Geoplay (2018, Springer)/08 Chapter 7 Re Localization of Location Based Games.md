---
title: "Chapter 7 (Re-)Localization of Location-Based Games"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 7 (Re-)Localization of Location-Based Games** 

## **Simon Scheider and Peter Kiefer** 

## **7.1  Introduction** 

Location-based games (LBGs) involve movement in and large-scale interaction with _environmental space_ (Nicklas et al. 2001; Schlieder et al. 2006), which is the space larger than the body which cannot be comprehended without considerable locomotion (Montello 1993). They form an important subclass of _mixed reality games_ , i.e., computer games played in a physical environment which add novel dimensions to the game experience, including seamless _immersion_ of players, new kinds of _social interaction_ with other players, as well as _physical interaction_ with the environment (Hinske et al. 2007). The main advantage of such games is that physical and social experiences are most authentic in a concrete physical or social environment, while the virtual layer of mixed reality adds unprecedented forms of imagination to these environments. In _pervasive games_ , the virtual, social, and physical environments are interconnected based on weaving computing power and sensors into the environmental fabric, and based on the fact that players constantly carry mobile devices (Hinske et al. 2007; Benford et al. 2005; Walther 2005). We regard LBGs as a particular subclass of _geogames_ , i.e., games played in geographic space (Schlieder et al. 2006). The latter, however, include also online games that make use of geographical information without any physical interaction of players (Ahlqvist et al. 2012). 

S. Scheider 

Institute of Cartography and Geoinformation, ETH Zurich, Zurich, Switzerland 

Department of Human Geography and Spatial Planning, University Utrecht, Utrecht, Netherlands 

P. Kiefer ( * ) Institute of Cartography and Geoinformation, ETH Zurich, Zurich, Switzerland e-mail: pekiefer@ethz.ch 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_7 

131 

S. Scheider and P. Kiefer 

132 

While LBGs have been around for some time (Nicklas et al. 2001), only few of them have succeeded in attracting a larger number of players. One reason is the difficulty of embedding game concepts in an environment. In order to reach players from different places and in order to allow for flexibility in taking gaming opportunities, LBG concepts need to be easily re-localized in a way which preserves the particular attractiveness of a game. Furthermore, turning successful virtual reality games played on a computer, or massive multiplayer online games (Ahlqvist et al. 2012), into a LBG requires localization, i.e., the suitable embedding of virtual game concepts into a physical environment. All these tasks still pose considerable conceptual and computational challenges, even though some effort has been made to tackle them (Schlieder et al. 2006; Kiefer et al. 2007; Hajarnis et al. 2011; Schlieder 2014). Furthermore, it recently has become popular to use game concepts in non-game contexts for persuasive computing (gamification) (Deterding et al. 2011; Scheider et al. 2015). Here, too, the successful embedding of elements of games and play into an environment constitutes a considerable challenge for designers (Hassenzahl and Laschke 2015). 

In general, we can distinguish three research challenges on the way towards really flexible location-based gaming: 

1. How can (arbitrary) games be localized? 

   - ( _Game_ → _Game_ + _Env_ ) 

2. How can location-based games be re-localized? 

   - ( _Game_ + _Env_ 1 → _Game_ + _Env_ 2) 

3. How can environments be gamified? 

   - ( _Env_ → _Game_ + _Env_ ) 

In order to provide answers to these questions, and to facilitate corresponding game localization technology, it is necessary to develop _computational quality criteria for the embedding of games in an environment_ . While this problem has partly been recognized in the literature (Schlieder 2014), a systematic derivation of criteria which take into account a game’s ludic dimension, the game narrative, as well as the activity-based embedding into an environment, is still missing. 

In this chapter, we discuss the problem of game localization in the light of recent game literature and environmental and psychological models of space (Sect. 7.2). Based on this, we propose a layered (3-tier) model of game localization (Sect. 7.3) which provides a way of addressing all three questions introduced above. We use this model to suggest some novel quality criteria (Sect. 7.4) for games which particularly reflect their environmental embedding and are based on state transition graphs. We illustrate our criteria with a hypothetical conquer game that has a very simple state transition graph (Sect. 7.5), and discuss its application to an existing LBG (Sect. 7.6). We conclude the chapter in Sect. 7.7 by discussing in how far our method provides answers to the research questions posed above, and what still needs to be done. 

7 (Re-)Localization of Location-Based Games 

133 

## **7.2  Location-Based Game Concepts and Related Work** 

Games consist of different conceptual elements which deploy a game in environmental space. These elements determine its quality, and thus need to be taken into account in game localization. 

## _**7.2.1  Games and Play**_ 

The element of _play_ refers to a kind of embodied activity which is shared and involves social roles, and which is deeply rooted in human biology (Stenros 2015). Play ranges from foundational forms of hiding and chasing to sophisticated forms of role play in a theater. The main characteristic of play is that involved objects and agents can play roles different from what they are supposed to be (outside play), and that the rules which guide play are not explicit, fixed and shared (Stenros 2015), i.e., they are not institutionalized facts (Searle 1995). Games, in contrast, can be seen as an institutionalized (codified) form of play (Stenros 2015), where (collective) intentionality presupposes that players stick to certain rules and follow pre-defined goals. Play accounts to a large extent for the experience of _immersion_ and _flow_ in a game (Hinske et al. 2007), where large parts are probably not made explicit or happen on a subconscious level. The explicit restrictions and rules that come with a game sometimes can even destroy a _playful experience_ , partly because breaking and redefining the rules is an intrinsic part of play (Stenros 2015). Still, a game retains an essential part of the play experience in the form of activities and roles which allow players to connect a game to meaningful places, scripts and narratives in the environment. We therefore hold that play is an intrinsic part of localizing games. 

## _**7.2.2  Scripts and Narratives in Games**_ 

In classic game research, there is a debate between ludologists, who investigate games in terms of game mechanics, referring primarily to their rules and winning strategies and sometimes denying the relevance of narratives in games, and narratologists, who see games primarily as a form of interactive story telling (Jenkins 2004). While games admittedly work in a different way than _plots_ in cinema or fiction, in the sense that the story is not told linearly and is not (entirely) in the hands of the game designer, narratives do play an essential role in game localization (Paay et al. 2008). The reason is that in LBGs, players often understand the environment in terms of a narrative, and thereby project the game onto the environment. This narrative has _a non-linear spatial form_ (Jenkins 2004), based on roles for things distributed in space that can be accessed by a player. In this way, games can evoke collectively known stories, such as pirate stories in a Disney amusement park. 

S. Scheider and P. Kiefer 

134 

Furthermore, players can push a story forward by movement in space (e.g., when a story unfolds through space, as in Bichard et al. (2006)), by revealing background stories (e.g., the murder in a classical detective game), or by constructing emergent stories on their own as in a game like **The Sims** (cf. Jenkins 2004), and through this they are able to break the linear narrative. For example, in backseat games (Bichard et al. 2006), where players move through an environment in the backseat of a car listening to a detective story that plays in their surroundings, the background story can be actively pushed forward at certain locations in that environment. Even though some games may not involve an elaborate linear plot, we suggest that game localization is always a matter of the design of a _spatial narrative_ (Jenkins 2004), where either some roles or some points in the story are fixed to locations, objects or activities in environmental space. In some cases, stories may be reduced to a minimal form, such as a _script_ (a stereotyped sequence of events) or a _frame_ (a stereotyped situation) in cognitive linguistics (Petruck 1996). In these cases, roles may be almost unrecognizable and remain manifest only in the names of figures, such as the queen game piece in chess. 

## _**7.2.3  Places and the Meaningful Environment in Games**_ 

LBGs need to control the space in which players act (Lemos 2011). This was first discovered by researchers on pervasive gaming: Benford et al. (2003, 2005) raised the problems of uncertainty, spatial configuration, and temporal orchestration of a pervasive game, which are caused by its embedding in space. Walther (2005) distinguished tangibility space, information space, and accessibility space, where the first is the space of possible interactions with a physical environment, the second is a digital game representation of the first, and the third interfaces the former two. Several authors (de Souza e Silva 2008; Montola 2005) argued that LBGs are performed simultaneously on different virtual, social and physical spaces which extent the “magic circle” of a game to encompass “serious” social life activities, and thus extend cyberspace to _geographic places_ and _objects_ (Lemos 2011). Reid argued that all LBGs have a degree of place-related embedding, which corresponds to the extent to which their narratives specifically relate to existing places instead of only loosely overlapping space (Reid 2008). 

In the age of digital information, space is often reduced to GPS coordinates. Place, in contrast, appears to be a more involved category of Geography (Cresswell 2013), which is closely related to daily activities (Seamon 1979), routine habits as well as narratives (Tuan 1977, 1991). Places shape possible actions (affordances) (Scheider and Janowicz 2014) by their spatial layout, by the people who live there, as well as by convention. In this, they are comparable to Gibson’s meaningful environment (Scheider and Janowicz 2010; Gibson 2013), which is a way to regard an environment in terms of what it affords to animals or humans. For these reasons, mobile technology needs to take existing places into account (Dourish 2006). Designing games such that player interactions closely correspond to affordances of 

135 

7 (Re-)Localization of Location-Based Games 

those places in which they are played increases a player’s immersion and feeling of authenticity, and thus, gives meaning to ludic activities. 

The latter seems, however, an ongoing challenge for game designers. Most pervasive games to date are rather “spatial” than “platial”: they largely consist of chases and hunts (Lemos 2011), and the interaction between space and cyberspace is reduced to tracking unrestricted movement or to arbitrary space division. For example, a game like **Parallel Kingdom**[1] arbitrarily divides geographic space into territory claims, without taking into account the structure of existing places. Another example is **Zombies Run!** ,[2] in which joggers can escape Zombies by running in any direction. In Google’s successful contemporary LBG **Ingress** ,[3] urban landmarks form “portals” which need to be “hacked” and “linked” to generate “control fields”, i.e., spatial triangles under the control of a group of players. However, the choice of landmarks and triangles is arbitrary, and there is no dependency between player actions and geographic places, in particular since actions remain largely virtual.[4] 

## **7.3  A Layered Model of Game Localization** 

While existing models of game localization mostly focus on a game’s codified rules or technical infrastructure for ubiquitous computing, playing a game is always a fabric of roles, concepts and actions on different layers of conceptual abstraction embedded into an environment. Large parts of these layers are often not made explicit or represented in a computer. In fact, one may consider LBGs as primary examples for the mingling of digital and analog computation (MacLennan 2009), in which the human environment takes over important roles in activities not necessarily represented in a digital form. 

## _**7.3.1  Three Conceptual Game Layers**_ 

Following the suggestion of Schlieder (2014), we distinguish the _ludic_ , _narrative_ and _environmental_ layer (see Table 7.1). The ordering of layers in Table 7.1 is important here, since lower ones are assumed to _deploy_ or _implement_ concepts of the upper layers. For example, a building in the environment may play the role of a castle on the narrative layer and be simply a place for resources on the ludic layer. 

> 1 http://www.parallelkingdom.com. 

> 2 https://zombiesrungame.com/. 

> 3 https://www.ingress.com/. 

> 4 This problem has recently led to serious ethical complaints of the German public. Ingress players had erected portals inside the former concentration camp Sachsenhausen in Berlin, cf. http://www. zeit.de/zeit-magazin/leben/2015-07/ingress-smartphone-spiel-google-niantic-labs-kzgedenkstaette. 

136 

S. Scheider and P. Kiefer 

**Table 7.1** The three conceptual layers of a LBG 

|Abstraction level|Abstraction level|Actions|Constraints|Qualitycriteria|
|---|---|---|---|---|
|0|Ludic|Game actions (e.g.<br>re-allocation)|Game rules and<br>mechanics|Game balancing|
|1|Narrative|Play actions (e.g.<br>conquer)|Scripts and story|Authenticity|
|2|Environmental (perception<br>or simulation)|Environmental actions<br>(e.g. movement)|Affordances|Playability,<br>breakability|



The action of walking somewhere on the environmental layer may correspond to an invasion on the narrative layer and an ownership change of a place on the ludic layer. To account for the dependency between layers, a _mapping_ between layers becomes necessary, which is discussed later in this chapter (see Sect. 7.4.1). 

We furthermore assume that layers on higher levels are not reducible to lower levels because each layer adds specific _constraints_ to the game actions, which are not necessarily present on other layers. For example, the ludic layer adds constraints by codified game rules (such as, whether a player is allowed to go to a place), the narrative layer adds constraints concerning scripts and roles in a corresponding narrative (such as, kings need to travel in carriages), while the environmental layer adds constraints concerning what can be done (affordances) in an environment (e.g., reaching a place in a certain time). Each layer thus adds _quality criteria_ for games associated with its constraints and concepts (see last column of Table 7.1). 

In the following sub-sections, we suggest a _state transition model_ for the layers in this hierarchy. This model is the basis for the localization criteria described in Sect. 7.4. 

## _**7.3.2  Ontology of Game States**_ 

During game play, all layers are in a _game state_ . States are described by sets of facts present on a given layer. _Actions and other processes_ can change this state from one to the next. Figure 7.1 gives an overview of a simple game state ontology expressed in OWL.[5] We suggest this game state ontology as a _pattern_ (Gangemi and Presutti 2010), i.e., a minimal ontology required to describe a LBG on the ludic layer. Note that more specific classes can be introduced for a specific game, and that narrative and environmental layer will extend this ontology. 

Among the _classes_ of this OWL pattern, we have _Agent_ which denotes the set of things that can act intentionally, and _Player_ as a subclass of Agent which encompasses all agents that participate in a game. _Object_ denotes the set of things that are neither agents, places nor locations. _Place_ and _Location_ localize games and need to be distinguished in order to cope with both discrete, cognitively meaningful space 

> 5 http://www.w3.org/TR/owl-features/. This is the “Web Ontology Language”, a W3C recommendation for describing Web information with ontologies. 

7 (Re-)Localization of Location-Based Games 

137 

**Fig. 7.1** An OWL ontology of the classes and properties used to describe the state of a LBG 

(such as cities and market places), as well as continuously measurable space (e.g., in terms of GPS coordinates in a spatial reference system). 

Among the _properties_ (denoting binary relations), we distinguish _owns_ , which denotes an agent’s ownership of some object or place, _has_ , which denotes that an agent carries some object, _at-place_ , which denotes that agents or objects are located at some place, and _at-loc_ , which denotes that agents, objects or places are located in some coordinate region (which may also be a single point). The union of the latter two properties is simply called _at_ . The distinction of ownership and possession can be important but may be irrelevant for a particular game. We also introduce properties which assign attribute values ( _qualities_ ) to objects, places, and players. These can be used to model all kinds of unary states, including also states denoting events. For example, the fact that an agent knows something relevant for the game can be modeled as a quality[6] . Furthermore, we distinguish a single property _socialrel_ among players which denotes possibly diverse social relations between them, such as that they belong to the same group, are at war, or that one player is superior to another player. 

## _**7.3.3  Game Processes as State Transitions**_ 

Game processes are modelled as state transitions, i.e., operations which trigger _changes of the sets_ denoted by the properties and classes of the state ontology on the respective layer. Note that game states may change with and without player actions involved. In principle, one can therefore distinguish two kinds of processes which 

> 6 Knowledge is modeled here simply as a particular state, without taking into account any more sophisticated (modal) logic. 

S. Scheider and P. Kiefer 

138 

can change the state of a game: a _game simulation_ and a _game sensing_ . A game simulation is a player-independent computer simulated process. For example, at a certain point in the game, a sequence of changes can be triggered to enforce a linear storyline, or there may be a random generator that enforces changes to a game’s state, similar to throwing a dice. Game sensors, in contrast, detect changes in qualities or states of the perceived environment which cannot be influenced by the computer, such as whether some object moves around, detected by positioning technology. In the following, we do not further distinguish between these two kinds of processes. 

We use another ontological hierarchy for describing kinds of state transitions. In the following notation, the subsumption operator ⊑ denotes the “ _subClassOf_ ” relation between _state transition classes_ . Note that _individual_ state transitions form the _edges_ of a state transition graph, whereas state transition classes form the _labels_ of these edges (see Sect. 7.4.2). Actions, whether performed by players or not, are the most important kinds of state transitions in games: 

**==> picture [99 x 9] intentionally omitted <==**

When an agent decides to perform an action, this—in essence—changes at least one of the sets which describe a game’s state. We can specify an action type therefore by the sets it is supposed to modify, using the symbol ∷→[7] : 

**==> picture [139 x 75] intentionally omitted <==**

**==> picture [153 x 31] intentionally omitted <==**

We distinguish ownership change from reallocation (take, put), since ownership change is possible without any location change. Movement, in contrast to reallocation, denotes only movement of players. Learning something means that some agent gets to know something. 

> 7 This is an informal notation, which illustrates the usage. A formal notation would make use of corresponding transition rules, see below. 

7 (Re-)Localization of Location-Based Games 

139 

## _**7.3.4  Ludic Layer**_ 

On the ludic layer, a game has a set of codified (shared and institutionalized) rules, i.e., the _rules of a game_ , which constrain player actions that modify a game’s state. Ludic game states are modelled therefore in the simplest possible form sufficient to describe such ludic constraints. 

The rules of a game are specific to a game, and thus cannot be specified in general. Codifying a game’s ludic rules can be done in terms of _inference rules_ , denoted by ⇒, specifying the conditions for actions (in the rule body) as well as their outcomes (in the rule head). For example, the action type _take_ can be defined as follows: 

_take_ : _Object_ ( _x_ ), _Agent_ ( _a_ ), _at_ ( _x_ , _p_ ), _at_ ( _a_ , _p_ ), ℜ _has_ ( _a_ , _x_ ) 

**==> picture [93 x 10] intentionally omitted <==**

We assume that all ludic player actions are made explicit, since otherwise, it is not possible to compute a _state transition graph_ on the ludic layer, i.e., a graph which explores action possibilities in an exhaustive form. 

Besides the rules of a game, the ludic layer also qualifies particular states of a game, namely _starts_ and _goals_ , based on corresponding _start and win conditions_ . For each player, game states are evaluated according to a win condition. For example, the goals of some games are based on a score of ownership, such as Monopoly, while others are based on a geometric state condition, such as checkmate in chess. 

## _**7.3.5  Game Narrative**_ 

On the narrative layer, _classes_ and _properties_ are added to the ontology which embed a game state into a certain narrative or script. For example, a fantasy game may add the following subclasses and properties to the game state ontology: 

**==> picture [82 x 76] intentionally omitted <==**

This specifies that, in this example, three different kinds of agents participate in the game, and that there is a particular type of social relation _superior_ , which denotes whether somebody was superior in a fight. 

S. Scheider and P. Kiefer 

140 

Also new state transitions (including player actions) can be added which are specific to this narrative, e.g. 

**==> picture [53 x 31] intentionally omitted <==**

**==> picture [151 x 10] intentionally omitted <==**

**==> picture [99 x 10] intentionally omitted <==**

Similar to the ludic rules above, on the narrative layer these actions may be further constrained. For example, in our fantasy play, players may be able to ask somebody only if the other Agent is spatially present. Furthermore, one may only be able to conquer something from somebody if the superior relation holds, e.g., as a result of an attack action. Note that narrative constraints may not be necessary for playing the game on the ludic layer, but still add a sense of authenticity and can account for large parts of the play aspect of a game. In this chapter, we treat narrative constraints as (non-codified) rules in a similar way as ludic constraints.[8] 

In a classical computer game, almost all game actions and states on higher layers map into virtual actions and states in an environmental simulation of the game, including virtual layouts visible on the computer screen. The only kind of physical action involved may be joystick manipulation and screen interaction. In a LBG, many actions translate into physical movement or manipulation of objects in the perceived human environment. The degree to which this is the case determines the degree to which a game is a _location-based_ , and thus determines its spatial scope. 

The constraints on the layer of environmental perception are usually not made explicit on a computer. Actually, they are given by _environmental affordances_ , and thus are implicit in the relation between objects and environment (Gibson 2013). 

## _**7.3.6  Environmental Perception and Simulation**_ 

The environmental layer is the level of direct _player interaction_ with a game, i.e., of interactions between physical and virtual entities through appropriate sensory interfaces. The _perceived environment grounds_ the upper layers (c.f. Scheider 2012), i.e., it serves as spatial anchor for the game abstraction hierarchy. It contains objects and layouts as well as corresponding affordances and actions, as proposed by Gibson (2013).[9] _Environmental simulation_ , in addition, denotes the computer simulation of the environment in a game. It can contain exactly the same kinds of things as the 

> 8 Whether this strategy is always applicable seems an open question of research: can narratives always be formalized in terms of rules? 

> 9 Environmental perception, as a matter of fact, can be considered a kind of simulation performed by our brains (cf. Hawkins and Blakeslee 2007; Scheider 2012). 

7 (Re-)Localization of Location-Based Games 

141 

perceived environment or further ones, such as ghosts or monsters. Just as the perceived environment, it displays game affordances and thus serves as a gaming interface for player actions. If the two environments are blended over each other, they constitute an augmented reality. 

## **7.4  Game Localization Criteria** 

In essence, game localization criteria are a function of the _particular embedding_ of a layer into lower layers, taking into account the _constraints_ , which exist on each layer. In the following, we discuss localization as embedding and the preservation of consistency under state transitions, define a number of novel criteria based on embeddings, and discuss how these criteria may be measured and computed. 

## _**7.4.1  Game Localization as Embedding**_ 

Localizing a game means to establish mappings between the narrative and the environmental layer, as well as between the narrative and the ludic layer—both, for kinds of state transitions, as well as for those entities, classes and properties (represented as unary and binary relations, respectively) that describe the state of a game (see Fig. 7.2). 

Mappings need to establish identity between layers in a way that still allows for layer-specific modifications of facts. For example, the fact that a knight is located at some forest on the narrative layer may translate into the fact that some player is located at some park on the environmental layer, or the action class horse riding may be translated as tram riding. Furthermore, we require that every fact describing the state of a game on higher layers and every state transition class is translated into lower layers, and thus into the environmental layer. That is, the mapping needs to be _total_ . This is because a game’s state needs to be fully controlled bottom-up by environmental processes, regardless of whether they are triggered by player actions, non-player processes or simulations. We leave open whether mappings are established ad-hoc, i.e., during the playing of a game, or a-priori. 

The main purpose of the mapping is to pinpoint those entities in an environment (or in a narrative) which are supposed to play a role in the game. As depicted in Fig. 7.2, we can identify game-relevant things on each layer in terms of the respective _images_ of the mappings. There may be other things on each layer that do not play a role in a game (e.g., smoking as an action on the environmental layer). Furthermore, we do not require mappings to be _injective_ (one-to-one), because there may be objects of the environment playing several roles in the game, and because there may be several ludic/narrative processes that map to a single process in the environment. For example, both swimming and riding in the narrative might be mapped to walking in the environment, whereas a ruin in the environment could be 

S. Scheider and P. Kiefer 

142 

**Fig. 7.2** The principle of game localization as a mapping of the three sets of game elements: domain entities ( _D_ ), relations (R), and state transitions (Π) between the three layers 

used for two different castles on the narrative layer. We thus propose to map game elements _top-down_ , i.e., from ludic to narrative and from narrative to the environmental layer. 

In summary, we propose that game localization consists of a mapping (refer also to Fig. 7.2): 

**==> picture [155 x 80] intentionally omitted <==**

Here, the index _i_ ∈ {0, 1}, with 0 = ludic, 1 = narrative, 2 = environmental layer, which means that the mapping stops precisely when mapping from the narrative into the environmental layer. The domain and range symbols of these mappings have the following meaning 

**==> picture [148 x 11] intentionally omitted <==**

**==> picture [177 x 11] intentionally omitted <==**

Π _i_ = { _Ti_ 1,…, _Tim_ }:= set of statetransitionclasseson layer _i_ 

7 (Re-)Localization of Location-Based Games 

143 

with _i_ ranging this time over all three layers, and _n_ and _m_ denoting the sizes of corresponding sets. 

## _**7.4.2  Consistency Preservation of Game States Under a Given Localization**_ 

A mapping of a certain game state into lower layers can be _consistent_ or not. We define a consistent mapping as one that preserves states of affairs between layers. This is also called a _homomorphism_ . If the mapping of game states is homomorphic, then it is the case that: 

**==> picture [276 x 11] intentionally omitted <==**

where _a_ to _z_ denote individual things and _Ri j_ the _j_ ‐ th relation on layer _i_ , and _ρi_ , _ιi_ denote mappings as defined above. This _propagates states of affairs_ upwards from the environmental layer to higher layers. For example, if ownership change on the narrative layer is translated as taking some object on the environmental layer, then whenever I have taken an object, a homomorphic mapping would cause me to own that object (Fig. 7.2). 

Since we do not require a localization to be homomorphic, and since state transitions are bounded by _independent constraints_ on each layer, a game state can become inconsistent. Figure 7.3 illustrates two inconsistent states in a state transition graph. The only consistent state is the start (state 1), while the two depicted follower states (states 2 and 2′) are inconsistent: if we map the relation _owns_ on the narrative layer to the spatial relation _at_ on the environmental layer (Fig. 7.3), and if it was excluded by narrative rules that two people can own a castle at the same time, then every time two people move to the ruin which denotes that castle (such as Peter and Bob in Fig. 7.3), the game state becomes inconsistent (state 2). More precisely, players can move on the environmental layer in a way which enforces a state transition on the narrative layer that _breaks the rules_ . We call this possibility of generating an inconsistency in a game _breakability_ . And vice versa, suppose that based on narrative constraints, we compute possible moves of a player, and that one of these possible moves leads a player straight across a wall (such as Bob in Fig. 7.3). Since this move is excluded by affordances on the environmental layer, it leads to a state inconsistent with environmental constraints (state 2′), and thus to a state which is not playable. The non-playable subset of the narrative graph therefore consists of edge 1 and state 2′, and the breakable subset of the environmental graph consists of edge 2 and state 2. 

It is important to understand that these possibilities of independently pushing a game into inconsistent states on different game layers under a given localization is exactly what causes _state transition graphs_ to become _incompatible_ between layers, and thus games to become either increasingly _non-playable_ or _breakable_ . The _nonplayable subset_ of the ludic state transition graph can now be precisely defined: it 

S. Scheider and P. Kiefer 

144 

**Fig. 7.3** Illustration of inconsistent state transition graphs on the narrative ( _upper_ ) and environmental ( _lower_ ) layer, given the rule that no two persons can own a single place 

consists of exactly those edges which do not have a corresponding edge in the environmental state transition graph, and the _breakable subset_ of the environmental state transition graph are exactly those transitions that do not have a corresponding edge in the ludic state transition graph. 

In order to formally capture this idea, we define a couple of functions which homomorphically translate between state transition graphs on different layers: 

**==> picture [309 x 60] intentionally omitted <==**

Here, _πi_ is a mapping between state transition classes on different levels as defined above. State transition graphs have states _sij_ as nodes (compare the squares in Fig. 7.3) and transitions between states as edges (compare edges between squares in Fig. 7.3) which are labelled by a state transition class _Tij_ . An example for such an _i_ edge would be “move(Peter)” in Fig. 7.3. _fedge_ translates such transition edges of a state transition graph into edges on another game level. An edge _e_ 0 = ( _s_ 01, _T_ 01, _s_ 02) of a ludic state transition graph _G_ 0 homomorphically translates to edge _e_ 2 = ( _s_ 21, _T_ 21, _s_ 22) of an environmental state transition graph _G_ 2 if states are mapped _homomorphically_ and _T_ 21 = _π_ 1( _π_ 0 _T_ 01) is a result of translating state transition classes by the 

145 

7 (Re-)Localization of Location-Based Games 

mapping. A homomorphic translation of a state transition graph _Gi_ = ( _Ni_ , _Ei_ , ) therefore can be expressed by: 

**==> picture [136 x 13] intentionally omitted <==**

Note that each node from _Ni_ in this graph denotes a whole game state on layer _i_ , and thus the graph cannot be easily visualized. In order to make state transition graphs more illustrative, we refer to the simple example given in Sect. 7.5, which contains a state transition graph on the ludic level together with possible translations (embeddings) into lower levels. We use these abstract ideas in the following to suggest novel quality criteria for breakability and playability of LBGs. 

## _**7.4.3  Quality Criteria**_ 

How can the constraints on each layer together with a mapping be used to determine quality criteria for localization? 

## **7.4.3.1  Playability and Breakability** 

Ideally, an embedding is such that higher layer constraints (ludic and narrative) are precisely reflected in lower layer constraints (environment). If this is not the case, then either actions foreseen on the ludic and narrative layers are not possible in an environment (non-playability), or it becomes easy in an environment to break the rules of the game (breakability), because actions are possible which are against the rules of the game. 

In order to capture these two qualities, we assume that _the space of state transitions_ can be computed on each layer _independently_ , based on the particular constraints of that layer. We capture these state transitions on each layer with state transition graphs _G_ ( _N_ , _E_ ), where _N_ is the set of graph nodes and _E_ the set of (transition- class labeled) edges between nodes: 

**==> picture [327 x 12] intentionally omitted <==**

**==> picture [329 x 35] intentionally omitted <==**

The set difference[10] between independently determined graphs on a given layer and graphs translated from higher layers is a measure for the quality of an embed- 

> 10 The operator for subtracting a set from another one is \. The set difference of two graphs _G_ 1 = ( _N_ 1, _E_ 1)\ _G_ 2 = ( _N_ 2, _E_ 2) is defined as _N_ 1\ _N_ 2, _E_ 1\ _E_ 2. 

146 

S. Scheider and P. Kiefer 

ding, because it captures all transition possibilities caused by non-compatible constraints. Degrees of _playability_ and _breakability_ with respect to different layers may therefore be defined most easily in terms of the relative size[11] of the following intersections: 

**==> picture [209 x 139] intentionally omitted <==**

However, since graph sizes only insufficiently capture the effect on possible game strategies, it may be more adequate to measure these qualities in terms of _possible paths_ from start to goal in the corresponding state transition graphs. This captures in how far possible _win strategies_ are affected by constraint propagation. Suppose we denote the set of possible paths through a graph _G_ from a start to a goal in _G_ by the function _pathsgoal_ ( _G_ ), then: 

**==> picture [175 x 147] intentionally omitted <==**

11 Denoted by dashes around sets. The size of a graph is defined as its number of edges. 

7 (Re-)Localization of Location-Based Games 

147 

## **7.4.3.2  Authenticity** 

Authenticity describes in how far entities conceptually resemble the entities into which they are mapped. A non-authentic localization, e.g., would map places of a narrative to arbitrary places in an environment, without taking into account whether the place experience fits to the place in the narrative. For example, a medieval game may be playable in New York but the specific localization may not give rise to a very authentic experience. Even in a medieval city center, there may be more or less authentic localizations of a particular game. 

In order to capture authenticity, we need to capture relevant aspects of _place experience_ , such as perceptual similarity (visual, auditory, haptic qualities) and conceptual similarity (such as historical relatedness or taxonomic distance). If we can express these aspects in terms of concepts in our game ontology, then we can use existing _semantic similarity measures_ in order to measure authenticity. For example, Rodriguez and Egenhofer (2004) and Janowicz (2006) proposed elaborated similarity measures for geospatial object classes. A simple kind of similarity ( _sim_ ) between two different entities _e_ 1 _e_ 2 (e.g. two places or two objects) would be to measure the maximum-standardized shortest distance ( _dist_ ) between their classes in the graph of the game ontology ( _O_ ): 

**==> picture [149 x 26] intentionally omitted <==**

Based on such a simple measure or a more elaborate one, authenticity could be defined as an aggregated similarity value: 

**==> picture [137 x 39] intentionally omitted <==**

The aggregation function _agg_ could be, e.g., a weighted sum with weights specific to the kinds of entities. Furthermore, one could also take into account  similarities between ontology classes and properties as well as between corresponding state transitions into account. 

## **7.4.3.3  Game Balancing** 

Another relevant but more ludic quality of any (also non-location-based) multiplayer game is determined by its balancing. An unbalanced game, i.e., a game in which one player has a dominant winning strategy, will be conceived as disappointing for the loosing player, and as not very challenging for the winning player. Previous work by Schlieder et al. on Geogames has pointed out that, due to the temporal duration of the _move_ action, the balancing of a LBG is particularly 

S. Scheider and P. Kiefer 

148 

challenging, since running as fast as possible may easily become a dominant strategy (Schlieder et al. 2006). Though race games (e.g., **Zombies Run!** or **Can You See Me Now** (Benford et al. 2003)) may have their particular charm and motivate their players to go running, they miss the intellectual challenge of reasoning over a state space (Schlieder et al. 2006). 

The spatialization of a LBG, together with the means of transportation available, influences how long it takes to locomote between places. The duration of a _move_ action can only be determined after mapping it down to the environmental layer. Consequently, we identify _game balancing_ as an important criterion of game localization. Tool-supported state-space analyses (Kiefer and Matyas 2005) can help simulate the spatiotemporal dynamics of a game for a given localization, yielding a numeric value that quantifies the degree of balancing. The most likely outcome of the game, as well as the number of actions each player will likely perform until that outcome is reached (given both act rationally), are two possible measures (Schlieder et al. 2006). Note that in games featuring moving (non-player) agents, the spatiotemporal balancing of a game is also influenced (and can be regulated) by the agents’ speed (refer to Kiefer et al. (2005)). In general, it seems that a good balancing strategy in designing LBGs is to prevent action types which require speed from dominating the state space, e.g., by sprinkling strategic thinking actions inside a game via the game rules. We end our discussion on game balancing of LBGs here, because this problem has been extensively treated in previous work. For a game example in which balancing is of particular importance, see Sect. 7.6. 

## **7.5  Relocalizing a Simple Conquer Game** 

To illustrate our quality measures, take, for example, the following simple game. Suppose there is a single player and states are described by the following vocabulary (abbreviations in brackets are used in Fig. 7.4). 

**==> picture [169 x 12] intentionally omitted <==**

**==> picture [86 x 12] intentionally omitted <==**

**==> picture [177 x 37] intentionally omitted <==**

**==> picture [126 x 10] intentionally omitted <==**

The idea of this conquer game on the _ludic layer_ is illustrated by 15 states (generated by according rules) in the state transition graph in Fig. 7.4: in this game, players need to find local information/equipment in an environment in order to conquer a target. At the beginning (dotted arrow on the bottom left), the player is located at 

7 (Re-)Localization of Location-Based Games 

149 

**Fig. 7.4** State transition graph of a simple (single player) conquer game (ludic layer). Nodes denote states, labels in nodes denote facts about the player that are true in this state. Labels of edges denote state transition classes. Players in crossed states lose the game, and there is a single winning state 

_home_ ( _H_ ) and can move to three other places. One of these places is the _target_ that needs to be conquered to win the game. The player can directly _move_ to the target, however, then lacks a resource (an object) necessary to win an _attack_ of an _enemy_ located at that target place, and thus will immediately loose the game (denoted by state _X_ ). The player thus first needs to find out where this object is located by asking a person in another place ( _Info_ ), and once she _knows_ where that object is, she can move to the _Depot_ place, _take_ the object _O_ , move to the target, and win the attack of the enemy with the help of this object. 

## _**7.5.1  Medieval Fantasy Embedding at “Schloss Burg”**_ 

In a medieval fantasy narrative of this game, the roles may be distributed as follows (where the embedding from the ludic level is into notions at equal positions in the following listing): 

**==> picture [164 x 12] intentionally omitted <==**

**==> picture [68 x 12] intentionally omitted <==**

150 

S. Scheider and P. Kiefer 

**==> picture [134 x 15] intentionally omitted <==**

**==> picture [101 x 13] intentionally omitted <==**

**==> picture [123 x 10] intentionally omitted <==**

Now the game tells the story (see Fig. 7.6a) of a wizard who wanders through a village and learns that an evil witch in the nearby castle has enslaved its inhabitants. The wizard promises to free the village from the reign of the witch. The way to the castle inevitably leads through a forest, where the wizard can ask a dwarf, who tells him that the witch put a spell on the castle that prevents people from escaping, and therefore can only be defeated using a magic wand, which is hidden in a cave. The wizard needs to find the wand and enter the castle to keep his promise. Note that under this embedding, all states of the game reappear homomorphically (see Fig. 7.6a), however, some state transitions were removed to streamline the story (e.g., there is no possibility to return to the village after a certain point in the story). 

Suppose we furthermore embed this narrative into the environment of a real castle, such as “Schloss Burg”[12] in Germany (see Fig. 7.5). The role of the village could be played by “ _Unterburg_ ”, which is part of a small town (Burg an der Wupper) located directly at the foot of the hill on top of which the castle is located, the forest could be played by “ _Schlossberg_ ”, the woody hill slope through which a footpath leads to the top, and the cave could be embodied by a _playground_ beneath the castle. The sphere of influence of the castle could involve a narrow buffer or boundary surrounding the castle (compare Fig. 7.5): 

_Places D_ 2 = { _Schlossberg_ , _Playground_ , _SchlossBurg_ , _Unterburg_ } 

**==> picture [151 x 82] intentionally omitted <==**

Note how some of the entities and actions are _virtual_ (the witch, the dwarf and the wand), while others correspond to things in physical reality. 

Note furthermore the state transition differences imposed by _environmental affordances_ (compare Figs. 7.6b and 7.5a): under this embedding, certain direct walks, namely the ones between the “forest” (Schlossberg) and the “cave” (Playground) are not possible anymore, because the footpath (black dotted line in Fig. 7.5a) through the forest inevitably leads to the castle first. Furthermore, a player 

> 12 https://en.wikipedia.org/wiki/Burg_Castle_(Solingen). 

151 

7 (Re-)Localization of Location-Based Games 

**Fig. 7.5** The environment for embedding the medieval narrative. ( **a** ) Places around Schloss Burg. ( **b** ) Schloss Burg a.d. Wupper, Germany (CC BY-SA 2.0 ( `https://creativecommons. org/licenses/by-sa/2.0/` ) courtesy by ''Polybert49'' on Flickr) 

can leave the castle and get to the playground by taking the footpath leading past the castle’s exterior wall. The latter breaks the rules of the game, whereas the former renders the game unplayable under this embedding. To be more precise, Table 7.2 shows the exact numbers for playability and breakability as defined in this chapter together with the underlying graph-based measures regarding the medieval embedding. 

Note that only the path-based measures ( _Q_[′] ) actually reveal that the game is practically unplayable under this embedding ( _playability_ = 0), and that every possible strategy will break the ludic as well as narrative rules of the game ( _breakability_ = 1). Note also that playability and breakability are not simply (1 − _x_ ) of each other. 

## _**7.5.2  Crime Story Embedding in “Little Italy”**_ 

Suppose we embed the medieval fantasy narrative ( _n_ 1 in Table 7.3) into an urban environment, such as the Little Italy district in New York ( _e_ 2 in Table 7.3). For instance, the narrative “Village” would map to “Angelo’s” (an Italian restaurant), the medieval “Forest” to “Ravenite Social Club”, etc. (refer to Table 7.3). The authenticity of this embedding, taking into account ontological differences between classes and properties, should be rather low. 

152 

S. Scheider and P. Kiefer 

**Fig. 7.6** State transition graphs on narrative ( **a** ) and environmental ( **b** ) layers for the medieval fantasy embedding. ( **a** ) State transition graph of the medieval fantasy narrative. ( **b** ) State transition graph of the game environment of Schloss Burg 

153 

7 (Re-)Localization of Location-Based Games 

**Table 7.2** Playability and breakability measures for the medieval embedding 

|||_G_2|||_vG_|||_G_2 ∩ _vG_||Breakability|Playability|
|---|---|---|---|---|---|
|_Q_0|19|31|11|0.421|0.355|
|_Q_1|19|19|13|0.316|0.684|
|_Q_I0|1|20|0|1|0|
|_Q_I1|1|2|0|1|0|



| _G_ 2| = cardinality of state transition graph on environmental layer, | _vG_ | = cardinality of translation from 0/1 layer to environmental layer, | _G_ 2 ∩ _vG_ | cardinality of intersection. Cardinalities are either of edge sets ( _Q_ ) or of sets of start-goal paths ( _Q_[′] ) 

**Table 7.3** Authenticity for two narrative and two environmental embeddings 

|Ludic|Narrative<br>1(n1)|Narrative 2<br>(n2)|Environment<br>1(e1)|Environment<br>2(e2)|Similarities|Similarities|Similarities|
|---|---|---|---|---|---|---|---|
||||||n1,e1|n1,e2|n2,e2|
|Home|Village|Restaurant|Unterburg|Angelo’s|0.75|0.25|1|
|Info|Forest|Nightclub|Schlossberg|Ravenite<br>Social Club|1|0.25|1|
|Depot|Cave|Rife Store|Playground|John Jovino<br>Gun Shop|0.5|0.25|1|
|Target|Castle|Bank|Schloss Burg|CityBank|1|0.5|1|
|_QAuthenticity_<br>1|||||0.8125|0.3125|1|



Figure 7.7 displays a simple ontology of the different types of places, which we can use to measure authenticity. And in fact, based on this ontology, it turns out that the averaged similarity (as defined in Sect. 7.4.3) over all places is 0.31 (see Table 7.3). 

For the New York environment, a different narrative would provide better authenticity values, and thus a better gaming experience. Consider a narrative playing in the times of the Mafia of the 1920s ( _n_ 2 in Table 7.3): the player is member of a Mafia family, seated at some restaurant, and has the goal of robbing a Bank. For this, he needs to move to a nightclub to find out how to get a gun. Some other Mafioso in the nightclub tells him to rob a specific gun shop. This embedding yields an averaged similarity of 1, since all places match places of identical classes (Table 7.3). Note that the original medieval fantasy embedding at Schloss Burg yields also a high authenticity value of 0.81, which is a bit lower than 1 because the playground is not an ideal place for the role of the cave. 

## **7.6  Localization of an Existing Multi-player Game: CityPoker** 

Here we demonstrate how relocalization can be applied to an existing game: **CityPoker** , a multi-player LBG introduced in (Kiefer et al. 2005; Kremer et al. 2013). As for any serious game, its state transition graph is too complex to be 

154 

S. Scheider and P. Kiefer 

**Fig. 7.7** A hierarchy of place types used for measuring authenticity based on semantic similarity 

visualized. We provide a simplified rule description here; the extended rule set can be found in Kiefer et al. (2005). 

In **CityPoker** , two players each aim at improving their hand of five cards by exchanging these with cards hidden in the environment. There are 20 cards in the game ({♣, ♦, ♥, ♠} × {10, J, Q, K, A}), 10 of which are on the players’ hands, and 10 hidden in five caches. Players can exchange at most once at each cache, which means they drop one card and pick another. Figure 7.8 (left) illustrates a possible initial card distribution for Bamberg, Germany, as well as the players’ starting positions. The end evaluation follows that of the traditional Poker game (Royal Flush > Four of a kind _>_ … _>_ One Pair). 

The ludic level contains the following things: 

**==> picture [168 x 106] intentionally omitted <==**

where the mechanics of the game are modeled with a large state graph describing all possible sequences of moving and exchanging cards. There is a trivial bijective mapping from the ludic to the narrative level (similar for state graphs): 

155 

7 (Re-)Localization of Location-Based Games 

**Fig. 7.8** CityPoker with two different narrative and environmental embeddings in Bamberg, Germany ( _left_ : original, _right_ : medieval version; basemap: OpenStreetMap) 

**==> picture [171 x 83] intentionally omitted <==**

**==> picture [125 x 10] intentionally omitted <==**

The localization displayed in Fig. 7.8 (left) yields in the following sets of game elements on the environmental level: 

**==> picture [181 x 106] intentionally omitted <==**

Let us assume our localization allows for locomotion by bicycle between each pair of caches, and the game software ensures that cards can only be exchanged following the ludic rules. In that case, the localization is perfectly playable and not at 

156 

S. Scheider and P. Kiefer 

all breakable. Authenticity, however, is rather weak (none of the selected places is associated with Poker), and a relocalization within Bamberg would not help either: the historical center of Bamberg is characterized by medieval buildings and tourist attractions, not with a single gambling place. 

This can be solved by changing the narrative to a medieval setting, while keeping the ludic rules fixed: the four colors ({♣, ♦, ♥, ♠}) could be replaced by four competing parties that were relevant in medieval times: { _CatholicChurch, Benedictines, Citizens, Peasants_ }. For each party, we could select five professions replacing the Poker numbers, such as { _Abbot, Vice-Abbot, Treasurer, Cellarer, Monk_ } for Benedictines, and { _Major, Vice-Major, Merchant, Blacksmith, Worker_ } for Citizens: 

**==> picture [195 x 16] intentionally omitted <==**

_D_ 1 _Objects_[′] = { _BenedictineAbbot_ , _BenedictineViceAbbot_ ,…, _Citize_ _**n** Worker_ } 

**==> picture [156 x 64] intentionally omitted <==**

In this narrative, players are delegates on some diplomatic mission with the goal of convincing influential people (which are considered items here, not agents). The winning condition is defined in a way consistent with Poker: all from one party > four of the same level > … > two of the same level. It is now possible to find a localization in Bamberg which ensures high authenticity (e.g., Bamberg Cathedral, Michaelsberg monastery, etc.; see Fig. 7.8). Finally, it will most likely be necessary to change the two start positions to keep the game dynamics balanced, which is out of the scope of this chapter. 

## **7.7  Discussion and Conclusion** 

Based on a layered model of game localization, we have suggested novel measures for playability, breakability and authenticity of possible environmental embeddings of a game. Since our approach involves game narratives, it takes into account some of the “play” aspect of games. It also contributes to the challenge of “deep” localization of games, which goes beyond superficial spatialization to consider embedding of games into places and possible actions (affordances). 

Now, one game embedding can be compared with another one in order to determine the optimal one given an environment. This provides a way to answer research questions 1 and 2 of section 1 about localization and re-localization, as it gives us novel and relevant criteria to evaluate possible localizations with respect to narratives, roles and environmental affordances. However, in this chapter, we have not 

7 (Re-)Localization of Location-Based Games 

157 

yet addressed the problem of _searching_ for good or optimal localizations. Based on future research, it might also become possible to search for a game that has the highest quality of embedding into some given environment, addressing question 3 (gamification) of section 1. 

Here are a number of open research questions that need to be addressed in order to reach these goals. 

First, to what extent does our approach really capture meaningfulness and the play aspect of games? In how far could it be used for _meaningful gamification_ of environments? The existing research on meaningful gamification is in a very early stage (Nicholson 2012; Hassenzahl and Laschke 2015), which means it is open what aspects of gaming activity really need to be taken into account. We think our chapter gives some suggestions on what criteria might be relevant. 

Second, our approach requires that state formalizations and state transition graphs are present on all game layers. Which sensors/observations are needed in order to generate state transitions on the environmental layer? How can we formalize state transition constraints on ludic as well as narrative layers? How can we compute state transition graphs given constraints? This can be of different complexity, depending on the nature of these constraints. 

Third, and most importantly, the computation of the localization quality of a given embedding, as well as the search for an optimal embedding given an environment are both computationally complex. Computing playability and breakability in a strategic manner requires computing all start to goal paths in transition graphs on all three layers. Computing authenticity requires similarity computations for each mapped symbol. Searching over the set of possible game localizations given states 

 _n_  on two layers is a combinatoric problem [] _m_ [][ where ] _[n]_[ is the size of the union of ] domain, relation and state transition symbols on one layer and _m_ on the other. However, the latter problem can always be simplified by certain practical considerations, such as a fixed start location of a user, and a restricted relation or state transition mapping. 

## **References** 

Ahlqvist O, Loffing T, Ramanathan J, Kocher A (2012) Geospatial human-environment simulation through integration of massive multiplayer online games and geographic information systems. Trans GIS 16(3):331–350 

> Rodriguez MA, Egenhofer MJ (2004) Comparing geospatial entity classes: an asymmetric and context-dependent similarity measure. Int J Geogr Inf Sci 18(3):229–256 Benford S, Anastasi R, Flintham M, Drozd A, Crabtree A, Greenhalgh C, Tandavanitj N, Adams M, Row-Farr J (2003) Coping with uncertainty in a location-based game. IEEE Pervasive Comput 2(3):34–41 

> Benford S, Magerkurth C, Ljungstrand P (2005) Bridging the physical and digital in pervasive gaming. Commun ACM 48(3):54–57 

> Bichard J, Brunnberg L, Combetto M, Gustafsson A, Juhlin O (2006) Backseat playgrounds: pervasive storytelling in vast location based games. In: Entertainment computing-ICEC 2006, Springer, pp 117–122 

158 

S. Scheider and P. Kiefer 

Cresswell T (2013) Place: a short introduction. Wiley, New York 

Deterding S, Dixon D, Khaled R, Nacke L (2011) From game design elements to gamefulness: defining gamification. In: Proceedings of the 15th international academic MindTrek conference: envisioning future media environments, ACM, pp 9–15 

- Dourish P (2006) Re-space-ing place: place and space ten years on. In: Proceedings of the 2006 20th anniversary conference on computer supported co-operative work, ACM, pp 299–308 

- Gangemi A, Presutti V (2010) Towards a pattern science for the semantic web. Semant Web 1(1-2):61–68 

Gibson JJ (2013) The ecological approach to visual perception. Psychology Press, Boston 

Hajarnis S, Headrick B, Ferguson A, Riedl MO (2011) Scaling mobile alternate reality games with 

geo-location translation. In: Interactive storytelling, Springer, New York, pp 278–283 

Hassenzahl M, Laschke M (2015) Pleasurable troublemakers. The gameful world: approaches, issues, applications. MIT Press, Cambridge, MA, p 167 

- Hawkins J, Blakeslee S (2007) On intelligence. Macmillan, New York 

- Hinske S, Lampe M, Magerkurth C, Röcker C (2007) Classifying pervasive games: on pervasive computing and mixed reality. In: Magerkurth C, Röcker C (eds) Concepts and technologies for pervasive games—a reader for pervasive gaming research, vol 1. Shaker Verlag, Aachen, p 20 

- Janowicz K (2006) Sim-DL: Towards a semantic similarity measurement theory for the description logic ALCNR in geographic information retrieval. In: On the move to meaningful internet systems 2006: OTM 2006 workshops, Springer, pp 1681–1692 

- Jenkins H (2004) Game design as narrative architecture. Computer 44(3):118–130 

- Kiefer P, Matyas S (2005) The geogames tool: balancing spatio-temporal design parameters in location-based games. In: Mehdi Q, Gough N (eds) Proceedings of the 7th international conference on computer games: artificial intelligence, animation, mobile, educational and serious games (CGAMES 2005), Angoulême, France, pp 216–222 

- Kiefer P, Matyas S, Schlieder C (2005) State space analysis as a tool in the design of a smart opponent for a location-based game. In: Masuch M, Hartmann K, Beckhaus S, Spierling U, Sliwka F (eds) Proceedings of the Computer Science and Magic 2005, GC Developer Conference Science Track, Messe Leipzig, Leipzig, Germany, ISBN:3-9804874-3-1 

- Kiefer P, Matyas S, Schlieder C (2007) Playing location-based games on geographically distributed game boards. In: Magerkurth C, Akesson KP, Bernhaupt R, Björk S, Lindt I, Ljungstrand P, Waern A (eds) 4th international sym posium on pervasive gaming applications (PerGames 2007). Shaker Verlag, Aachen, Salzburg, Austria 

- Kremer D, Schlieder C, Feulner B, Ohl U (2013) Spatial choices in an educational geogame. In: Games and virtual worlds for serious applications (VS-GAMES), 2013 5th international conference on, IEEE, pp 1–4 

- Lemos A (2011) Pervasive computer games and processes of spatialization: informational territories and mobile technologies. Can J Commun 36(2):277–294 

- MacLennan B (2009) Analog computation. In: Meyers RA (ed) Encyclopedia of complexity and systems science. Springer, New York, pp 271–294. https://doi.org/10.1007/978-0-387-30440-3 

- Montello DR (1993) Scale and multiple psychologies of space. In: Spatial information theory—a theoretical basis for GIS. Springer, New York, pp 312–321 

- Montola M (2005) Exploring the edge of the magic circle: defining pervasive games. In: Proceedings of DAC, vol 1966, p 103 

- Nicholson S (2012) A user-centered theoretical framework for meaningful gamification. In: Games+Learning+Society 8, Madison, WI 

- Nicklas D, Pfisterer C, Mitschang B (2001) Towards location-based games. In: Proceedings of the international conference on applications and development of computer games in the 21st century: ADCOG, vol 21, pp 61–67 

- Paay J, Kjeldskov J, Christensen A, Ibsen A, Jensen D, Nielsen G, Vutborg R (2008) Locationbased storytelling in the urban environment. In: Proceedings of the 20th Australasian conference on computer-human interaction: designing for habitus and habitat, ACM, pp 122–129 

159 

7 (Re-)Localization of Location-Based Games 

- Petruck MR (1996) Frame semantics. In: Verschueren J, Östman J-O, Blommaert J, Bulcaen C (eds) Handbook of pragmatics. John Benjamins, Philadelphia, pp 1–13 

- Reid J (2008) Design for coincidence: incorporating real world artifacts in location based games. In: Proceedings of the 3rd international conference on digital interactive media in entertainment and arts, ACM, pp 18–25 

- Scheider S (2012) Grounding geographic information in perceptual operations, vol 244. IOS Press, Amsterdam 

- Scheider S, Janowicz K (2010) Places as media of containment. In: Proceedings of the 6th international conference on geographic information science (extended abstract) 

- Scheider S, Janowicz K (2014) Place reference systems: a constructive activity model of reference to places. Appl Ontol 9(2):97–127 

- Scheider S, Kiefer P, Weiser P, Raubal M, Sailer C (2015) Score design for meaningful gamification. In: Researching gamification: strategies, opportunities, challenges, ethics, Workshop at CHI 2015 

- Schlieder C (2014) Geogames—Gestaltungsaufgaben und geoinformatische Lösungsansätze. Informatik-Spektrum 37(6):567–574 

- Schlieder C, Kiefer P, Matyas S (2006) Geogames: designing location-based games from classic board games. IEEE Intell Syst 21(5):40–46 

- Seamon D (1979) A geography of the lifeworld. St. Martin’s Press, New York 

- Searle JR (1995) The construction of social reality. Simon and Schuster, New York 

- de Souza e Silva A (2008) Hybrid reality and location-based gaming: redefining mobility and game spaces in urban environments. Simul Gaming 40(3):404–424 

- Stenros J (2015) Behind games: Playful mindsets and transformative practices. In: Walz SP (ed) The gameful world: approaches, issues, applications. MIT Press, Cambridge, MA, p 201 

- Tuan YF (1977) Space and place: the perspective of experience. University of Minnesota Press, Minneapolis 

- Tuan YF (1991) Language and the making of place: a narrative-descriptive approach. Ann Assoc Am Geogr 81(4):684–696 

- Walther BK (2005) Atomic actions–molecular experience: theory of pervasive gaming. Comput Entertain (CIE) 3(3):4–4
