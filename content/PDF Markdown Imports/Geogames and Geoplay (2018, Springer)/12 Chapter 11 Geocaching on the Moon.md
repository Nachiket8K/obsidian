---
title: "Chapter 11 Geocaching on the Moon"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 11 Geocaching on the Moon** 

## **Cheng Zhang** 

## **Abbreviations** 

|AR|Augmented Reality|
|---|---|
|ARTEMIS|Acceleration, Reconnection, Turbulence and Electrodynamics of|
||the Moon’s Interaction with the Sun|
|DEM|Digital Elevation Model—a digital model for 3D presentation of a|
||terrain’s surface, created from terrain elevation data|
|ESA|European Space Agency|
|GPS|Global Positioning System|
|GRAIL|Gravity Recovery and Interior Laboratory|
|ISS|International Space Station|
|JAXA|Japan Aerospace Exploration Agency|
|LAC|Lunar Aeronautical Chart|
|LADEE|Lunar Atmosphere and Dust Environment Explorer|
|LCROSS|Lunar Crater Observation and Sensing Satellite|
|LRO|Lunar Reconnaissance Orbiter|
|LROC|The Lunar Reconnaissance Orbiter Camera|
|NASA|National Aeronautics and Space Administration|
|QR code|Quick Response Code|
|SELENE|Selenological and Engineering Explorer (JAXA)|
|STEM|Science, Technology, Engineering, and Mathematics|
|VR|Virtual Reality|
|WAC|Wide Angle Camera|



C. Zhang ( * ) 

NASA Scientific Visualization Studio at Goddard Space Flight Center, Greenbelt, MD, USA 

The Ohio State University, Columbus, OH, USA e-mail: cheng.zhang@nasa.gov 

© Springer International Publishing Switzerland 2018 

O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0_11 

209 

C. Zhang 

210 

## **11.1  Introduction** 

The Moon is the only natural satellite of the Earth—the closest celestial object to our home planet. Appearing in folktales of almost all cultures, the Moon has fascinated people for thousands of years. Even though humanity has accomplished great achievement of lunar exploration, only 12 people have thus far landed on the Moon; It remains inaccessible for the rest of us. To rectify this, **The Moon Exploration** is a geocaching, multiplayer, mixed reality game that brings the Moon down to the Earth so that people can have access to it. Using the most up to date scientific data, players can explore in the game as if they were the astronauts exploring on the Moon. The location-based mapping scheme maps a lunar location to places on the Earth, so people can explore the Moon in the virtual world while moving around on the Earth. The game-playing facilitates communication and social interactions among players, which could facilitate the formation of a large lunar geocaching community on the Earth. 

Since 2000, the scientific community has seen a new trend of private sector and even individuals participating in space exploration. This grass-roots movement needs an accessible platform where everyone can try out and feel what things would be like on the Moon. **The Moon Exploration** platform can provide universally accessible and useful information about the Moon. The game uses data from lunar landing missions, spacecrafts, satellites, or lunar orbiters. The goal is to bring the Moon down to the Earth in an appealing way so that people can explore the Moon as if they were the astronauts in the virtual world while moving around on the Earth. The pervasive play has the potential to stimulate young generations’ interests in space exploration and promote STEM learning. The game can also be a platform for potential citizen science projects in the future, which would benefit the science research community as well. 

In the following section, I offer an overview of lunar exploration and lunar geology. I also review the geocaching games and the technology of virtual reality (VR) and augmented reality. I describe how the game is designed and developed in Sect. 11.4. 

## **11.2  Background** 

People have studied the Moon since ancient times. Ancient astronomers understood the lunar regular cycle of phases, the lunar gravitational influence on the ocean tides, the cause of lunar eclipses, and could even predict solar eclipses by analyzing the Moon’s motion (Zhentao et al. 1989; Steele and Stephenson 1998; Stephenson 1997). It was Galileo Galilei who first observed lunar mountains and craters when he pointed his crude telescope to the Moon. Nevertheless, it is only in modern times that human beings could actually explore the Moon. 

11 Geocaching on the Moon 

211 

## _**11.2.1  The Exploration of the Moon**_ 

Since 1959, 78 spacecraft have so far (to date) orbited, impacted, flown by, or landed on the Moon (Lunar and Planetary Institute 2016; Williams 2013; Spudis 2008). These missions can be divided into two phases: the lunar exploration driven by the space race from 1950s to 1976 and the current exploration that began in the 1990s. In the first phase, both competitors the Soviet Union and the United States have accomplished great achievements. 

From the late 1950s to 1976, the Soviet Union carried out the Luna Program, a series of robotic spacecraft missions to the Moon. On January 2, 1959, Luna 1, the first robotic spacecraft to the Moon, missed its intended impact and became the first spacecraft to fall into orbit around the Sun. In September 1959, Luna 2 was launched and successfully hit the Moon’s surface, becoming the first man-made object to reach the Moon. Launched in October 1959, Luna 3 returned the first photographs of its far side, which can never be seen from the Earth. Luna 9 was the first spacecraft to perform a successful lunar soft landing in 1966. Luna 10 was the first artificial satellite of the Moon. Luna 16 in 1970, Luna 20 in 1972, and Luna 24 in 1976 returned a total of 0.3 kg rock and soil samples from the Moon. The Soviet Lunokhod program landed two pioneering robotic rovers on the Moon in 1970 and 1973. 

On the other hand, The United States explored the Moon in two steps: (1) the robotic spacecraft missions to pave the way for manned landing; (2) the Apollo program landing men on the Moon. The first step had three missions: six hard landing Ranger missions (1961–1965) (Williams 2005b; Hall 1977), five Lunar Orbiters missions (1966–1967) (Lunar and Planetary Institute 2011a), and the Surveyor space probes (1966–1968) (Lunar and Planetary Institute 2011b). Meanwhile, the Apollo Program (Loff 2015) was developed in parallel. Apollo 8 made the first crewed mission to lunar orbit in 1968. The Apollo 11–17 except for 13 (1969– 1972), six successful manned landings are seen as the culmination of the space race. The Apollo missions return about 382 kg of lunar rocks and soil in about 2200 separate samples. Many scientific instrument packages were installed on the lunar surface. For example, the stations’ lunar laser ranging corner-cube retroreflector arrays are still being used. Starting in the 1990s, many other countries became directly involved in lunar exploration. Japan (NASA 2007; JAXA 2007), China (Huixian et al. 2005; Li et al. 2015), and India (Bhandari 2005; Pieters et al. 2009) have developed their lunar exploration projects and launched spacecraft to the Moon. Meanwhile, the United States has orchestrated several lunar exploration missions—Clementine (Dino 2008; Williams 2011), Lunar Prospector (Williams 2005a; Lunar and Planetary Institute 2010), LRO and LCROSS (NASA 2015), ARTEMIS (Folta and Woodard 2010; NASA 2013a), GRAIL (NASA 2011a, b) and LADEE (NASA 2013b, c) for further information on the Moon such as gravitational fields, the chemical composition and distribution of the moon surface, and the Moon’s interaction with the Sun. 

C. Zhang 

212 

## _**11.2.2  Lunar Geology**_ 

The knowledge gained from lunar exploration helps us better understand early history of the solar system and the lunar geology (Wilhelms 1987; Jolliff et al. 2006). Unlike the Earth, the Moon lacks a significant atmosphere and does not have a dipolar magnetic field. Its radius is only about one fourth of the Earth, and its gravity is only about one sixth that of the Earth. The crust of the Moon is on average about 50 km thick. 

The lunar surface is mainly covered by bright and dark areas. Lighter areas are lunar highlands and darker areas are maria. The highlands are older than the visible maria, and hence are more heavily cratered. The maria are the major products of volcanic processes on the Moon. At a close look, the lunar landscape is characterized by craters, volcanoes, mountains, valleys, rilles, domes, wrinkle ridges, and grabens. According to the study by Head et al. (2010), there are 5185 craters larger than 20 km in diameter. Impact cratering is the most noticeable geological process on the Moon. The largest impact basins were formed during the early periods. They were successively overlaid by smaller craters. Small craters tend to form a bowl shape, whereas larger impacts can have a central peak with flat floors. These lunar geological data would be embedded into the virtual game world. 

Elements presented on the lunar surface include oxygen, silicon, iron, magnesium, calcium, aluminum, manganese and titanium. Rare elements such as titanium, gadolinium, and terbium draw growing interest of the Moon (SPACE.com 2011; David 2015). Another potential treasure on the moon is Helium-3, an isotope that may support fusion in the future. Helium-3 is a component of the solar wind. Since the moon doesn’t have much atmosphere, scientists estimate that there may be more than a million tons of isotope on the Moon. 

## _**11.2.3  The New Trend and Associated Challenges**_ 

As of 2000, space exploration is no longer exclusively the realm of large governmentdriven programs. The private sector has increasingly play a role—sometimes even a critical one. For example, as of 2015 SpaceX has flown six missions to supply the ISS with cargo. NASA also awarded SpaceX a contract to develop a program to transport crew to the ISS. The important feature of this new trend is the affordability of access to space. Because of the low cost and the readiness of technologies, more grass-roots start-up companies, or even individual projects have appeared. For example, teams in Google Lunar XPrize[1] (XPrize Foundation 2007) are all privately funded, and some have started from an individual’s idea. This trend also forms the 

> 1 Google Lunar XPRIZE is a $30 million competition to land a privately funded robot on the Moon. Google Lunar XPRIZE aims to open a new era of lunar travel by vastly decreasing the cost of access to the Moon and space. 

11 Geocaching on the Moon 

213 

collaborations between large government space agencies and the private sector. Many private companies or individuals seek launch vehicles (usually operated by large government programs) to lift off into space as payloads or space tourists (Sven 1996; Space.com 2007; Fox 2010). NASA has developed many programs to benefit from the commercial attempts to space. For example, in 2010, NASA awarded six companies the ILDD (Holmer 2012) contracts for the purchase of technical data resulting from industry efforts to develop vehicle capabilities and demonstrate endto- end robotic lunar landing missions (Braukus et al. 2010). The data from these contracts will inform the development of future human and robotic lander vehicles and exploration systems. 

Recruiting the general public (individual amateurs) as citizen scientists to conduct serious research is another example of the trend. Zooniverse (Zooniverse 2013) is a citizen science web portal produced and operated by the Citizen Science Alliance (Citizen Science Alliance 2013). Hosted by Zooniverse, the Moon Zoo (Galaxy Zoo 2010) is a citizen science project that asks users to identify, classify, and measure the shape of features on the lunar surface by providing released Planetary Data System (PDS) with high spatial resolution images from NASA’s Lunar Reconnaissance Orbiter (LRO) camera instrument. So far the Moon Zoo users have already visually classified 3,915,560 images and help researchers study the lunar surface in unprecedented detail (Katherine et al. 2010) and address important themes of lunar science and exploration. 

In future physical lunar exploration, the goal is beyond landing spacecraft or people on the Moon surface. It is more about how to make use of the lunar resources and how to build a hub or colony (Schmitt 2005). On November 26, 2015, President Obama signed the U.S. commercial Space Launch Competitiveness Act (or H.R. 2262) into law (114th Congress 2015). The law grants companies the rights to the natural resources that they mine from outer space, including Moon, Mars, asteroids, and other heavenly bodies. In 2013, ESA teamed up with architect companies (such as Foster and Partners) to test out various Moon base-building technologies including 3D printing. They concluded that 3D printing using lunar soil was feasible in principle for constructing buildings and other structures (3DERS 2014). Recently, ESA announced its plan to build a 3D printed Moon Village by 2030 in the International Symposium on Moon 2020–2030 in the Netherlands. The new Moon Village is designed to replace the International Space Station (ISS), and could provide a potential springboard for future missions to Mars. According to the estimation by NexGen Space LLC, a consultant company for NASA, a lunar refueling station would reduce the cost of sending humans to Mars by as much as $10 billion per year (Crew 2016). A moon village seems to look pretty inevitable. 

Given the above achievement, people should have a better chance to reach the Moon. However the reality suggests otherwise. So far only 12 Apollo astronauts have landed on the Moon since the Apollo program began. The Moon still remains unreachable for most people on the Earth. The Moon can be regarded as the eighth continent of the Earth, but given its distance of 384,400 km from the Earth, it is a long journey for people to get to the Moon. It took Apollo Astronauts 3 days 3 h 49 min to reach the Moon in 1969. By far the fastest mission to fly past the Moon 

C. Zhang 

214 

was NASA’s New Horizons Pluto mission. The powerful rockets propelled it over 58,000 km/h speed. Still, it took 8 h and 35 min to reach the Moon (Williams 2016). Even for the elite, rich space tourists[2] (Fox 2010) without financial concerns, space travel is still a daunting task physically and mentally, which also requires people to obtain systematic knowledge and rigorous trainings. The Moon is a remote and uncharted territory. It’s a lifeless, rainless, sun-seared, barren, and hostile world. Survival in such an extreme environment is difficult for ordinary people. Given the cost, training, physical conditions, space tourism is still not accessible for the general public. While available, large scientific data of the Moon are most likely used by and interpreted for science community rather than the general public. Because the original data are usually in the raw format of instruments and data in different processing levels (NASA 2010) may be involved with various parameters (or in different map projections (Fenna 2006; Snyder 1987)), they would be too complicated for the general public to comprehend. The challenge is how to access the Moon with the first-hand experience in an easy, interesting, and safe way with low cost. 

Through computing technology, people can have access to more information about the Moon than before. For example, NASA has produced a lot of lunar data products including latest lunar topography with the resolution of half meter per pixel. NASA Scientific Visualization Studio (Studio NSV 2000) has created a lot of animations about the Moon such as lunar phases, libration, eclipses, evolution, craters, and other features which precisely convey the latest scientific achievements to the general public. However, all these animations are piece by piece, linear in storyline. They cannot provide users with interactive and immersive experience of being on the Moon. Google Moon (Google 2012) allows viewers to have a virtual tour of the Moon and visit Apollo landing sites, but the number of sites that can be visited is very limited. Moon Zoo can provide users with a lot of 2D high-resolution lunar images and show the live information of different users online. However, users cannot interact with each other in real time. In other words, the current available applications/software lack an integrated solution that provides users with interactive, immersive, and first-hand virtual experience on the Moon, which is very much needed as a sandbox for the future physical lunar exploration—lunar mining and constructions of permanent lunar bases. 

## **11.3  Related Work** 

Besides the rich lunar content, **The Moon Exploration** also touches two exciting areas, geocaching games and VR/AR technology. In this section, I offer two short overviews. 

> 2 Space tourism has emerged since 2000. Seven rich individuals spending $20 million to $40 million have become space tourists. 

215 

11 Geocaching on the Moon 

## _**11.3.1  Geocaching Games**_ 

To bring down the Moon as the eighth continent of the Earth, I found that **geocaching** is an appealing idea to make it work. Originally from a very old treasure-hunt game, geocaching has been around since 2000 when President Clinton announced the removal of Selective Availability of GPS (FAA 2000). Geocaching is a GPSenabled, location-based treasure hunt. In this outdoor recreational activity, participants (geocachers) can hide or hunt ‘treasure’ (geocache or cache) by using GPS receivers. A geocache usually consists of a waterproof container that contains a logbook and inexpensive items. The coordinates of geocaches are posted onto a geocaching website. When a geocacher finds a geocache, he records the date and signs the logbook with his established code name. Afterwards, the cache must be placed back in the exact location where it was found. 

Since 2000, geocaching has rapidly become popular worldwide. Many geocaching companies have been established, for example geocahing.com, NaviCache (NaviCache 2011), TerraCaching (TerraCaching 2004), and **Munzee** (Munzee 2012). Geocaching is now played in more than 200 countries around the world, and there is at least one physical geocache deployed on every continent, including Antarctica (Spencer 2012). **Ingress** is another location-based game created by Niantic Inc., previous under Google[3] . **Ingress** is not exactly geocaching but has very similar game structures as a location-based game. The game was first released in November 2012. In 2015, **Ingress** already has seven million players worldwide. The hottest location based game to date, Pokémon Go, released by Niantic in July 2016, quickly became a global phenomenon. It has reportedly been downloaded by more than 100 million people worldwide even with mixed review 

In their work (Farvardin and Forehand 2013), Farvardin and Forehand conducted a survey about the motivation of geocaching, which reveals the reasons why the game is so appealing. The top motivations include (1) The thrill of the hunt, the opportunity to discover and explore new places, (2) Natural wonders and memorable experiences, (3) A way to get exercise, (4) Challenge, Solving puzzles, Cracking difficult codes (5) Socializing, Meeting new people, Making friends; Likeminded folks. These are also the motivations that we will try to integrate into our solution. 

## _**11.3.2  Virtual Reality and Augmented Reality**_ 

Since Ivan Sutherland and Bob Sproull created the first head mounted display (HMD), Sword of Damocles in 1968 (Sutherland 1986), VR/AR has become an exciting area in academia, military training, and medical fields. Some fundamental work has been done, particularly in theory. The concept the reality-virtuality continuum proposed by Milgram et al. (1994) indicates no clear line between reality 

3 Ninantic Inc. spun off from Google as an independent company in August 2015. 

216 

C. Zhang 

**Fig. 11.1** Some affordable HMDs in the current market. Goggle Cardboard, Samsung Gear, and Goggle Tech C1-Glass can be directly used with cell phones. Goggle Tech C1-Glass can be folded into a glass case. With 70 sensors and two wireless infrared cameras (not shown here), HTC Vive Pre offers users better motion tracking while users are moving freely around in a room. Fove is the first eye-tracking HMD. Microsoft HoloLens is expensive but has built-in Windows 10. It can merge real-world elements with virtual holographic images, creating half virtual and half augmented reality 

and virtual reality. In his forward-looking book (Zhai 1998), Zhai presented a philosophical view of virtual reality as invented realities that may be more real than people dare to believe. 

For nearly 50 years, even though many interesting developments have been achieved, VR/AR industries are still in smoldering stage. Several advances in technology have made the widespread use of VR more possible than before. One is the development of low-cost high-quality mobile devices and another is wearable  computing, which makes affordable and comfortable VR devices available in the market as shown in Fig. 11.1. Google’s Cardboard, which costs about $20, helped introduce VR to mainstream consumers. Consumers seem to be ready for VR. Samsung’s $99 Gear VR sold out on Amazon during the 2015 holiday season within 2 days. Most mobile phones can work with Google’s Cardboard and Samsung’s Gear VR, which allows people to have immersive experiences at any time anywhere. Meanwhile, enterprises are beginning to see the potential of VR applications such as gaming, entertainment, training, manufacturing, communication, and so on. According to a report from Digi-Capital, both VR and AR markets will become mainstream by 2020, and will generate $150 billion in the next 5 years (Gaudiosi 2015). The large IT companies such as Google, Facebook, Samsung and Microsoft all have products in the virtual reality space. In a research report from Goldman Sachs, the virtual and augmented reality market could become an $80 billion industry by 2025. Even though there is a big gap between these two reports, both agree that VR reaches far beyond gaming and entertainment. Gaming and entertainment will still drive much of the growth, but car 

11 Geocaching on the Moon 

217 

makers, retailers and even interior designers could bank on VR technology, according to Goldman Sachs analyst Heather Bellini. 

The affordable and portable VR devices such as those in Fig. 11.1 are the essential component to **The Moon Exploration** . 

## **11.4  The Approach** 

How do we make the Moon easily accessible? Can we access the Moon as easily as we access a place on the Earth via Google Maps or Google Earth? We design our solution as a multiple-players, geo-caching, mixed reality game. The goal is to create an effective learning experience in an interactive virtual lunar world with real world Global Positioning System (GPS) data. The main idea is to use real world GPS data to make a connection between a location on the Moon and places on the Earth. The link through GPS data shortens the distance between the Earth and the Moon, which makes the Moon become the accessible eighth continent of the Earth. Treasure-hunting is a proven appealing game genre that has existed for thousands of years. **The Moon Exploration** integrates treasure hunting as inviting activities for players. As a result, players can explore on the Moon surface in the game world while they are actually on the Earth. 

Behind the scenes, **The Moon Exploration** has two main game mechanics, the two module structure and the mapping scheme. The two-module structure is designed for the game to grow efficiently and flexibly. The mapping scheme makes use of both geo-data of the Moon and the Earth to bring the Moon down to the Earth. The two-module structure and the mapping scheme are presented in Sects. 11.4.1 and 11.4.2. In terms of locale, **The Moon Exploration** can be divided into two parts, the Moon (the virtual world) and the Earth (the real world). The lunar virtual world is created in the computer with Unity3D based on the available scientific data mainly from Lunar Reconnaissance Orbiter (LRO). LRO’s standardized lunar coordinate system (NASA GSFC 2008) is used to determine any location on the Moon surface with a unique set of latitude, longitude, and elevation. The coordinate system is also employed to compute the accurate positions and movements of the Sun and the Earth at runtime. The virtual world also contains manmade objects such as Lunar Module, Lunar Roving Vehicle (LRV or Moon Buggy), science equipment, and virtual caches. Each player has his own avatar (as in Fig. 11.2) in the virtual world as well. More details of the virtual world are in Sect. 11.4.4. In the real world, the game setting and playing are not much different from other online games. Players can create a cache, place it in a location, explore the lunar world, or hunt and find a cache. Several modes (creation mode, adventure mode, spectator mode, and multi-player mode) are used to facilitate various play activities. The game also provides players with the option to plug in virtual reality devices such as **Oculus Rift** , allowing players to have first-hand 3D immersive virtual experiences. The gameplay is described in Sect. 11.4.3. 

C. Zhang 

218 

**Fig. 11.2** The default avatar is created based on the appearances of Apollo astronauts 

## _**11.4.1  Two-Module Structure**_ 

Involving the two worlds, the Moon and Earth, the content of **The Moon Exploration** can be very broad and rich. The usage of the game may evolve further in various directions over time. For it to become more efficient and flexible, I designed an open-end two-module structure shown in Fig. 11.3. One module is for end players, the other for developer (expert) team. An approval process is needed to connect the two modules. This process is to ensure that the entire two-module structure works. 

In the player module, players have two options for their game property, public and private. The game property of a player refers to the player’s playing data, ideas, designs, and new implementations of the game. Under the public option, a player can make his/her game property available for the approval process toward being published and eventually available for all players once approved. Under the private option, a player can keep his/her game property private from the public. 

In the expert-team module, the team has the authority of further developing the game. For example, the team can create and approve new developments, modify simulation models, configure the general game settings, and analyze and validate the collected data. In the approval process, players provide the inputs. The experts can have access to and evaluate the inputs. Qualified ones will be integrated into the system and become available to all users. Unqualified ones will be filtered out and only be available for the submitter himself. This structure allows the game to evolve as new developments (from both players and developer team) become available. Having users’ inputs as a part of new development is a very powerful approach to enhance the existing application. For example, Google Maps allows users to add new features or edit existing ones with pending approval (Google n.d.). A user can 

11 Geocaching on the Moon 

219 

**==> picture [112 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
Game Mechanics & Assets<br>Expert Team Players<br>Simulation Model<br>Other Game Approval<br>Settings process<br>Analysis<br>**----- End of picture text -----**<br>


**Fig. 11.3** The two-module structure 

add new points of interest such as restaurants, hospitals, schools. A user can also add a walking trail, biking path, and more. Based on individual knowledge and experience, a lot of fine details can be added into Google Map by users via the approval process. In return, Google Maps can provide users with meticulous information on places. 

This architecture can also turn the game into a powerful crowdsourcing platform where players’ data, design, and implementation can be available and analyzed. In this setting, research such as citizen science projects can be carried out. **The Moon Exploration** is an open world game that has no single final goal for players to accomplish, providing players with a large amount of freedom in choosing how to play the game. However, the game has an achievement/scoring system to motivate players to gain recognition for their performance in their published profiles. 

Other than the two-module structure, mapping a lunar location to places on the Earth plays a key role in dragging the Moon to accessible range. In the next section, the mapping scheme is described in detail. 

## _**11.4.2  The Mapping Scheme**_ 

The mapping scheme is a critical component that fastens the Moon and the Earth together smoothly, which allows people to explore on the Moon while moving around on the Earth. The mapping scheme is based on the two coordinate systems, one for the Moon and the other for the Earth. Any location on the moon or on the 

C. Zhang 

220 

**Fig. 11.4** The map of all artifacts on the Moon. Source: NASA 

Earth can be specified by a set of numbers such as latitude, longitude, and elevation in these coordinate systems. For the Moon, I use LRO’s standardized lunar coordinate system (NASA GSFC 2008), which is comparable to the latitude and longitude of Earth in the common geographic coordinate system for the Earth. 

Given a lunar location with its latitude and longitude, we can find the corresponding position on the Earth with the same values of latitude and longitude. However, in this naïve mapping, most points of interest, such as robotic or manned lunar landing sites and the locations of most manmade artifacts left on the near side of the Moon (see Fig. 11.4) would be mapped into somewhere in oceans, desserts or jungles in Africa. In a reverse mapping, The United States is mapped into places on the far side of the Moon. Another issue is about the scale. The lunar diameter is about 3474 km, 27.242% of the Earth diameter. The total area of the lunar surface is only 7.4% the Earth surface area. In fact, the scale directly affects the speed of exploration in the virtual world. If 1:1 scale ratio is used, the United States would take up almost half of the Moon (see Fig. 11.5). The scale ratio 0 _._ 27242:1 would make more sense in the following situation. If the driving speed is 60 mph on the Earth, then the corresponding driving speed would be about 15 mph on the lunar surface, which is closer to the record of lunar rover vehicle (LRV) by Eugene Cernan, 11.2 mph (18 _._ 0 km/h). LRVs were designed with a top speed of about 8 mph (13 km/h) in the Apollo program. 

In our solution, scale ratio is a variable that can be changed by a player to fit different scenarios. When players interact with each other, their scale ratios need to be the same. The mapping function can be determined by several parameters including the initial lunar location _Pt_ 0 _L_[ and the start point on the Earth ] _[P][t]_ 0 _E_[.] 

**==> picture [204 x 41] intentionally omitted <==**

11 Geocaching on the Moon 

221 

**Fig. 11.5** The U. S. mapped on the near side of the Moon at scale 1:1, courtesy of Nicholas Schroen 

When a player chooses a lunar location he wants to visit, his initial position on the Earth is mapped to the selected lunar location as defined in Eq. 11.1 with a mapping scale Eq. 11.2, where _s_ . Afterwards, anytime his lunar location can be computed through _PtiL_ − 1[ is the previous lunar location, ] _d_  is the direction vector,  Δ _t_ is the time step, and _s_ is the scale ratio. Note that the direction vector _d_ is measured by the player’s movement on the Earth if he’s playing in the real world with GPS turned on in his device. However, the direction vector _d_  can be computed by the movement of the player’s avatar on the lunar virtual world if the player is indoors or his device has no GPS signals. 

The mapping is one-to-many from the virtual world to the real world. For example, the point (Lon: 30.77°, Lat: 20.19°) in Taurus-Littrow Valley (Apollo 17 land− ing site) on the Moon can be mapped to the location (Lon: 76.851531°, Lat: 38.996078°) in NASA Goddard Space Flight Center, the location in Time Square − (Lon: 73.98513°, Lat: 40.758896°) in New York city, or the location (Lon: 2.338568°, Lat: 48.860371°) at the Louvre in Paris. This one-to-many mapping allows people in different places on the Earth to explore one point of interest on the Moon. 

C. Zhang 

222 

Similarly, caches follow the same scheme. A virtual cache can have many corresponding real caches on the Earth. The score calculation reflects this mapping scheme—a player will achieve the maximal score for seeking a cache if he can find the virtual cache and all its corresponding real caches. Previous lunar explorations left many artifacts (NASA 2011c) on the lunar surface, which can be ideal candidates for super caches (see Fig. 11.4). The details about cache design is in Sect. 11.4.4. 

## _**11.4.3  Gameplay**_ 

**The Moon Exploration** is a mixed reality game. Its play is pervasive, extended out in the real world. Via gameplay, people can explore the Moon in the virtual world while moving around on the Earth. On the other hand, a player can also play the game without stepping out of the door, that is, no GPS data is needed. To have a proper game environment for players, I designed flexible options of play mode, mapping scheme, transportation tools, avatar, views, and so on. What’s most important, there are four play modes available in the game. 

1. **Creation mode** —assists a player in creating and building items such as caches, or anything as a part of a lunar colony. The Moon is believed to be a central hub for humans’ further journey into space. Colonizing on the Moon is one of the important steps to explore the cosmos (Schmitt 2005). ESA, working with the renowned architectural company Foster and Partner, proved that 3D printing using lunar soil was feasible in principle (3DERS 2014). The game borrows this idea and allows players to have 3D printers to manufacture parts, then assemble them into a habitable base on the Moon, especially in lunar lava tubes (CNN 2010) or craters in lunar poles, such as Shackleton Crater at the South Pole. 

2. **Adventure mode** —is designed for players to explore the Moon and find caches. As mentioned above, caches can be either virtual or real. When a player finds a cache, he should record the event in the log. If the cache is virtual, the system will automatically update the game status. If the cache is real (the player plays game in the real world), the player will use the cache ID to update the game status in a device. The player has an option to take an item from the cache and place a new item in the cache as well. For transportation, a player can have three ways to traverse on the Moon: walking, driving the buggy, and flying a small aircraft (as the transportation tools). More advanced tools require certain training and skills with higher cost. The game provides a menu to allow a player to choose his way to travel. If the speed does not fit in the player’s choice, the game will display the menu window for the player to make a new choice. 

3. **Spectator mode** —allows players to explore on the moon surface and watch other players playing activities such as hiding or hunting caches, or interacting with others. In this mode, a user can check and study certain features at a location on the moon just like the way we use Google Maps. 

4. **Multiplayer mode** —enables multiple players to interact and communicate with each other on the virtual lunar world. Except for communication, players need to 

11 Geocaching on the Moon 

223 

have the same scale ratio to interact with each other. There are several ways for players to communicate with each other. Each player has his profile that is publicly available, but the player can turn off certain items in his profile. The game has a broadcasting board that everyone can see. A player can send a message for assistance or recruit his partner or team over there. A player can also send a private message to certain players if he knows their usernames. Since players would explore in the extreme, remote, harsh lunar territory, a positive and healthy relationship among players is critical to have an effective experience in pursuing the common goal. Jenova Chen’s **Journey** has set up an excellent example of how to forge healthy companionships among players (That Game Company 2012a, b). The basic idea for **Journey** designed by Chen and his team, was to create a game that moved beyond the “typical defeat/kill/win mentality” of most video games. **Journey** is intended to make the player feel “small” and to give them a sense of awe about their surroundings (Nava 2012). In a similar situation where the Moon surface is a remote, harsh, and lifeless environment, players need solid friendships to achieve common goals in **The Moon Exploration.** 

The four play modes are not mutually exclusive. Some can work together. For example, with both the creation mode and multiplayer mode on, a player can build a project with a partner or team. In addition, GPS tracking function can be turn on/ off anytime. In some sense, this option offers a switch among different worlds. If GPS is off, a player can play the game in a device like most computer games (indoor). With the GPS on, a player can play the game while moving around on the Earth. This option can even help players handle the obstacles that they encounter on the Earth. For example, if a participant is playing the game while walking until a big lake blocks his way, he can turn off GPS and continue to explore the Moon in the virtual world with his device; alternatively he can continue to traverse on the Moon while rowing a boat in the lake with GPS being turned on. 

At the beginning, a player can choose the avatar he wants to play. The default avatar looks like an Apollo astronaut, shown in Fig. 11.2. The player can also change the scale ratio _s_ in the mapping function. By default, the game is played in the first person view to have a better sense of immersion/presence, particularly with VR display devices[4] . But in certain situations, the third person view may provide better perceptions. A player can change it as well. 

## _**11.4.4  The Game World**_ 

The game world consists of the lunar world and the earth world. On the display screen, a user can swap these two worlds anytime during the game. Like Google Map, the view of the earth world is simple, indicates the positions of real caches around the location on the Earth. The lunar world, however, is complex, is generated 

> 4 Like most current computer games, **The Moon Exploration** can be played without a VR device. 

C. Zhang 

224 

**Fig. 11.6** 3D model of Taurus-Littrow Valley is created in Unity 3D based on real topographic data 

procedurally based on the initial location and the real lunar topographical data from previous or ongoing missions such as LRO. For example, shown in Fig. 11.6, a 3D model of Apollo 17 landing site, Taurus-Littrow Valley is created in Unity based on topographic data such as DEM. Small items or textures in the lunar world are also generated procedurally based on available data. For instance, boulders can be created according to the boulder density hazard maps generated from the Moon Zoo. The purpose is to create a believable 3D environment, that is, a simulation of the lunar world containing useful lunar geological information. With the mapped GPS location and time, the playing environment is also simulated with the accurate motions of Sun, Earth, and other celestial objects in the solar system, creating the correct impression of what it looks like on the Moon in a specific location at a certain time. A compass and a location indicator are built in with the option to show the 2D map of the region, the facing direction, the location’s latitude, longitude, and the names of surrounding geological features such as mountains, craters, and maria, etc. Some other useful information such as the distribution/concentration of certain elements can also be embedded in the game. 

The lunar world also contains virtually manmade materials—tools and equipment, constructions built by players with the approval of the expert team, the artifacts left by previous missions, and caches. Tools and equipment include transportation means such as rovers and aircraft. The higher the level of the players, the more skills they possess, and the higher-end transportation means are available to them. Similarly, the distribution of equipment such as 3D printers and various robots follows the same pattern. Note that 3D printers are the revolutionary protocol for manufactory. They can be used to create gears and parts of any large tools and equipment. The initially available robots help assemble them together. The process can also create more available robots and eventually lead to the creation of a colony. 

225 

11 Geocaching on the Moon 

In **The Moon Exploration** , caches are essential ingredients. Like most geocaching games, a cache is a container at a given coordinates either on the lunar surface or on the Earth. A cache must contain a logbook with a unique ID, owner’s name and contact information. It may also include items for trade and other activities. When a player finds a cache, he must record his activity in the logbook (such as when and where the cache is found, and by whom, and whether any item is taken away or left out, etc.). To accommodate various activities, I have designed several types of caches: lunar cache, earth cache, and event cache. 

1. A **lunar cache** is on the lunar surface. Its size may vary. Along with the logbook, it may also contain information of surrounding geological features, personal experience, hints, tips, instructions, or warnings. A player can leave/inform helpful messages for later visitors. 

2. An **earth cache** is like a traditional geocache, but is placed at a coordinate on the Earth rather than in the virtual lunar world. 

3. An **event cache** is about a gathering of players in the game community. The Event Cache specifies a time for the event and may provide coordinates to its location in the virtual lunar world or on the Earth. After the event has ended, it is archived. 

Among caches, many interesting things can be arranged. For example, I designed a so-called chained cache—in order to completely recover a cache, a player may need to find out other caches to obtain critical information required by this cache. The player can broadcast to find a partner(s) to assist him. With this twist, communication and collaboration can be forged naturally. 

## _**11.4.5  Players and Communities**_ 

**The Moon Exploration** is a cultivated learning environment where players can have effective first-hand learning experiences. It is a multi-level game with an openended structure that can evolve as an effective crowdsourcing platform where serious lunar research can be conducted. It is also a sandbox where innovated designs or blueprints can be conceived, tested, and modified. Therefore, the target users are in a large range—from third or fourth graders all the way to graduate students, professionals, and experts. Players have several interaction options when playing the game. Every activity is possible for solo players but larger and more complicated tasks, for example, building a lunar base/colony, are more appropriate for groups. Players can form a virtual group, community, or society in the play world. The interactions among players help promote building healthy friendships and companionships in the harsh environment while pursuing common goals. As this game will be across-platform, it can be played in desktops, laptops, tablets, or mobile phones. **The Moon Exploration** would be the lunar information center, and can be made universally accessible and useful. 

226 

C. Zhang 

The game is designed as an open platform, in which the game can grow via not only the development team but also the player community. The game content can also be expanded to include more interesting, scientific, and educational materials. The complexity of **The Moon Exploration** requires (or draws) various skills and knowledge from different disciplines, which would lead to a multidisciplinary community. As the community grows, a virtual economy may also merge. 

## _**11.4.6  Development**_ 

**The Moon Exploration** is designed to be a multiplayer online geocaching game, which involves complex content of lunar science and complicated computing technology to support such a game system. To make the implementation feasible, I divide the whole project into at least three phases. 

Phase one includes the implementation of characters/avatars, basic game world, interface and interaction design, the core game mechanics, and key algorithms. The key algorithms procedurally generate certain aspects of the game world. For example, I created an algorithm to generate lunar terrains procedurally in runtime based on the initial location and the lunar topographic database. The algorithm works with the terrain engine of Unity3D to create lunar terrain so that it would never run out in play. Similar algorithms will be implemented, for instance, to generate boulders on the lunar surface based on geological feature data. 

Major tasks in phase two include (1) expanding the game to handle big geo-data, e.g., how to smoothly transit among different data sets; (2) building the game into different platforms—PCs, smart phones and handheld tablet computers; (3) making the game available in a local network with multiplayers. 

Scaling up the game with hundreds of players online is the challenge in phase three. A well-known issue is to develop the engines to handle vast numbers of players. The engines are made of powerful servers. If a typical server can handle a certain number of players simultaneously, dividing the players into many servers proves to be an efficient solution. Another predicted difficulty is time synchronization across hundreds or thousands of players since time is used to drive many physics simulations as well as scoring and damage detection. 

In phase one, I use the index map with 144 quadrangles (shown in Fig. 11.7) as the basic structure in my algorithms. The map with 144 plates, adapted from Bussey and Spudis’ work (Bussey and Spudis 2012), corresponds to the widely used Lunar Astronautical Chart (LAC) series. Each plate has 2° overlay with its adjacent plates if any, which ensures a smooth transition when traversing from one quadrangle to another. In terms of location, lunar terrains, data, game items can be efficiently organized with this structure. Given a location that a player wants to visit, it is easy to determine which quadrangle the location is in. Then the game can load all the information and objects related to that quadrangle at runtime while ignoring the rest. For each quadrangle, data are hierarchically organized from low resolution to 

11 Geocaching on the Moon 

227 

**Fig. 11.7** The index map with 144 quadrangles corresponds to the LAC system. At the lunar equator a plate is 20° in longitude and 16° in latitude. Source: NASA 

high resolution like a pyramid. Based on the distance between the camera and the destination in the 3D scene, the algorithm can automatically choose the proper resolution data to be used. 

When creating lunar terrain, a common issue is the missing data in a high resolution file as shown in Fig. 11.8, I create an algorithm to repair the holes. The general idea is to make use of the hierarchical data in various resolutions. If data are missing in a high resolution file, then the algorithm interpolates the corresponding value from surrounding pixels in the same file or interpolate it from lower resolution data. Since topographic data (usually in DTM) (Tran et al. 2010) are often associated with a confidence map that gives users a guidance on what elevation values to trust and not to trust, we can easily find out which pixels have missing data. Then the algorithm calculates the missing values through various resolution data files. 

To make lunar information universally accessible and useful, **The Moon Exploration** is designed as an across-platform game. It can be played in desktops, laptops, tablets, and mobile phones. The game also provides users an option to connect their VR display devices such as Oculus Rift, Google cardboard, etc. during the game-play, which would provide players a believable and immersive experience. 

C. Zhang 

228 

**Fig. 11.8** Topographical data of Apollo 17 landing site (Taurus-Littrow Valley) is available at LROC website http://lroc. sese.asu.edu/. The resolution is 2 m per pixel. The missing data appears in the middle of the image 

## **11.5  Summary** 

**The Moon Exploration** is a multiplayer online geocaching game based on real scientific data from direct lunar exploration, space crafts, satellites, and observations on the Earth. The goal is to make the Moon accessible as the “eighth continent” of the Earth. A user can explore any place on the lunar surface in the virtual world while moving around on the Earth. The gameplay provides a participant believable first-hand experiences as if they were the astronauts exploring on the Moon. The gameplay also fosters communication and social interactions among players to form a community of lunar geocaching on the Earth. **The Moon Exploration** is designed as a powerful crowdsourcing platform in which serious lunar research can be conducted. It may serve as a sandbox where innovative ideas, designs, and plans can be prototyped, tested, and modified. Finally, the game is also meant to attract the young generations’ attentions to space exploration and STEM learning. 

**Acknowledgements** I am very grateful to the Editors and two anonymous reviewers for their constructive and insightful comments. I would also like to thank my colleague Ernest Wright for his proof reading and comments that greatly improve the exposition of the manuscript. All remaining errors are my own. 

11 Geocaching on the Moon 

229 

## **References** 

- 114th Congress (2015) H.R.2262—U.S. Commercial Space Launch Competitiveness Act. https://www.congress.gov/bill/114th-congress/house-bill/2262/text# toc-HEE062BAAFBDD 4A43859C0142C68E67F9. [Online]. Accessed 30 Dec 2015 

- 3DERS (2014) ESA outlines plan to use 3D printing to build a fully habitable base on the Moon. http://www.3ders.org/articles/20141107-esa-outlines-plan-to-use-3d-printing-to-build-a-fullyhabitable-base-on-the-moon.html. [Online]. Accessed 20 April 2015 

- Bhandari N (2005) Chandrayaan-1: science goals. J Earth Syst Sci 114:701–709. https://doi. org/10.1007/BF02715953 

- Braukus M, Madison L, Byerly J (2010) NASA awards contracts for innovative lunar demontrations data. https://www.nasa.gov/home/hqnews/2010/oct/HQ_10-259_ILDD_Award.html 

- Bussey B, Spudis PD (2012) The Clementine atlas of the Moon. Cambridge University Press, Cambridge, UK 

- Citizen Science Alliance (2013) A community of practice for the field of public participation in scientific research. http://citizenscienceassociation.org/ 

- CNN (2010) Moon hole might be suitable for colony. http://www.cnn.com/2010/TECH/ space/01/01/moon.lava.hole/ 

- Crew B (2016) European Space Agency announces plans to build a ’Moon village’ by 2030. [Online]. Accessed 15 Jan 2016 

- David L (2015) Is moon mining economically feasible?. http://www.space.com/28189-moonmining- economic-feasibility.html. [Online]. Accessed 11 Nov 2015 

- Dede C (2007) Reinventing the role of information and communications technologies in education. In: Smolin L, Lawless K, Burbules N (eds) Information and communication technologies: considerations of current practice for teachers and teacher educators [NSSE Yearbook 2007 (106:2)]. Blackwell, Malden, MA, pp 11–38 

- Dino J (2008) NASA—Clementine mission. http://www.nasa.gov/missionpages/LCROSS/searchforwater/clementine.html. [Online]. Accessed 21 Oct 2015 

- FAA (2000) Satellite navigation—GPS—Presidential policy. https://www.faa.gov/about/office_ org/headquarters_offices/ato/service_units/techops/navservices/gnss/gps/policy/presidential/. [Online]. Passed 21 Aug 2015 

- Farvardin A, Forehand E (2013) Geocaching motivations. Worcester Polytechnic Institute, Worcester 

- Fenna, D. (2006) Cartographic science: a compendium of map projections, with derivations. CRC, Boca Raton 

- Folta D, Woodard M (2010) ARTEMIS—the first Earth-Moon libration orbiter. https://www.nasa. gov/mission_pages/themis/news/artemis-orbit.html. [Online]. Accessed 11 Oct 2015 

- Fox S (2010) Private companies that could launch humans into space. https://www.space. com/8541-6-private-companies-launch-humans-space.html 

- Galaxy Zoo (2010) Moon zoo. https://www.zooniverse.org/ 

- Gaudiosi J (2015) VR, AR will generate $150 billion in the next five years—Fortune. http://fortune.com/2015/04/25/augmented-reality-virtual-reality/. [Online] Accessed 10 Jan 2016 

- Google (2012) Google Moon. https://www.google.com/moon/. [Online]. Accessed 21 June 2015 

- Google (n.d.) Google map maker. https://www.google.com/mapmaker. [Online]. Accessed 15 Jan 2016 

- Hall RC (1977) Ranger impact—a history of project ranger. Tech. rep. NASA SP 4210. National Aeronautics and Space Administration. http://history.nasa.gov/ SP-4210/pages/Cover.htm 

- Head JW III, Fassett CI, Kadish SJ, Smith DE, Zuber MT, Neumann GA, Mazarico E (2010) Global distribution of large lunar craters: implications for resurfacing and impactor populations. Science 329:1504–1507 

- Holmer CI (2012) An overview of the Innovative Lunar Demonstration Data (ILDD) program: NASA’s next steps to extending public/private partnerships beyond earth orbit. In: Lunar and planetary science conference, Lunar and Planetary Inst. Technical report, vol 43, p 1605 

C. Zhang 

230 

Huixian S, Shuwu D, Jianfeng Y, Ji W, Jingshan J (2005) Scientific objectives and payloads of Chang’E-1 lunar satellite. J Earth Syst Sci 114:789–794. https://doi.org/10.1007/BF02715964 JAXA (2007) KAGUYA (SELENE)—TOP. http://www.kaguya.jaxa.jp/index e.htm. [Online]. Accessed 21 May 2015 

- Jolliff BL, Wieczorek MA, Shearer CK, Neal CR (eds) (2006) New views of the Moon, vol vol. 60. Mineralogical Society of America, Washington, DC. http://www.minsocam.org/msa/rim/ rim60.html 

- Katherine J, Crawford I, Grindrod P et al (2010) Moon Zoo: citizen science in lunar exploration. Astron Geophys 52(2):10–12 

- Li C, Liu J, Ren X, Zuo W, Tan X, Wen W, Li H, Mu L, Su Y, Zhang H, Ouyang JYZ (2015) The Chang’e 3 mission overview. Space Sci Rev **190** :85–101 

- Sarah Loff (2015) The Apollo missions—NASA. http://www.nasa.gov/mission pages/ apollo/missions/index.html. [Online] Accessed 11 Oct 2015 

- Lunar and Planetary Institute (2010) Lunar prospector mission. http://www.lpi.usra.edu/lunar/missions/prospector/. [Online]. Accessed 21 Oct 2015 

- Lunar and Planetary Institute (2011a) The lunar orbiter program. http://www.lpi.usra.edu/lunar/ missions/orbiter/. [Online]. Accessed 11 Oct 2015 

- Lunar and Planetary Institute (2011b) The surveyor program. http://www.lpi.usra.edu/lunar/missions/surveyor/. [Online]. Accessed 11 Oct 2015 

- Lunar and Planetary Institute (2016) Lunar exploration timeline. http://www.lpi.usra.edu/lunar/ missions/ 

- Milgram P, Takemura H, Utsumi A, Kishino F (1994) Augmented reality: a class of displays on the reality-virtuality continuum. In: SPIE telemanipulator and telepresence technologies, vol 2351, pp 282–292 

- Munzee (2012) Munzee: 21st century scavenger hunt. https://www.munzee.com/. [Online] Accessed 20 Oct 2015 

- NASA (2007) Hiten—Hagoromo mission profile. http://solarsystem.nasa.gov/missions/hiten/ indepth. [Online] Accessed 21 May 2015 

- NASA (2010) Data processing levels. http://science.nasa.gov/earth-science/ earth-science-data/ data-processing-levels-for-eosdis-data-products/. [Online] Accessed 21 May 2015 

- NASA (2011a) GRAIL—NASA. http://www.nasa.gov/mission pages/grail/main/#. Vq9sWvEvtug. [Online] Accessed 11 Oct 2015 

- NASA (2011b) GRAIL mission overview—NASA. http://www.nasa.gov/mission pages/grail/ overview/#. Vq9rw Evtug. [Online] Accessed 11 Oct 2015 

- NASA (2011c) NASA’s recommendations to space-faring entities: how to protect and preserve the Historic and scientific value of U.S. Government Lunar Artifacts. Tech. rep. National Aeronautics and Space Administration, USA 

- NASA (2013a) ARTEMIS: studying the Moon’s interaction with the Sun—NASA. http://www. nasa.gov/mission pages/artemis/#.Vq9qJfEvtug. [Online]. Accessed 11 Oct 2015 

- NASA (2013b) LADEE—lunar atmosphere dust environment explorer—NASA. https://www. nasa.gov/mission pages/ladee/main/index.html. [Online] Accessed 11 Oct 2015 

- NASA (2013c) Missions—LADEE—NASA science. http://science.nasa.gov/missions/ ladee/. [Online] Accessed 11 Oct 2015 

- NASA (2015) Lunar reconnaissance orbiter. http://www.nasa.gov/mission pages/ LRO/main/ index.html. [Online] Accessed 21 Oct 2015 

- NASA GSFC (2008) A standardized lunar coordinate system for lunar reconnaissance orbiter. Tech. rep. NASA Goddard Space Flight Center, Greenbelt, MD 

- Nava M (2012) The art of journey. Bluecanvas, Inc., Los Angeles, CA 

- NaviCache (2011) Geocaching with NaviCache—NaviCache home page. http://www.navicache. com/. [Online]. Accessed 20 Oct 2015 

- Pieters C, Goswami J, Clark R, Annadurail M (2009) Character and spatial distribution of OH/ H2O on the surface of the Moon seen by M3 on Chandrayaan-1. Science 326:568–572. http:// science.sciencemag.org/content/early/2009/09/24/science.1178658 

- Schmitt HH (2005) Return to the Moon. Praxis Publishing Ltd, New York, NY 

11 Geocaching on the Moon 

231 

- Snyder JP (1987) Map projections used by the U.S. Geological Survey. Tech. rep. Bulletin 1532, U.S. Geological Survey 

- Space.com (2007) Space tourism: the latest news, features and photos. http://www.space.com/ topics/space-tourism 

- SPACE.com (2011) Moon packed with precious titanium, NASA probe finds. http:// www.space. com/13247-moon-map-lunar-titanium.html. [Online] Accessed 21 Oct 2015 

- Spencer S (2012) New game in town. http://www.telegram.com/apps/pbcs.dll/article? AID=/20121110/NEWS/111109916/1246. [Online] Accessed 20 Oct 2015 

- Spudis PD (2008) NASA lunar exploration: past and future. http://www.nasa.gov/ 50th/50th magazine/lunarExploration.html 

- Steele JM, Stephenson FR (1998) Astronomical evidence for the accuracy of clocks in PreJesuit China. J Hist Astron 29(1):35–48 

- Stephenson FR (1997) Historical eclipses and Earth’s rotation. Cambridge University Press, New York, NY 

- Studio NSV (2000) NASA scientific visualization studio. https://svs.gsfc.nasa.gov/. [Online] Accessed 21 May 2015 

- Sutherland IE (1986) A head-mounted three dimensional display. In: Proceedings of AFIPS 68, pp 757–764 

- Sven (1996) Prospects of space tourism. In: 9th European aerospace congress—visions and limits of long-term aerospace developments. Aerospace Institute 

- TerraCaching (2004) TerraCaching. http://www.terracaching.com/. [Online] Accessed 20 Oct 2015 

- That Game Company (2012a) Journey. URL http://thatgamecompany.com/games/journey/. [Online] Accessed 1 May 2015 

- That Game Company (2012b) Journey PS3 Games PlayStation. https://www.playstation. com/ en-us/games/journey-ps3/. [Online] Accessed 1 May 2015 

- Tran, T., Rosiek, M., Beyer, R.A., Mattson, S., Howington-Kraus, E., Robinson, M.S., Archinal, B., Edmundson, K., Harbour, D., Anderson, E., the LROC Science Team (2010) Generating digital terrain models using LROC NAC images. In: ASPRS/CaGIS 2010, November 15–19, Orlando, Florida 

- Wilhelms D (1987) The geologic history of the Moon. Tech. rep. 1348, United States Geological Survey. http://ser.sese.asu.edu/GHM/ 

- Williams DR (2005a) Lunar prospector information. http://nssdc.gsfc.nasa.gov/ planetary/lunarprosp.html. [Online] Accessed 21 Oct 2015 

- Williams DR (2005b) Ranger to the Moon (1961–1965). http://nssdc.gsfc.nasa.gov/ planetary/ lunar/ranger.html. [Online] Accessed 21 Oct 2015 

- Williams DR (2011) NASA—Clementine project information. http://nssdc.gsfc.nasa. gov/planetary/clementine.html. [Online] Accessed 21 Oct 2015 

- Williams DR (2013) Lunar exploration timeline. http://nssdc.gsfc.nasa.gov/ planetary/lunar/lunartimeline.html 

- Williams M (2016) How long would it take to travel to the nearest star?. http://www.universetoday.com/15403/how-long-would-it-take-to-travel-to-the-nearest-star/. [Online]. Accessed 29 Jan 2016 

- XPrize Foundation (2007) Google lunar XPRIZE. http://lunar.xprize.org/ 

- Zhai P (1998) Get real: a philosophical adventure in virtual reality. Rowman & Littlefield Publishers, Lanham, MD 

- Zhentao X, Yau KKC, Stephenson FR (1989) Astronomical records on the Shang Dynasty oracle bones. Archaeoastronomy 20(14):61–72 

Zooniverse (2013) Zooniverse—real science online. https://www.zooniverse.org/ 

## **Ludography** 

The ludography lists geogames as well as video and online games that are mentioned in the chapters of the book. In addition to games, we also included platforms and frameworks for creating games. 

For commercial games, we provide the website of the game as the primary reference. All web links of the ludography have been accessed on June 5, 2017. Games created by researchers are referred to by the earliest publication describing them or by the publication that provides the most comprehensive description. For some of these games, the best description is found in one of the book chapters. In those cases, the reference is simply “Geogames and Geoplay.” The ludography distinguishes four types of entries: _C_ for console games, massively multiplayer online games or virtual worlds, _P_ for platforms used to create and/or run games, _L_ for location‐based geogames, and _D_ for desktop geogames. 

© Springer International Publishing Switzerland 2018 O. Ahlqvist, C. Schlieder (eds.), _Geogames and Geoplay_ , Advances in Geographic Information Science, https://doi.org/10.1007/978-3-319-22774-0 

233 

Ludography 

234 

|Chap.<br>(page)|10 (6–10)|3 (7)|9 (4)|8 (2)|4 (11)|7 (19)|3 (8)<br>6 (2, 6–19)<br>7 (26–28)|6 (13–19)|9 (2)|2 (3)|8 (11)|8 (11)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Additional reference||||Holden, C (2015) ARIS:<br>Augmented reality for<br>interactive storytelling. In:<br>C. Holden et al. (eds) Mobile<br>media learning, pp. 67–83.|||Geogames and Geoplay, Chap. 7|||Project Darkstar (n.d.). In<br>Wikipedia. https://en.wikipedia.<br>org/<br>wiki/<br>Proje ct_Darkstar#RedDwarf|||
|Primary reference|http://rezzly.com/|https://en.actionbound.com/|https://www.activeworlds.com|https://felddaylab.org|Poplin, A. (2014). Digital serious game for urban planning: B3—Design your<br>Marketplace!, Environment and Planning B: Planning and Design, 41 (3),<br>pp. 493–511.|Benford, S. et al. (2003) Coping with uncertainty in a location‐based game.<br>IEEE Pervasive Computing, 2(3), pp. 34–41.|Geogames and Geoplay, Chap. 6|Geogames and Geoplay, Chap. 6|https://civilization.com/|https://github.com/dworkin/reddwarf|Holden, C (2015) ARIS: Augmented reality for interactive storytelling. In:<br>C. Holden et al. (eds) Mobile media learning, pp. 67–83.|Mathews, J., Squire, K. (2009) Augmented reality gaming and game design as<br>a new literacy practice. In: K. Tyner (ed) Media Literacy: New Agendas in<br>Communication, pp. 209–232.|
|Game or<br>technology|3DGamelab|Actionbound|Active Worlds|ARIS|B3‐Design Your<br>Marketplace!|Can You See Me<br>Now|CityPoker|CityPokerGD|Civilization|Darkstar|Digital Graffti<br>Gallery|Dow Day|
|Type|P|P|C|P|D|L|L|P|C|P|L|L|



235 

Ludography 

|Chap.<br>(page)|8 (2)|9 (4)|3 (8)|1 (15–16)|5 (3, 7–11)|6 (1, 2)<br>11 (4)|1 (16)<br>5 (3, 7–11)|3 (8)<br>6 (13)|2 (1–13)|2 (3, 8)|
|---|---|---|---|---|---|---|---|---|---|---|
|Additional reference||||Noulas, A. et al. (2011). An<br>Empirical Study of Geographic<br>User Activity Patterns in<br>Foursquare. In: Proc. Int. AAAI<br>Conf. Web and Social Media,<br>pp. 570–573.||O’Hara, K. (2008).<br>Understanding geocaching<br>practices and motivations. In:<br>Proc. CHI‐08, ACM,<br>pp. 1177–1186.|Dykes, J. et al. (2008).<br>Exploring volunteered<br>geographic information to<br>describe place, In: Proc. of the<br>GIS Research UK Conf.<br>(pp. 256–267).|http://www.geogames‐team.org|||
|Primary reference|Klopfer E, Squire, K. (2004). Getting your socks wet: Augmented reality<br>environmental science. In: Proc. Int. Conf. Learning Sciences, p.614|https://www.eveonline.com/|Bell, M. et el. (2006). Interweaving Mobile Games with Everyday Life, In:<br>Proc. CHI‐06, pp. 417–426.|https://foursquare.com/|http://swarmapp.com/|http://www.geocaching.org<br>http://www.opencaching.us/<br>http://www.opencaching.de/|http://www.geograph.org.uk/|Schlieder, C., Kiefer, P., & Matyas, S. (2006). Geogames: Designing location‐<br>based games from classic board games. IEEE Intelligent Systems, 21(5),<br>pp. 40–46.|Geogames and Geoplay, Chap. 2|Geogames and Geoplay, Chap. 2|
|Game or<br>technology|Environmental<br>Detectives|Eve online|Feeding Yoshi|Foursquare<br>(after 2014:<br>Swarm)||Geocaching|Geograph<br>Britain and<br>Ireland|GeoTicTacToe|GIS‐MOG|Green revolution|
|Type|L|C|L|L||L|L|L|P|D|



236 

Ludography 

|Chap.<br>(page)|1 (8)<br>3 (7)<br>5 (3, 7–11)<br>6 (1, 3)<br>7 (5)<br>11 (5)|8 (11)|11 (12)|8 (2)|3 (8)|8 (9)|11 (5)|8 (9)|1 (16)<br>3 (8)<br>5 (3, 7–13)|4 (7)|
|---|---|---|---|---|---|---|---|---|---|---|
|Additional reference|Hodson, H. (2012). Google’s<br>Ingress game is a gold mine for<br>augmented reality. New<br>Scientist, vol. 216, no. 2893,<br>p. 19.||||Case, A. (2013). Introducing<br>MapAttack: An Urban<br>Geofencing Game, blog from<br>Oct 17, 2013,http://pdx.esri.<br>com/blog/introduci<br>ng‐mapattack/||Munzee (n.d.). In Wikipedia.<br>https://en.wikipedia.org/wiki/<br>Mun zee||http://www.geogames‐team.org||
|Primary reference|https://www.ingress.com/|Rosenkrantz, H. (2014) Jewish time travel gets real. The Covenant Foundation.<br>http://www.covenantfn.org/news/152/Jewish‐Time‐Travel‐Gets‐Real|http://thatgamecompany.com/games/journey/|Squire, K., Jan, M. (2007). Mad City Mystery. Journal of Science Education<br>and Technology, 16(1), pp. 5–29.|n.a.|Holden, C., Sykes, J. (2012) Mentira: Prototyping language‐based locative<br>gameplay. In: S. Dikkers et al. (eds.) Mobile media learning, pp. 113–129.|https://www.munzee.com|Martin, J. (2009) Mystery trip. In: S. Dikkers et al. (eds.) Mobile media<br>learning, pp. 99–110.|Feulner, B., Kremer, D. (2014). Using Geogames to foster spatial thinking, In:<br>R. Vogler et al. (eds). GI‐Forum‐14: Geospatial Innovation for Society, VDE:<br>Berlin, pp. 344–347.|Poplin, A. (2012). Playful public participation in urban planning, Computers,<br>Environment and Urban Systems, 36(3), pp. 195–206.|
|Game or<br>technology|Ingress|Jewish Jump<br>Time|Journey|Mad City<br>Mystery|MapAttack|Mentira|Munzee|Mystery Trip|Neocartographer|NextCity|
|Type|L|L|C|L|L|L|L|L|L|D|



Ludography 

237 

|Chap.<br>(page)|1 (15)<br>2 (8)<br>3 (1–23)|2 (8)|7 (5)|1 (1)<br>6 (1)|8 (14)|8 (12)|9 (4)|2 (13)<br>9 (2)|8 (11)|8 (2)|11 (1–17)|7 (3)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Additional reference||Lantz, F. (2007). Pacmanhattan,<br>In: F. von Borries et al. (eds.)<br>Space, Time, Play, pp. 262–263.|Parallel Kingdom (n.d.). In<br>Wikipedia, https://en.wikipedia.<br>org/wiki/Paral lel_Kingdom|Colley, A. et al. (2017). The<br>geography of Pokémon GO, In:<br>Proc. CHI‐17, ACM,<br>pp. 1179–1192.||||Gaber, J. (2007). Simulating<br>planning: SimCity as a<br>pedagogical tool. Journal of<br>Planning Education and<br>Research, 27(2), pp. 113–121.||http://education.mit.edu/<br>portfolio_page/taleblazer/|||
|Primary reference|Geogames and Geoplay, Chap. 3|http://www.pacmanhattan.com/|http://www.parallelkingdom.com|http://www.pokemongo.com/en‐us/|Macklin, C., Guster, T. (2012) Re:activism: Serendipity in the streets. In:<br>S. Dikkers et al. (eds.) Mobile media learning, pp. 151–169|Geogames and Geoplay, Chap. 8|http://secondlife.com/|http://www.simcity.com/|https://mobile.wisc.edu/mliprojects/project‐sustainable‐u/|http://taleblazer.org/|Geogames and Geoplay, Chap. 11|https://www.thesims.com|
|Game or<br>technology|Origami|Pac‐Manhattan|Parallel<br>Kingdom|Pokémon GO|Re‐activism|Riverside|Second Life|SimCity|SustainableU|TaleBlazer|The Moon<br>Exploration|The Sims|
|Type|D|L|L|L|L|L|C|C|L|P|D|C|



Ludography 

238 

|Chap.<br>(page)|9 (5)|8 (11)|8 (12, 15)|8 (11)|4 (19)|1 (15)<br>4 (1–22)|7 (5, 19)|
|---|---|---|---|---|---|---|---|
|Additional reference||||https://mobile.wisc.edu/<br>mliprojects/<br>feld‐research‐project‐webird/|||Zombies, Run! (n.d.). In<br>Wikipedia, https://en.wikipedia.<br>org/wiki/Zombies,_Run!|
|Primary reference|https://www.tombraider.com|Mathews, J. (2010). Using a studio‐based pedagogy to engage students in the<br>design of mobile‐based media. English Teaching, 9(1), pp. 87–102.|Wagler, M., Mathews, J. (2012). Up river: place, ethnography, and design in<br>the St. Louis river estuary. In: S. Dikkers et al. (eds.) Mobile media learning,<br>pp. 39–60.|https://mobile.wisc.edu/mliprojects/feld‐research‐project‐webird/|https://worldofwarcraft.com|Geogames and Geoplay, Chap. 4|https://zombiesrungame.com/|
|Game or<br>technology|Tomb Raider|To Pave or not to<br>Pave|Up River|WeBird|World of<br>Warcraft|YouPlaceIt!|Zombies Run!|
|Type|C|L|L|L|C|D|L|
