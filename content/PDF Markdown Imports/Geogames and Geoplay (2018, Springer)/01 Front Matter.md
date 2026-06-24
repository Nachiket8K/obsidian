---
title: "Front Matter"
book: "Geogames and Geoplay (2018, Springer)"
source_pdf: "Geogames and Geoplay (2018, Springer).pdf"
tags:
  - pdf-import
  - split-book
---

**Advances in Geographic Information Science** 

# Ola Ahlqvist Christoph Schlieder _Editors_ Geogames and Geoplay Game-based Approaches to the Analysis 

## **Advances in Geographic Information Science** 

## **Series editors** 

Shivanand Balram, Burnaby, Canada Suzana Dragicevic, Burnaby, Canada 

More information about this series at http://www.springer.com/series/7712 

Ola Ahlqvist • Christoph Schlieder Editors 

## Geogames and Geoplay 

Game-based Approaches to the Analysis of Geo-Information 

_Editors_ Ola Ahlqvist Christoph Schlieder Department of Geography Faculty of Information Systems The Ohio State University and Applied Computer Sciences Columbus, OH, USA University of Bamberg Bamberg, Germany 

ISSN 1867-2434 ISSN 1867-2442 (electronic) Advances in Geographic Information Science ISBN 978-3-319-22773-3    ISBN 978-3-319-22774-0 (eBook) https://doi.org/10.1007/978-3-319-22774-0 

Library of Congress Control Number: 2017958350 

© Springer International Publishing Switzerland 2018 

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. 

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use. 

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, express or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Printed on acid-free paper 

This Springer imprint is published by Springer Nature The registered company is Springer International Publishing AG The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland 

## **Foreword** 

Many people around the world were taken by surprise in July 2016 by the release of ‐ ‐ Pokémon Go, a virtual reality based mobile game. The mainstream press felt the need to expose every possible angle to the story: privacy, safety, physical exercise, add‐on complementary products, and of course business models. 

‐ But this mobile game did not appear from a vacuum. It was a re skinning (rebranding) of a far less popular game called Ingress, which served for a couple of ‐ years as the user generated data collector that fed the current version. The people behind the game at the company Niantic had not only top pedigree (the CEO John Hanke was a co‐founder of Keyhole, which became Google Earth) but also the backing of the technology giant Google/Alphabet from which it spun‐off. And the partnership with Pokémon’s creator, Nintendo, did not hurt either. 

This is one of the relatively few success stories in the world of thousands of game launches every year. The editors and authors of this book have been studying similar games—geogames—and related game mechanics for years now. Successful geogames are born of successful planning, narrative design, technical implementation, marketing, as well as other factors. These can and are being studied in much greater depth at universities around the world. 

When I contacted the editors to ask their opinion on the new Pokémon Go, they took some time to study it deeply and came back with some interesting, detailed ‐ ‐ criticism (and praise). Just as a best selling novel might not be the best written, this hugely popular game had its flaws. Some—excessive personal data collection for example—were picked up by others, and Niantic was forced to make immediate fixes. But the point is that geogames—mobile games in which geographic location of the players is a foundational characteristic—are easier than ever to create; however, creating a _successful_ geogame remains as much an art as a science. 

This book covers many of the key aspects of geogame and geoplay design, implementation, and testing. Of special interest to me are two concepts: geogame patterns and relocation from one context (city) to another. Identifying patterns allows us to more easily abstract and to imagine how new game ideas can fit into an overall structure and therefore borrow or inherit well‐tested ideas from nearby fields or communities. Relocation of a geogame from city to city involves interesting 

v 

vi 

Foreword 

geographic information system (GIS) tasks such as identifying similar places by their geometrical or descriptive characteristics. 

It has been a pleasure to have worked with the editors and with some of the authors over the last few years, in the ideation, testing, and creation of geogames. This book also is the fruit of several workshops on geogames and geoplay, held in locations such as California, Spain, Austria, and Finland, during which very useful feedback was received from a wide range of participants, from programmers to educational psychologists. 

I hope that the reader of this book also provides feedback and actively participates in this nascent community of geogame and geoplay researchers and practitioners. This community will surely grow and prosper in the coming decades and will be able to point to this book as an early anchor or flag planted in the sand. Imagine, create, explore, learn, enjoy. 

Michael Gould Esri, Inc. Redlands, CA, USA University Jaume I Castellón, Spain 

## **Contents** 

- **1 Introducing Geogames and Geoplay: Characterizing an Emerging Research Field** Ola Ahlqvist and Christoph Schlieder 

- **2 Defining a Geogame Genre Using Core Concepts of Games, Play, and Geographic Information and Thinking** Ola Ahlqvist, Swaroop Joshi, Rohan Benkar, Kiril Vatev, Rajiv Ramnath, Andrew Heckler, and Neelam Soundarajan 

- **3 OriGami: A Mobile Geogame for Spatial Literacy** Thomas Bartoschek, Angela Schwering, Rui Li, Stefan Münzer, and Vânia Carlos 

- **4 Spatial Game for Negotiations and Consensus Building in Urban Planning: YouPlaceIt!** Alenka Poplin and Kavita Vemuri 

- **5 Addressing Uneven Participation Patterns in VGI Through Gamification Mechanisms** Vyron Antoniou and Christoph Schlieder 

- **6 Teaching Geogame Design: Game Relocation as a Spatial Analysis Task** Christoph Schlieder, Dominik Kremer, and Thomas Heinz 

- **7 (Re-)Localization of Location-Based Games** Simon Scheider and Peter Kiefer 

- **8 The Design and Play of Geogames as Place- Based Education** Jim Mathews and Christopher Holden 

- **9 A Cost-effective Workflow for Depicting Landscapes in Immersive Virtual Environments** Nathaniel J. Henry 

vii 

viii 

Contents 

- **10  Structural Gamification of a University GIS Course** Michael N. DeMers 

- **11  Geocaching on the Moon** Cheng Zhang 

## **Ludography** 

## **Contributors** 

**Ola Ahlqvist** Department of Geography, The Ohio State University, Columbus, OH, USA 

**Vyron Antoniou** Hellenic Army General Staff/Geographic Directorate, Athens, Greece 

**Emelie Bailey** The Ohio State University, Columbus, OH, USA 

**Thomas Bartoschek** Institute for Geoinformatics, University of Muenster, Muenster, Germany 

**Rohan Benkar** The Ohio State University, Columbus, OH, USA 

**Vânia Carlos** University of Aveiro, Aveiro, Portugal 

**Michael N. DeMers** New Mexico State University, Las Cruces, NM, USA 

**Andrew Heckler** Ohio State University, Columbus, OH, USA 

**Thomas Heinz** University of Bamberg, Bamberg, Germany 

**Nathaniel J. Henry** Ohio State University, Columbus, OH, USA 

**Christopher Holden** University of New Mexico, Albuquerque, NM, USA 

**Swaroop Joshi** Ohio State University, Columbus, OH, USA 

**Peter Kiefer** Institute of Cartography and Geoinformation, ETH Zurich, Zurich, Switzerland 

**Dominik Kremer** University of Bamberg, Bamberg, Germany 

**Rui Li** University at Albany-SUNY, Albany, NY, USA 

**Stefan Münzer** University of Mannheim, Mannheim, Germany 

**Jim Mathews** Field Day Lab, University of Wisconsin, Madison, WI, USA 

**Alenka Poplin** Iowa State University, Ames, IA, USA 

ix 

Contributors 

x 

**Rajiv Ramnath** Ohio State University, Columbus, OH, USA 

**Simon Scheider** Institute of Cartography and Geoinformation, ETH Zurich, Zurich, Switzerland 

Department of Human Geography and Spatial Planning, University Utrecht, Utrecht, Netherlands 

**Christoph Schlieder** University of Bamberg, Bamberg, Germany 

**Angela Schwering** Institute for Geoinformatics, University of Muenster, Muenster, Germany 

**Neelam Soundarajan** Ohio State University, Columbus, OH, USA 

**Kiril Vatev** Ohio State University, Columbus, OH, USA 

**Kavita Vemuri** International Institute of Information Technology, Hyderabad, India 

**Cheng Zhang** NASA Scientific Visualization Studio at Goddard Space Flight Center, Greenbelt, MD, USA 

The Ohio State University, Columbus, OH, USA
