# DigiDuRe
This repository contains code and scripts developed for the [Digital Dutch Religion Portal 1500-2000 project](https://research-software-directory.org/projects/digidure).

The project aims to map long-term developments in Dutch public discourse, especially in religion. To do so, it will link the Short-Title Catalogue Netherlands ([STCN]( http://data.bibliotheken.nl/doc/dataset/stcn)) dataset, the Gemeenschappelijk Geautomatiseerde Catalogiseersysteem ([GGC](https://www.oclc.org/nl/ggc.html)), the Dutch Biography Portal ([BP](http://www.biografischportaal.nl/)), the Repertorium Academicum Neerlandicum (RAN ~ not available in the public domain) and various other open-access databases. 
Through a connection between the various datasets an analysis of book titles and connected meta-data can be performed which is anticipated to deliver a bottom-up reconstruction of trends and changes in thematization. Though many fields of history may profit from this experiment in digital history, the focus on religion will stimulate innovations in this subdiscipline.

## Overview of activities within the project

Roughly the project can be divided in five core activities. 

1. **Data Harmonization:** First, the various data sources need to harmonized. It must become clear how the various datasets can be connected and what possible conversions need to be made in order to do so. As a first step we therefore aim to map the various database schemas that we want to connect. Once the database schemas are clear, the technical steps need to be taken to actually link the various datasets in order for them to be linked and enriched.
2. **Data Analysis**: The moment the datasets are linked/connected, a series of analysis methods can be performed. Queries combined with statistic and or network analysis methods will be applied to identify relevant connections in the datasets. 
3. **Dissemination**: The knowledge from the previous steps will be disseminated allowing these to be reproduced by other scholars. 
4. **Long Term Sustainability**: Finally, all the scripts for harmonization and analyses need to be stored in a sustainable manner allowing it to be reused.

![Figure 1 shown a schematic overview on the various activities and shows that the activities are nonlinear, meaning that especially between the data harmonization and data analysis phase iterations will take place.](/images/figure1.png)


Given the number of datasets that the projects aims to integrate, the steps above will not be taken in a linear way. Instead, the activities will be performed in an iterative manner. Meaning that we are first going to link two datasets and perform a series of analyses (going through steps 1-3), followed by integrating another dataset and later on another one etc. . 

### Datasets that are envisioned to be used in the project are

i. Repertorium Academicum Neerlandicum (not available in the public domain)

ii. Gemeenschappelijk Geautomatiseerde Catalogiseersysteem [GGC](https://www.oclc.org/nl/ggc.html)

iii. the Dutch Biography Portal [BP](www.biografischportaal.nl/)

iv.  Short-Title Catalogue Netherlands [STCN](http://data.bibliotheken.nl/doc/dataset/stcn)



Furthermore, we envision that a link will be made with [Dutch Historical Dictionaries](https://ivdnt.org/woordenboeken/historische-woordenboeken/#historical-dictionaries)

In addition, a link with the [churches database 1800-1970] (https://geoplaza.vu.nl/cms/projectportfolio/kerkenkaart-2/) and the [monastries](https://geoplaza.vu.nl/cms/projectportfolio/kloosterkaart/) database is likely to be made and will be explored.

## Data Harmonization

### Activity 1. Harmonization of Repertorium Academicum Neerlandicum (RAN). 
As part of the data harmonization phase, two datasets need to be integrated which together form the Repertorium Academicum Neerlandicum. Database Dutch Reformed Clergy 1555-1816 (Repertoriummetoudepersoonsnummers.docx) and Dutch Ministers 1572-2004 (predikantenbestand ca1572-ca2004.accdb)

The first dataset is the Database Dutch Reformed Clergy 1555-2004 (Repertoriummetoudepersoonsnummers.docx) provided by the lead applicant. This dataset contains biographical information and career path information of Dutch ministers that started after 1555 until the starting data 1816. This means that it does contain careers that continue after 1816. The dataset contains 12558 individuals which are systematically registered in a text file of which a sample is provided below. 

> Aalst; Wilhelmus
> Gedoopt Biggekerke 5 jan. 1664; pred. Aardenburg 22 mei 1695, overl. 19 dec. 1700.<4>
>
> Aalst, van; Cornelius
> Geb. Castricum ca. 1686; ambassadepred. in Parijs maart tot dec. 1715; pred. Kalslagen ber. 21 febr. 1717, emer. 1751; overl. Amsterdam 27 aug. 1756.<2>
> 
> Aalst, van; Gerardus
> Geb. xxx sept. 1678; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, emer. 1755; overl. 29 juni 1759.<3>

In its current form it is not possible to for instance categorize persons based on the place that they were born or years that they were active in a certain church. Therefore, the first steps that need to be taken is to map the dataset into a relation database (RD). By doing so a series of basic and more analysis methods will become present. Putting it into a RD would allow to for instance make a sub- selection of persons that were active in a specific decade in a certain province. Furthermore, it allows for more complex analyses such as network analysis to see which individuals lived near to each other and eventually allowing it to be linked with other datasets such as STCN.

[On the following page the process of converting the RAN into a RD are described in detail.](/act1/convert_RAN_RD.md) 
