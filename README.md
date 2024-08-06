# DigiDuRe

This repository contains code and scripts developed for the [Digital Dutch Religion Portal 1500-2000 project](https://research-software-directory.org/projects/digidure), a collaboration between the [Vrije Universiteit Amsterdam, Faculty of Humanities, HDC](https://vu.nl/nl/over-de-vu/diensten/universiteitsbibliotheek/meer-over/collectie-hdc-protestants-erfgoed) and the [Netherlands eScience Center](https://www.esciencecenter.nl). The main researcher from the VU is [prof. dr. Fred van Lieburg](https://research.vu.nl/en/persons/fred-van-lieburg), and the lead research software engineer from the Netherlands eScience Center is [Dr. Maurice de Kleijn](https://www.esciencecenter.nl/team/dr-maurice-de-kleijn/).

The project aims to map long-term developments in Dutch public discourse, especially in religion. An analysis of book titles and connected metadata with multiple other data sources should deliver a bottom-up reconstruction of trends and changes in thematization. To do so, four main activities are defined.

![Figure 1 shows a schematic overview of the various activities.](/images/figure1.png)
*Overview of the various activities in DigiDuRe*

## 1. Data Harmonization - Protestant individuals

A structured dataset with careers of Dutch Protestant ministers from 1555 until 2004 is created out of a series of semi-structured data sources that are the result of archival historical research. This process is considered data harmonization and entails the modeling of the data structure and a series of processing steps. The processing steps are available as Jupyter notebooks and are grouped under [1_Data_Harmonization](/1_Data_Harmonization/). On top of the data harmonization, a curation process took place as well, especially since multiple data sources with information from the same individual have been integrated and contained differences in spelling. This process has resulted in a new dataset named **CLERUS - Database Dutch Reformed Clergy**, where the emphasis lies on ministers that have served in Dutch churches. The database and data model could be extended with data from ministers that were active in other countries (i.e., in the West and East Indies), as well as information about individuals that obtained the right to act as Protestant ministers (proponenten) but followed a different career path (e.g., school teacher, professor, medical doctor, etc.).

## 2. Linking and Enriching Data

To use book title data with the CLERUS, a script has been created that extracts the data from the [Royal Library’s Linked Data SPARQL endpoint](http://data.bibliotheken.nl/sparql) and translates that to separate tables. The main reason for this is that the digital skill level of the target audience did not match the required skill level needed for using Linked Data. In addition, the history scholars participating in this project want to be able to store the dataset locally and have the opportunity to manipulate it. [2_Linking_data](/2_Linking_data/) thus consists of a script that allows downloading data from the Royal Library’s SPARQL endpoint to extract a selection from the Short-Title Catalogue Netherlands ([STCN](http://data.bibliotheken.nl/doc/dataset/stcn)) dataset and the [Nederlandse Bibliografie Totaal (NBT)](http://data.bibliotheken.nl/doc/dataset/nbt).

Linking CLERUS with the book title datasets is challenging since the spelling of names in both datasets does not always align, and since in many cases people have been given the same names. Chapter [2_Linking_data](/2_Linking_data/) also provides a script that links CLERUS with the book title data.

Besides linking book title data, a script that connects CLERUS with the Dutch Biography Portal ([BP](http://www.biografischportaal.nl/)) is made. Furthermore, a geocoding script has been developed to link place names in CLERUS (e.g., places of birth and where certain individuals acted as ministers, etc.) to XY coordinates allowing them to be plotted on a map.

## 3. Data Analysis

With the CLERUS dataset available, a series of analysis scripts have been developed to explore the data and add to the analysis of book titles, allowing for a bottom-up reconstruction of trends and changes in thematization. These analysis scripts can be found under [3_Data_Analysis](/3_Data_Analysis/).

## 4. Dissemination

During the project, it has been presented on many occasions. Under [4_Dissemination](/4_Dissemination/), slide decks can be found, as well as installation instructions for the software used.
