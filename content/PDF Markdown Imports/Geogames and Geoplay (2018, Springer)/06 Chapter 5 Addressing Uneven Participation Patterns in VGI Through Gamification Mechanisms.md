---
title: "Chapter 5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms** 

## **Vyron Antoniou and Christoph Schlieder** 

## **5.1  Introduction** 

The internet era since the turn of the century has been characterized by the ubiquity of open source, user generated data. The classic example of this “Web 2.0” paradigm is Wikipedia, an enormous, free, user generated encyclopedia. The geospatial domain entered the Web 2.0 era by leveraging user generated _spatial_ content, known as _Volunteered Geographic Information_ (VGI) (Goodchild 2007). Created by neogeographers (Turner 2006), the most successful example so far is OpenStreetMap (OSM). OSM has motivated a constantly growing pool of contributors to create a free map of the world, providing up-to-date Geographic Information (GI) that was previously unavailable (Estes and Mooneyhan 1994; Goodchild 2007). 

While OSM is quickly building a world map from open and freely available data, challenging points in the process have. One of the most discussed issues in the literature is the VGI data quality and fitness-for-purpose, often using OSM data as a paradigm (see for example Haklay et al. 2010; Jackson et al. 2013; Arsanjani et al. 2013; Kalantari and La 2015; Stein et al. 2015). Another closely related issue is that new sources of error and uncertainty related to social phenomena directly affect VGI datasets. These sources of error and uncertainty are fundamentally different from those of traditional authoritative datasets. This is mainly due to the social aspect of the VGI phenomenon and the crowd-based mechanism for data collection (see Antoniou and Skopeliti 2015 for an overview of the social factors that can affect VGI quality and participation patterns). For example, empirical research 

V. Antoniou ( * ) Hellenic Army General Staff/Geographic Directorate, Athens, Greece e-mail: v.anoniou@ucl.ac.uk 

C. Schlieder Faculty of Information Systems and Applied Computer Sciences, University of Bamberg, Kapuzinerstraße 16, 96047 Bamberg, Germany 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_5 

91 

V. Antoniou and C. Schlieder 

92 

results show that contributors are affected by the underlying socioeconomic context of their activity area. There is a strong correlation between the Index of Multiple Deprivation for UK and the OSM completeness (Haklay 2010) and OSM positional accuracy (Antoniou 2011). Similarly, Girres and Touya (2010) note that socioeconomic factors (e.g. high income and low population age) result in a higher number of contributions. Zielstra and Zipf (2010) show that demographic factors such as the low population density areas (i.e. rural areas) have a direct impact on the completeness of VGI data. As the evidence converges on the question of how crowds behave, academic research has shifted focus to theoretical analyses of contributors: their nature, and motivation (Goodchild 2007; Coleman et al. 2009) and their new role in the production (Budhathoki et al. 2008). 

Interestingly enough, the aforementioned observations hold true and similar patterns emerge for other sources of VGI, such as the popular photo-sharing web application of Flickr[1] that provides geo-tagged images. For example, Antoniou et al. (2010) show that by conducting a density analysis of geo-tagged images in Flickr, there are certain areas that attract more contributors than others resulting in the uneven distribution of user contributed data. However, the same type of spatial analysis conducted using the geo-tagged images of Geograph[2] found different results. Geograph is a spatially explicit application that implements a gamification approach to user contributed data, and provides more evenly distributed area coverage despite having fewer photos compared to Flickr (7993 Flickr photos vs. 1109 Geograph photos) (see Fig. 5.1). 

Following this line of research, this chapter investigates the participation patterns of OSM contributors, the results produced, and the resulting impact on spatial data quality. The chapter provides solutions for counter-balancing unwanted effects of participation patterns through geogames. More specifically, in Sect. 5.2 we identify three issues of OSM mapping: (1) high productive contributors show little commitment to return and update geographic features they created, (2) the gap between the accumulated percentage of created features and the accumulated percentage of updated features is widening, (3) there is a significant contrast between areas of high and low mapping activity. Section 5.3 describes spatial allocation games as a subclass of location-based games suitable for addressing the participation issues. Based on an analysis of the geogames **Geograph** , **Foursquare** , **Ingress** , and **Neocartographer** six common design patterns for the allocation and deallocation of places are identified. We also show how the participation issues map onto the game design patterns. Finally, Sect. 5.4 describes the results from an  agent- based spatial simulation that provide insights into the game flow of spatial allocation games. We present a model that distinguishes between a phase of fast and slow gameplay. Game designer should try to avoid the slow phase. The chapter concludes with a discussion of the results and an outlook on questions for future research in Sect. 5.5. 

> 1 www.flickr.com. 

> 2 www.geograph.co.uk. 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

93 

**Fig. 5.1** Density surfaces for ( **a** ) Flickr and ( **b** ) Geograph in a test area of 3 × 5 km in North London. Source: Antoniou et al. (2010) 

## **5.2  The OpenStreetMap Case Study** 

The focus area is the Greater London Area in UK, as the birthplace of OSM is University College London. Moreover, urban areas attract more OSM contributors and thus such areas facilitate the monitoring and the analysis of their digital 

V. Antoniou and C. Schlieder 

94 

**Table 5.1** Descriptive statistics of the dataset 

|OSM data set: Greater London Area, UK|OSM data set: Greater London Area, UK|
|---|---|
|Number of features|438,980|
|Number of unique contributingusers|3230|
|Number of versions|917,000|
|Versionsper feature(average)|2.09|
|Versionsper user(average)|283.9|



behavior. Instead of a direct bulk download from the OSM database, the dataset of the area was downloaded in a shapefile format (by www.geofabrik.de) and then the OSM API was used to collect only the necessary data for the analysis (changesets, timestamps etc.) using the unique osmid of each feature. As in most wiki-based projects, in OSM it is possible to trace back the lineage of each spatial feature and thus monitor all the changes that each feature has undergone from its initial capture up to date. The dataset contains 438,980 features that have in total 917,000 versions, contributed by 3230 OSM contributors that have been active in the area since the beginning of OSM. The descriptive statistics of the dataset are shown in Table 5.1. 

Although descriptive statistics give a basic understanding of the data at hand, they do not shed light to the geographic distribution of the data or to any underlying patterns. Thus, a more thorough analysis of the OSM datasets was conducted aiming to provide answers to the following questions relevant to the participation patterns and biases in OSM. Unwanted participation patterns and biases will be later targeted by the gamification processes so to counter-balance them and thus enable a more balanced volunteered contribution. 

## _**5.2.1  Is There a Commitment Between OSM Contributors and Their Spatial Edits?**_ 

From the early days of VGI, many scholars (see for example Elwood 2008; Goodchild 2008; Heipke 2010) have recognized that one of the most important elements of crowdsourced spatial content is its unique relationship with local knowledge and its ability to capture such information. Indeed, in many crowdsourced projects (see for example Haklay et al. 2010) local knowledge plays a central role. However, when it comes to projects that extend to global scale, despite the numerous contributors that might be involved, the picture is quite different. An analysis of the behavior of the most productive contributors (i.e. those that have contributed more than 100 times) took place in order to examine how committed OSM contributors are to their edits, and thus see if local knowledge is present in such datasets. The results showed that there is limited relationship between contributors and spatial features. In fact, just a mere 10% of these high productive contributors are returning to more than 20% of the features that have created in the past. This observation is creating a fresh line of questions regarding the notion that contributors are bringing 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

95 

along their local knowledge and the importance of this knowledge in the quality of the OSM dataset. 

## _**5.2.2  Is the OSM Dataset Kept Up-to-date by the OSM Contributors?**_ 

From the outset of OSM in 2004, the Greater London Area has been a very active area in terms of data crowdsourcing either through OSM mapping parties (i.e. leisure activities devoted to mapping an area) or through individual contributions. As a result, a highly detailed map of this area was available even from the first years of OSM. However, as more and more spatial features are portrayed in the OSM map, the contributors devote more of their energy to editing existing features than capturing new ones (Fig. 5.2). More specifically, until the second half of 2007 there were more additions of new features than updates of existing ones. However, from that point onwards the contributors focus more on updating OSM feature than creating new ones. This is a seemingly healthy evolution of OSM as in a densely built area the number of new features created is relatively small, while the editing of new ones could theoretically correct existing geometric and attribute errors, provide more detailed description of spatial features and improve the overall spatial data quality. Of course, this assumption holds true only if the editing effort is evenly distributed by OSM contributors to the entire population of spatial features available. In Sect. 5.2.3 we show that an uneven geographic distribution of edits has been observed and thus participation biases emerge. 

Moreover, the examination of the edits’ distribution shows a pattern where most of the features have only few edits while a small part of them gathers a large number of edits. More specifically, almost 66% of the features have up to 10 edits (note that the first edit is the creation of the feature) when at the same time about 12% of the features have more than 100 edits (Fig. 5.3). As explained below, interesting patterns also emerge when examining how up-to-date is the OSM dataset or how participation patterns are affected by the geography of the area. 

**Fig. 5.2** The percentage of the active OSM contributors (out of the 3230 in total recorded) in Greater London Area that have created ( _blue line_ ) and edited (i.e. updated) ( _red line_ ) features 

96 

V. Antoniou and C. Schlieder 

**Fig. 5.3** Percentage of features per number of versions 

**Fig. 5.4** The accumulated % of created features ( _blue line_ ) vs the accumulated % of updated features ( _red line_ ) by 6-month period. The _green bars_ show the % of difference in the number of features 

In order to examine how up-to-date the OSM dataset is, the number of features created and edited in each 6-month period since the beginning of OSM has been calculated. There is a steadily growing difference (Fig. 5.4). More specifically, in the first half of 2013, over half (56%) of the geographic entries had not been updated/ edited. This observation leads to the concerning conclusion that a growing number of OSM features are falling behind when the up-to-date factor is considered. This is even more interesting as the analysis showed that more contribution effort is focused on data updating than data creation (see Fig. 5.2) and thus this effort is not evenly distributed to the spatial features. Also, it is interesting to consider that, as previous research has shown, edits from many contributors improve the overall quality of the spatial features (Haklay et al. 2010). 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

97 

## _**5.2.3  Is There Any Spatial Pattern in the OSM Contributors’ Behavior?**_ 

Spatial statistical analysis was completed (Hot Spot Analysis using the Getis-Ord Gi* statistic provided in ESRI ArcGIS 10.2.2) on the dataset using the number of edits of each OSM feature. The null hypothesis is that all areas equally attract contributors’ interest in terms of editing existing features. Any deviation from this hypothesis should be a random phenomenon (an exception could be in the cases of major reconstruction works in specific areas that could lead to increased number of edits, however no such thing has been recorded for the study period). It was possible to identify statistically significant spatial clusters of both high values (hot spots) and low values (cold spots) in the number of edits for each feature. The Hot Spot Analysis based on the number of edits of each road segment reveals which areas are attracting the interest of OSM contributors and which are not and thus challenges the validity of the null hypothesis. Figure 5.5 shows the results of the hot spot analysis of the streets of the Camden London Borough. It is interesting to note that the hot areas are the area around UCL (lower red) and the famous and highly touristic are of Camden Market (middle red). This observation shows that users are focusing their contribution on specific popular and well-known areas while overlooking other more obscure ones and thus the null hypothesis is rejected. The results of this analysis are in accordance with previous observations about the correlation of socioeconomic factors and contribution mentioned above. 

The analysis of the OSM dataset shows that the evolution of VGI introduced new uncertainty sources for the spatial data available on the Web. Apart from the classic spatial quality elements (ISO 2005), there is growing evidence that social factors influence data quality of VGI. It is worth noting that these social factors are totally different from the error sources that usually affect the classic geographic information production mechanisms followed by national mapping agencies. Consequently, the VGI opens up new areas for further research in the subject mat- 

**Fig. 5.5** ( **a** ) OSM participation pattern based on the hot spot analysis on the versions of each feature, ( **b** ) the z-score and p-value distributions (source: ESRI) 

V. Antoniou and C. Schlieder 

98 

ter of spatial data quality and the long-run evolution of initiatives like OSM. Measures to counter- balance social data phenomena should be taken into account if OSM is to become a world-class spatial database, and/or simply preserve its current status as a reliable, up-to-date spatial database. 

## **5.3  Spatial Gamification** 

One solution to the data issues emerging from VGI, such as those identified for OSM in the prior section, is using techniques used in geogames to increase updated data from less popular places. Crowd-based mapping shares some characteristics with the game playing activities in geographic space that have become popular, such as Niantic’s global multi-player game **Ingress** (Hodson 2012) or the gamification mechanisms of the location-based social network **Foursquare** (Lindqvist et al. 2011)—not to mention the current ecstasy about **Pokémon Go** . In such locationbased geogames, the geographic location of the player constitutes a fundamental game element since different places in the geographic environment are associated with different choices of game actions (Schlieder et al. 2006). In the following, we use the term geogame to refer to such location-based games, thus, in a more restricted sense than in the introductory chapter of this book. Geogames motivate players to visit places which they probably would not visit outside the game. Not surprisingly, researchers have started to study geogames as a means to increase participation in VGI. Examples include the photographing and geo-referencing of buildings (Matyas et al. 2009) or the mapping of noise in an urban environment (Garcia-Martí et al. 2013). However, little is known on how to relate the participation issues of VGI mapping to specific design patterns of geogames. 

The following analysis concentrates on the design of the game mechanics, that is, the set of rules which define the sequence of game actions (Montola et al. 2009; Adams and Dormans 2012). Geogames are played as search games or chase games or they follow some other paradigm, frequently, a paradigm drawn from precomputer outdoor games (Davidsson et al. 2004). The many variants of capture-theflag games constitute such a time-tested paradigm. Places in the geographic environment act as resources that the mechanics of the geogame allocate to the players according to a variety of rule sets. This analysis refers to such games as spatial allocation games. 

**Geograph** , the photographic mapping activity mentioned in the chapter’s introduction, can be seen as a spatial allocation game in which the player’s task consists in submitting the first geographically representative photograph for squares of the Ordnance Survey grid of Great Britain and Ireland[3] . Three other geogames illustrate other ways to interpret the spatial allocation paradigm. **Foursquare** primarily offers the services of a location-based social network, however, the check-in mechanism implemented in releases prior to Foursquare 8.0 adds a gamification element 

3 The full name of the game is Geograph Britain and Ireland (www.geograph.org.uk). 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

99 

(foursquare.com). Users who check-in at places with a mobile device are rewarded for frequent re-visits by becoming the “Mayor” of the place. **Ingress** is a geogame in which two teams of players compete to capture and re-capture places called “portals” on a global game board (ingress.com). The game comes with complex game mechanics which—to simplify considerably—allocates a portal to the team of the player who visits the place while being in possession of the appropriate game resources and knowing how to best deploy them tactically. **Neocartographer** has been designed by the second author of this article as a game for two competing players or teams. The players try to obtain places which form a particular spatial configuration, instead of just maximizing the number of places in their possession (www.geogames-team.org). 

## _**5.3.1  Design Pattern for Allocation Games**_ 

Some fundamental design choices apply to all types of geogames as pointed out by Montola et al. (2009). Geogames are either played on a bounded game field or without spatial restrictions anywhere in the global geographic space. In the temporal dimension, the game can last for a limited playing time or can go on without end (pervasive play). 

The specific design choices for spatial allocation games have not been systematically described in the literature. For the purpose of this analysis, two design parameters are considered: allocation type and place-to-player ratio. In three of the four example games, place allocation is exclusive, that is, a place can only be allocated to one player or team at a time. **Foursquare** , where several users can check-in at the same place and earn badges for these check-ins, uses multiple allocation in combination with exclusive allocation for awarding the title of mayor of a place. 

A simple metric of ratio of places to players reveals further differences. **Geograph** is played by 12,038 players (accounts) in 331,956 places (grid cells)[4] , reflecting a place-to-player ratio of approximately 30:1. In contrast, the **Foursquare** website states for the same period that more than 1,500,000 places (venues) created by businesses are visited by more than 45,000,000 players (patrons) which amounts to a ratio of 1:30. **Ingress** does not publish global player statistics. However, since only two teams compete, the ratio is of the same order of  magnitude as the global number of portals. A typical **Neocartographer** game where two players compete for half an hour is played with ten places, that is, with a place- to- player ratio of 5:1 (Table 5.2). 

Most geogames with a large place-to-player ratio are based on a mechanics with exclusive place allocation. In OSM mapping, the geographic features outnumber the mappers by far with a place-to-player ratio even higher than that of **Geograph** or **Ingress** . A global and pervasive game play with exclusive allocation suggests itself as design choice for a gamification approach to OSM mapping. Different game design patterns for allocating and deallocating places are consistent with this choice. 

4 As of April, 2014. 

V. Antoniou and C. Schlieder 

100 

**Table 5.2** Design parameters of spatial allocation games 

||Spatial<br>boundary|Temporal<br>boundary|Allocation<br>type|Place-to-player ratio r|
|---|---|---|---|---|
|**Geograph**|Game<br>feld|Pervasive<br>play|Exclusive|10 < r < 100|
|**Foursquare**|Global|Pervasive<br>play|Multiple|10−2< r < 10−1|
|**Ingress**|Global|Pervasive<br>play|Exclusive|105< r < 106|
|**Neocartographer**|Game<br>feld|Playing time|Exclusive|1 < r < 10|



**Table 5.3** Design patterns for allocating places 

||Mechanics|Objective|Example|
|---|---|---|---|
|First-to-<br>visit|The place goes to the frst<br>visitor|Spatial<br>coverage|Geograph points (Geograph)<br>Claiming a portal (Ingress)<br>Claiming a cell<br>(Neocartographer)|
|Nth-to-<br>visit|The place goes to the n-th<br>visitor|Game<br>balancing|Second visitor points (Geograph)|
|Most-<br>revisits|The place goes to the most<br>frequent visitor|Revisit<br>frequency|Mayor of a place (Foursquare)|



An allocation pattern describes the game mechanics which specify what players need to do in order to obtain a place. A widely used mechanism consists in allocating the place to the first visiting player (first-to-visit pattern, Table 5.3). In a later stage of the game, when most of the places have been allocated to their first visitors, some games employ an additional mechanism which awards the place also to the second or even third visitor in a multiple allocation scheme (nth-to-visit **pattern** , Table 5.3). Geogames with a small place-to-player ratio tend to reward players who revisit a place (most-revisits pattern, Table 5.3). 

Deallocation mechanisms counteract the consumption of places by allocation mechanisms. Some games, such as the original version of **Geograph** , do not use deallocation at all (never pattern, Table 5.4). The most popular mechanism for competitive two player games permits the player to reclaim a place from the opponent. In the simplest form, a place is reallocated any time one of the two players visit it (when-reclaimed pattern, Table 5.4). Another solution consists in using a decay time after which places are freed (when-decayed pattern, Table 5.4). 

Although the aforementioned design patterns for allocation and deallocation do not provide an exhaustive inventory of design choices, they help to identify possible gamification approaches to the quality issues of OSM mapping. The design objective of maximizing the revisit frequency matches the problem that OSM contributors show little commitment to their edits (most-revisits pattern, Table 5.3). Similarly, the when-reclaimed pattern for deallocation motivates players to visit places which other players have visited before. It permits to address the design 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

101 

**Table 5.4** Design patterns for deallocating places 

||Mechanics|Objective|Example|
|---|---|---|---|
|Never|The place is allocated for the<br>wholegame|Simplicity|Geograph points<br>(Geograph)|
|When-<br>claimed|The allocation changes if<br>another player meets the<br>allocation criterion|Data recency game<br>balancing|Reclaiming portals<br>(Ingress)|
|When-<br>decayed|After a time span, the allocation<br>is cleared|Game balancing|Energy loss of<br>resonators (Ingress)<br>Moving time window<br>(Foursquare)<br>Time-gap points<br>(Geograph)|



objective of data recency in a VGI game context. The issue of spatial regularities in the behavior of OSM contributors seems more complex as it reflects the effects of socio-economic factors. Gamification might still counteract the spatial clustering of mapping activities. The first-to-visit pattern combined with exclusive allocation is a well-tried mechanism for maximizing the spatial coverage of in-game activities. 

## _**5.3.2  Place Allocation and Game Flow**_ 

Allocation measures the accumulated percentage of places that have been assigned to players as a function of the percentage of total playing time. It runs from 0% allocated places at 0% time to some percentage smaller or equal 100% allocation at the end of the game (100% time). This simple measure captures an important aspect of the game flow, especially if changes in allocation are observed: a low allocation rate indicates a phase in which the game’s goal is hard to achieve, while a high rate corresponds to a phase of easier game play. 

In principle, a game can allocate places at a constant rate until no more places are available. It is not difficult to design game mechanics with that effect (Box 5.1). There are some advantages of a constant allocation rate, most importantly, the control over total playing time. In organizing a gamified mapping event, which targets a specific feature class and spatial region, for instance, parking lots on a university campus, it helps being able to anticipate the progress of the game. Furthermore, constant allocation implies constant consumption of additional resources that the game might require, such as the verification of the mapped features. 

Most game mechanics do not guarantee a constant allocation rate in all games, although some display a similar behavior on average. In general, the allocation rate of a game changes over time and depends on a number of factors such as the spatial distribution of players or the type of locomotion they use. Allocation is empirically determined by logging the game and expressed as a real-valued function _a_ ( _t_ ): [0,1] → [0,1]. Figure 5.6a shows a typical plot of allocation as a function of time. 

V. Antoniou and C. Schlieder 

102 

## **Box 5.1 Game Mechanics with Constant Allocation Rate** 

The task of the players consists to map geo-features at 1000 distinct places. Each day a maximum of ten places are allocated to players that have mapped the corresponding features. The game client informs the players in real-time on the number of places that can still be mapped that day. After the daily upper bound is reached, the game server ignores all allocation requests. There is no queuing of requests. If at the end of the day less than ten places have been mapped, a place lottery allocates the remaining places to some randomly chosen players. No geo-features are mapped in places that have entered the lottery. 

The game mechanics produces an allocation rate of exactly ten places/day and ends the game after a period of exactly 100 days. To minimize or avoid the place lottery, the daily maximum should be sufficiently small. It is also a good idea to try to estimate the difficulty of mapping a place and put “easy” places into the lottery. Since the difficult mapping tasks are accomplished during the game, chances are good that the few remaining places will be mapped without the incentive provided by the game. 

**Fig. 5.6** Neocartographer ( **a** ) allocation plot, ( **b** ) interface 

The values on both axes are expressed as percentages and describe ten allocation events of a **Neocartographer** game. The additional data point (0,0) has been added to describe the status at the start of the game. This specific instance of the game has been played on a rather small and sparsely populated (n = 10 places) game field in the city of Augsburg, Germany. Two players were competing for the  allocation of the places. The game play followed the mechanics described in Box 5.2. Figure 5.6b shows the interface of the client software at the end of a (different) game. It is important to realize that the allocation of a place constitutes an event. Allocation 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

103 

## **Box 5.2 Neocartographer** 

In its simplest version, Neocartographer is a two-player game in which each player tries to be the first to accomplish specific mapping tasks at the _n_ places shown by the game client software. From the point of view of allocation, the game mechanic is very simple. Whoever maps a place first, owns that place, a straightforward application of the first-to visit pattern with no deallocation. 

The main point of the game mechanic, however, is to challenge the players to reason spatially. Places are not equally interesting to own. The worth of a place is determined by the size of its Voronoi cell. In the standard playing mode, the boundary of the cell is not shown to the players. They have to decide on which place to move to next taking into account the location of the opponent, the distance of the place, and what they believe, the size of its cell is. 

Game logs of the two-player version of Neocartographer show that for small game fields with uniformly distributed places, the game mechanic produces a relatively constant allocation rate on average. 

changes in a stepwise way. At 51% playing time, allocation increases to 70% and at 60% playing time it still has the same value (Fig. 5.6a). The line segments interpolating between the data points are shown only to illustrate the concept of allocation rate, with a steeper slope of a segment indicating a higher rate. 

Allocation is a discontinuous step function _a_ ( _t_ ) if a geogame is played on a finite number of places. For the purpose of visualization and analysis, however, the data points of _a_ ( _t_ ) are often interpolated to produce a continuous approximation of the allocation function. If no deallocation of places occurs, the allocation function is monotonic: for any two time points _u_ and _v_ during playing time, _u_ < _v_ implies _a_ ( _u_ ) ≤ _a_ ( _v_ ). Many monotonic allocation games are played until all places have been allocated, that is, _a_ (1) = 1. We call them _simple geogames_ . A simple geogame has a _convex allocation rate_ if for any two time points _u_ and _v_ during playing time, the graph of the allocation function _a_ ( _t_ ) lies below or on the line segment through _a_ ( _u_ ) and _a_ ( _v_ ) (Fig. 5.7a). If the graph lies above or on the line segment for all choices of _u_ and _v_ then the allocation rate is called _concave_ (Fig. 5.7b). Convex and concave are not mutually exclusive properties: constant allocation is both convex and concave. As the example from Fig. 5.7c illustrates, an allocation function may also be neither convex nor concave. 

In convex geogames, place allocation starts slow and accelerates towards the end of the game. Box 5.3 describes a game mechanic with convex allocation. Many designers consider it a flaw if a game becomes progressively easier to play. They fear that such a game scares off novice players by its difficulty and bores expert players by not providing sufficient challenge during the later phases of play. In fact, none of the four geogames considered in this chapter are designed to produce convex allocation. 

V. Antoniou and C. Schlieder 

104 

**Fig. 5.7** Allocation function of simple geogames ( **a** ) convex, ( **b** ) concave, ( **c** ) neither convex nor concave 

## **Box 5.3 Game Mechanics with Convex Allocation Rate** 

The task of the players consists of mapping geographic features at 1023 distinct places. At the beginning of the game, a single geographic location is disclosed to the players. This place will be easy to reach for some players, but for most players it will be far from their current geographic position and thus difficult to reach. The place is allocated to the first player who moves there and accomplishes the mapping task. After 10% of the total playing time, two more places are disclosed, and after 20% another four places, and so on until the last disclosure occurs at 90% playing time. The last disclosure of places informs the players about the geographic position of the remaining 512 distinct places. 

Places are disclosed according to a power law. Assuming a uniform random distribution of players and places, the chance to reach a place before other players doubles in each successive phase of the game. Allocation should increase from phase to phase provided that the player base maintains its activity level throughout the game. 

Nevertheless, the idea of increasing the place allocation rate during game play makes sense for some spatial gamification scenarios. One reason for adopting convex allocation is to counterbalance the effects of physical fatigue in games that involve locomotion over long distances and long periods of time, especially when weather conditions are bad. Another reason is that the game mechanics may need to deal with places that differ considerably in the difficulty of the associated mapping task (e.g. harder to access, more time consuming). Convex game mechanics such as the one from Box 5.3 may be used to balance task difficulties by disclosing first the places that are the hardest to map leaving the easier cases for the end game. 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

105 

## **5.4  Simulation Studies: The Problem of Accumulated Advantage** 

Most game mechanics do not follow convex allocation. They make it easy for players to obtain place allocations at the beginning of the game while making allocation progressively harder towards the end. A number of questions are relevant to the game designer interested in such a concave allocation: Under which assumptions does such an allocation arise? Is it possible to distinguish different phases in place allocation? How do the phases affect the game play? Simulation studies can help to address some of these questions. 

Since most geogames do not permit the modification of their game mechanics (e.g. **Geograph** , **Ingress** , **Foursquare** ), it is difficult to field-test the causal effects of allocation patterns. Additionally, field-testing geogames that use a large number of places requires a considerable time investment by large numbers of players. In response, some designers have resorted to integrating testing into playing. However, any optimization of the game mechanics means changing the rules during the game, which is unpopular among players, to say the least. An alternative approach, using game simulations has been successfully applied to the design of video games (Adams and Dormans 2012). One of the issues that simulation testing highlights is the problem of accumulated advantage, which is discussed more in this section. 

One critical element of location-based game simulation is the model of spatial player behavior. Many degrees of realism are possible, including agent-based simulations that interact with a terrain model (Heinz and Schlieder 2015). In simulations, much less input is needed to gain a better understanding of place allocation. Qualitative abstractions that permit the comparison of results between different simulation runs and between modifications of the player model are also quite helpful. The following phases of concave allocation described in this section provide such an abstraction for comparison. 

A very simple model of casual game play is used to illustrate this type of analysis. The software agents that model the players show alternating phases of spatial activity and inactivity. In an activity phase, the agent moves according to a constant velocity random walk direction mobility model (e.g. Roy 2011). This reflects the casual character of game play. The player does not actively travel towards the places that are of interest in the game, rather, the player uses journeys he or she engages in for some other reasons (e.g. commuting to work). A more elaborate model would take into account that players are sometimes willing to deviate from their routine journeys to gain some advantages in the game. Spatial inactivity corresponds to phases in which the agent does not change the location such as is the case for most types of work or leisure activity. For a casual player, the latter phases are typically longer than the phases devoted to locomotion. 

The simulation uses a grid-based representation of the spatial environment. Places where the game invites players to map geographic features are represented as a single cell each. The simulation is implemented in the NetLogo 5.05 environment 

106 

V. Antoniou and C. Schlieder 

**Fig. 5.8** Simulation ( **a** ) unallocated places ( _black cells_ ), allocated places ( _colored cells_ ), and players ( _colored triangles_ ), ( **b** ) activity phases 

(Wilensky 2012), which supports grid-based spatial simulations. Figure 5.8a shows a typical scenario: the agents (colored triangles) move through the grid along random walk trajectories (shown for one agent). The places at which the game invites to engage in geographic mapping activities are shown as colored cells. Cells that have been allocated to an agent are colored in the corresponding color. The black cells are still available for allocation. The game state is depicted at a later stage where all but 17 of the 128 places have been allocated to players. 

Although Fig. 5.8a does not convey the dynamics of the simulation, the location of the phases of inactivity can be identified to a certain extent from the players’ trajectory because of the specific random direction model. It lets the agents move along rather smooth paths. At brisk turns in the trajectory, the agent, very likely, has paused for a phase of inactivity. In Fig. 5.8b, which is from a different simulation run, the locations of inactivity have been marked by circles. 

The simulation models exclusive allocation to the first visitor with no deallocation, this is similar to the game mechanics of the original version of **Geograph** or that of **Neocartographer** . Interestingly, a single form of allocation function consistently emerges in the simulation runs. Figure 5.9 shows the percentage of allocated places as a function of the percentage of total playing time for a typical simulation. In the example, 20% of the places are allocated in less than 5% of the playing time and to allocate 80% of the places, it needs less than 40% of the time. The same qualitative behavior is found in repeated simulation runs. As in the much smaller example from the **Neocartographer** game (Fig. 5.6a), the linear interpolation of the simulated allocation function is neither convex nor concave. Its overall shape, however, indicates that the game start with high allocation rates and then slows down considerably. In such a case, allocation can be approximated by a concave function. 

Fitting a concave function to the simulation distinguishes two phases: a phase of fast play during which the allocation change is above average followed by a phase of slow play during which allocation change is below average (Fig. 5.10a, b). For obvious reasons, the slow play phase is not very attractive to human players. Players experience most success, in the sense that they are mapping features, during the first part of the fast play phase when there are more places than players. 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

107 

**Fig. 5.9** ( **a** ) Simulated first-to-visit allocation with no deallocation. ( **b** ) Least-square fit of a concave function (logarithm) 

**Fig. 5.10** ( **a** ) Concave function with phases of fast and slow play. ( **b** ) Phases of gameplay in a simulation run 

The simulation reveals another problem of a game mechanics based on exclusive first-to-visit allocation with no deallocation: the outcome of the game is predictable at an early phase. From the top 10% highest scoring players at the moment when 50% of places are mapped, most will still be among the top 10% at the end of the game. An advantage early in the game accumulates with this game mechanics. This phenomenon is called the problem of accumulated advantage in game design. 

To avoid the slow-down, first-to-visit allocation without deallocation should not be played beyond the point of 50% mapped places. Note that **Geograph** which 

V. Antoniou and C. Schlieder 

108 

implements this pattern, has already allocated 82% of the places to players. Based on the simulation results, one would predict that a spatial allocation game at this stage is mostly of interest to the highest performing players. This prediction is consistent with the high score lists published by the **Geograph** project which show little change over the course of the years. 

Remediating the problem by deallocation is not straightforward. Two-player geogames often combine exclusive allocation to the first visitor with the whenreclaimed deallocation pattern. Simulations show that frequently a new type of problem with the game balance emerges: the outcome of the game becomes too unpredictable as it is virtually decided in the last cycles of the simulation. For the playing experience, advantages which do not accumulate at all are as frustrating as advantages which accumulate too fast. 

## **5.5  Conclusions and Outlook** 

This chapter presented first results relating participation patterns in VGI to gamification mechanisms which can help to address participation issues. A case study from the Greater London Area revealed three spatial pattern in the behavior of OSM contributors. First, highly productive contributors were found to show little commitment to return and update the geographic features they created (commitment problem). Second, the gap between the accumulated percentage of created features and the accumulated percentage of updated features is widening (update problem). Third, the spatial analysis of OSM feature version shows a contrast between areas of high and low mapping activity (clustering problem). 

The chapter described spatial allocation games as a class of geogames suitable for a gamification approach to approach these issues in VGI mapping. Two design choices specific to allocation games were identified, the allocation type and the place-to-player ratio. The analysis of the geogames **Geograph** , **Foursquare** , **Ingress** , and **Neocartographer** helped to specify six common design patterns for the allocation and deallocation of places, and mapped the VGI participation issues onto design patterns. The commitment problem can be addressed by the most-revisits allocation pattern, the update problem by the when-reclaimed deallocation pattern, and the clustering problem by the first-to-visit allocation pattern. 

Agent-based simulations can help understanding the effect of allocation and deallocation patterns. The phase model based on the approximation of the allocation function helps to describe the two phases of fast and slow play produced by game mechanics based on concave allocation. To the best of our knowledge, simulations studies have not been systematically used to design geogames. Results from the first trials are encouraging. The simulation correctly reproduced the problem of accumulated advantage which arises in the Geographing game and links it to first-to-visit allocation pattern. As for any type of simulation, realism remains a challenge, especially when modeling player motivation. However, the costs for play testing 

5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms 

109 

geogames are much higher than for classical video games, which is why simulations offer an interesting alternative to study their game mechanics. 

Future research will explore more complex game mechanics which go beyond the combination of a single positive feed-back loop (allocation) with a single negative feed-back loop (deallocation). Preliminary results show that agent-based simulation provides a valuable method for avoiding the repeated modifications of the game mechanics by trial and error, which geogames currently impose on their players. 

**Acknowledgments** The second author’s research has been funded in part by ESRI Inc. within the Geogames and playful Geodesign project. 

## **References** 

- Adams E, Dormans J (2012) Game mechanics: advanced game design. New Riders Games, Berkeley, ISBN 978-0-321-82027-3 

- Antoniou V (2011) User generated spatial content: an analysis of the phenomenon and its challenges for mapping agencies, Doctoral thesis [Online] http://discovery.ucl.ac.uk/1318053/. Accessed 18 March 2014 

- Antoniou V, Haklay M, Morley J (2010) Web 2.0 geotagged photos: assessing the spatial dimension of the phenomenon. Geomatica 64(1):99–110. Special Issue on VGI 

- Antoniou V, Skopeliti A (2015) Measures and indicators of VGI quality: an overview. ISPRS Ann Photogramm Remote Sens Spatial Inf Sci 1:345–351 

- Arsanjani JJ, Barron C, Nakillah M, Helbich M (2013) Assessing the quality of openstreetmap contributors together with their contributions. In: 16th AGILE international conference of geographic information science, Leuven, Belgium, pp 14–17 

- Budhathoki NR, Bruce B, Nedovic-Budic Z (2008) Reconceptualizing the role of the user of spatial data infrastructure. GeoJournal 72(3–4):149–160 

- Coleman DJ, Georgiadou Y, Labonte J (2009) Volunteered geographic information: the nature and motivation of producers. Int J Spatial Data Infrastruct Res 4:332–358 

- Elwood S (2008) Volunteered geographic information: key questions, concepts and methods to guide emerging research and practice. GeoJournal 72(3-4):133–135 

- Davidsson O, Peitz J, Björk S (2004) Game design patterns for mobile games. Project report. Nokia Research Center, Finland 

- Estes JE, Mooneyhan W (1994) Of maps and myths. Photogramm Eng Remote Sens 60(5):517–524 

- Garcia-Martí I, Rodríguez-Pupo L, Díaz L, Huerta J (2013) Noise battle: a gamified application for environmental noise monitoring in urban areas. In: Vandenbroucke D et al (eds) AGILE-13. Springer, New York. www.agile-online.org/index.php/conference/proceedings/ proceedings-2013 

- Girres JF, Touya G (2010) Quality assessment of the French OpenStreetMap dataset. Trans GIS 14(4):435–459 

- Goodchild MF (2007) Citizens as sensors: the world of volunteered geography. GeoJournal 69(4):211–221 

- Goodchild MF (2008) Commentary: wither VGI? GeoJournal 72(3-4):239–244 

- Haklay M (2010) How good is volunteered geographical information? A comparative study of OpenStreetMap and Ordnance Survey datasets. Environ Plann B Plann Des 37(4):682–703 

- Haklay M, Basiouka S, Antoniou V, Ather A (2010) How many volunteers does it take to map an area well? The validity of Linus’ law to volunteered geographic information. Cartogr J 47(4):315–322 

Heipke C (2010) Crowdsourcing geospatial data. J Photogramm Remote Sens 65(6):550–557 

V. Antoniou and C. Schlieder 

110 

- Heinz T, Schlieder C (2015) An Agent-based simulation framework for location-based games. In: AGILE-15, proceedings of international conference on geographic information science, online proceedings. agile-online.org/index.php/conference/proceedings/proceedings-2015 

- Hodson H (2012) Google’s Ingress game is a gold mine for augmented reality. New Scientist 216(2893):19. https://doi.org/10.1016/S0262-4079(12)63058-9 

- International Organisation for Standardisation (2005) 19113 geographic information—quality principles. ISO, Geneva 

- Jackson SP, Mullen W, Agouris P, Crooks A, Croitoru A, Stefanidis A (2013) Assessing completeness and spatial error of features in volunteered geographic information. ISPRS Int J Geo-Inf 2(2):507–530 

- Kalantari M, La V (2015) Assessing OpenStreetMap as an open property map. In: OpenStreetMap in GIScience. Springer International Publishing, Switzerland, pp 255–272 

- Lindqvist J, Cranshaw J, Wiese J, Hong J, Zimmerman J (2011) I’m the mayor of my house: examining why people use foursquare-a social-driven location sharing application. In: SIGCHI-11, Proc. conf. on human factors in computing systems, pp 2409–2418 

- Matyas S, Matyas C, Mitarai H, Kamata M, Kiefer P, Schlieder C (2009) Designing location-based mobile games: the CityExplorer case study. In: de Souza e Silva A (ed) Digital cityscapes. Merging digital and urban playspaces. Lang, New York, pp 187–203 

- Montola M, Stenros J, Waern A (eds) (2009) Pervasive games. Theory and design. Morgan Kaufmann, Burlington, MA 

- Roy RR (2011) Handbook of mobile ad hoc networks for mobility Models. Springer, New York 

- Stein K, Kremer D, Schlieder C (2015) Spatial collaboration networks of OpenStreetMap. In: Jokar Arsanjani J et al (eds) OpenStreetMap in GIScience. Springer, Netherlands, pp 167–186 

- Schlieder C, Kiefer P, Matyas S (2006) Geogames: designing location-based games from classic board games. IEEE Intell Syst 21(5):40–46 

- Turner AJ (2006) Introduction to neogeography. O’Reilly Media Inc., Sebastopol, CA 

- Wilensky U (2012) NetLogo 5.0. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University. Evanston, IL 

- Zielstra D, Zipf A (2010) A comparative study of proprietary geodata and volunteered geographic information for Germany. In: Proceedings of the thirteenth AGILE international conference on geographic information science, Guimarães, Portugal
