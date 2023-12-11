# DigiDuRe
This repository contains code and scripts developed for the [Digital Dutch Religion Portal 1500-2000 project](https://research-software-directory.org/projects/digidure) a project that has been a collaboration between the [Vrije Universiteit Amsterdam, Faculity of Humanities, HDC](https://vu.nl/nl/over-de-vu/diensten/universiteitsbibliotheek/meer-over/collectie-hdc-protestants-erfgoed]) and the [Netherlands eScience Center](www.esciencecenter.nl). The main researcher from the VU is [prof. dr. Fred van Lieburg](https://research.vu.nl/en/persons/fred-van-lieburg), the lead engineer from the escience Center is [Dr. Maurice de Kleijn](https://www.esciencecenter.nl/team/dr-maurice-de-kleijn/).

The project aims to map long-term developments in Dutch public discourse, especially in religion. An analysis of book titles and connected meta-data with multiple other data sources should deliver a bottom-up reconstruction of trends and changes in thematization. To do so three main activities are defined.

1. **Data Harmonzation - Protestant persons**
A structured dataset with carreers of protestant ministers and individuals that passed the exam that allows them to act as protestant minister from 1500 until 2000 needs to be created out of a series of semi-structured datasources that have been generated as a result of archival historical research conducted over the last 30 years. This process is considered data harmonization and entails the modelling of the data structure and a series of processing steps to translate the data from the one format / structure to the other. This results in a new dataset named CLERUS - Database Dutch Reformed Clergy.

2. **Data linking**
In order to analyse book titles in relation to protestant persons, datasets need to be linked. Linking dataset which each other is on the one hand a technical challenge. It entails making sure that the various file formats communicate with each other and that the content of fields overlap. For names the combination of surname, firstname and infix are considered unique, however not every dataset has this combination stored in the same way. Also, variety in name spelling and individuals having the same name is an issue when connecting dataset with other.

The project produces a script which allows to extract various datasets, allowing them to be linked from a technical point. Furthermore, a series of methods to connect the datasets with each other are prepared. Datasource that are connected are the Short-Title Catalogue Netherlands ([STCN]( http://data.bibliotheken.nl/doc/dataset/stcn)) dataset, the Gemeenschappelijk Geautomatiseerde Catalogiseersysteem ([GGC](https://www.oclc.org/nl/ggc.html)). In addition, datasources on individuals are connected from the Dutch Biography Portal ([BP](http://www.biografischportaal.nl/)).

3. **Data Analysis**
Through the connection of the various datasets an analysis of book titles and connected meta-data can be performed which is anticipated to deliver a bottom-up reconstruction of trends and changes in thematization. Though many fields of history will benefit from work in digital history, the focus on religion will stimulate new insights in this subdiscipline.

4. **Dissemination**
A vital part of this project is also to train the history scholars in how to work with data. Therefore, the steps that have been taken in this project are well documented and training material has been produced in which certain concepts are introduced and explained.
Another aspect of the dissemination is that the data can be accessed in various formats. Therefore an additional script is developed to publish the data as linked data.

![Figure 1 shows a schematic overview on the various activities.](/images/figure1.png)


