# Harmonization of CLERUS.

The archival corpus of documents about carreer paths of Dutch protestantism is rich, yet scattered around in multiple in archives. Since 1980-s prof. dr. Fred van Lieburg has initiated multiple projects to sytematically collect the information about carreer paths of Dutch protestant ministers ("predikanten") focussing at students, persons that passed the exam that allows them to act as protestant minister ("proponenten") and individuals that were actually assigned to a parish ("predikanten"). The various archival data collection project have resulted in a series of datasets which together form the basis for CLERUS. The dataset is the analysis of the different datasets listed below and can be accessed [here](/0_1_datamodel_CLERUS.md).

In order to make these datasets available for analysis, a process of harmonzation needs to be take place. This means that from a technical point of view the datasets need to be integrated into interoperable file formats, but more important that the various information categories are alligned and strucutured. The process of defining the various fields has been iterative, allowing it to identify various expections (every dataset on its own produced new expections and had its own complexity). Based on the analysis of the various datasets a database diagram has been developed for CLERUS.

Below an overview of the various datasources that form the basis of CLERUS is provided. 

## Overview of datasources

The datasources that CLERUS exists of exists of records that have been registered with a different purpose. A distinction can be made between.
1. Registrations on where and when Dutch ministers were assigned to act in a parish. 
2. Registrations of individuals that passed their proposition exam ("proponenten") which allowed them to act as minister 
3. Registrations of students 

### Datasource 1 - Database Dutch Reformed Clergy (DRC) 1555-1816

The first dataset is the Database Dutch Reformed Clergy (DRC) 1555-1816 (stored as Repertorium.docx). This dataset contains biographical information and career path information of Dutch protestent ministers that started after 1555 until the starting data 1816. DRC forms the basis of CLERUS since it is aimed to contain all protestant ministers that have been assigned to a parich. The year 1816 is set as cut-off point, meaning that carreer paths that started before oer in 1816 have been included. Ministers that started after 1816 have not been included. The dataset is the result of archival research performed in the context of van Lieburg´s disseration [van Lieburg, F. A. (1997). Profeten en hun vaderland. De geografische herkomst van de gereformeerde predikanten in Nederlamd van 1572 tot 1816. [PhD-Thesis - Research and graduation internal, Vrije Universiteit Amsterdam]. Boekencentrum.](https://hdl.handle.net/1871.1/e1bfb2c9-8d30-42b4-8edf-83b20bd6c5a7), and ever since maintained and updated by van Lieburg. DRC contains 12579 individuals which are systematically registered in a text file.

The datasource is semi-structerd and stored as a text file. The processing steps to transform this into a relational database are described [here](/1_1_DRC_1555-1816.md).

### Datasource 2 - Dutch Ministers (DM) 1572-2004

The second dataset of CLERUS is Dutch Ministers (DM) 1572-2004 (predikantenbestand ca1572-ca2004.accdb). This dataset contains information about the carreers of Dutch ministers between 1572 and 2004. It thus overlaps with DRC, but goes beyond 1816. It has been created be by analysing the archives of parishes. It thus has not been focused at the individual carreers, but on the parished. Yet, if the registration is correct on its content and spelling, it is possible to derive carreer path form this dataset. The processing steps for this harmonization are available [here](/1_2_DM_1572-2004.md)

### Datasource 3 - Acta der particuliere synoden from 1620 ~ 1735 
This datasource is constructed by anaylysing and transcribing the records from the various Acta. These records are derived from protestant institutes where students could take their proposition exam which give them the right to act as protestant minister, this however did not mean that these individuals actually choose that carreer path. Some of them became medical doctors, whereas others choose a carreer path as university professor. The various registrations contain the year of their of proposition exam, often followed by their fist assignment (which can be post as minister or another role).

For the construction of the dataset a start has been made allowing it to distinguish that various data items / fields it contains. The moment of writing, December 2023, the collection of the data is not yet complete, yet it is clear which datafields it contains, thus can be integrated into the CLERUS datamodel. This datasource will form a clear basis for all the individuals in CLERUS. For this datasource no further prossessing needs to take place, since the fields to which the information in this datasource are collected have been determined before the data collection takes place, thus no further conversions or data processing needs to take place. Yet a processing description on how to collect and integrate the data can be accessed [here](/1_3_Acta.md)

### Datasource 4 - Boekzaallijst 1736 - 1816
This datasource is the result of analysing so called "Boekzaallijsten" en converting these into structered cards. These cards have been digitized in a structured table. It contains information about when students were registered, when they went for their proposition exam and where they has their first assignment (if any). In some cases it also contains information about their second assignment. The dataset has a temporal coverage form 1735-1816. The dataset contains xxx records and have been curated manually in order to identify individuals that are within DRC as well. In order to link the individuals from this datasource a joining method using [Levenshtein](https://maxbachmann.github.io/Levenshtein/levenshtein.html#distance) has been applied to facilitate the curation process. The description of this dataset and accompanying script are available [here](/1_4_Boekzaallijst.md). 


### Datasource 5 - Keppel 1747

This datasource is a recorded in 1747 and gave an overview of all the individuals that acted as protesetant minister at that moment including the date of their proposition exam. The temporal coverage of the dataset goes runs from approximately 1700 to 1747. 

### Datasource 6 - Naamregister 1717-1739

The datasource Naamregister provides and overview on all the proposition exams that have been executed between 1717 and 1739. Futhermore, it provided the first role of the proponent. It contains volumes for 1717 to 1739, excluding the years 1729, 1734 and 1735.

For datasources 5 and 6 a process of manual curation has taken place and individuals that are part of DRC are identified. Therefore a description script and conversion script to CLERUS are relative straightforward and can be accessed [here](/1_56_Keppel_Naamregister.md)




