# Harmonization of data for CLERUS 

The archival corpus of documents about career paths of Dutch Protestant ministers is rich, yet scattered around in multiple archives. Since the 1980s, prof. dr. Fred van Lieburg has initiated multiple projects to systematically collect information about career paths of Dutch Protestant ministers ("predikanten"), focusing on students, persons that passed the exam that allows them to act as Protestant ministers ("proponenten"), and individuals that were actually assigned to a parish ("gemeente" - "predikanten"). 

In order to make these datasets available for analysis, a process of harmonization took place in DiGiDuRe. This means that the various datasets needed to be transferred to interoperable file formats, but more importantly that the various information categories are aligned and structured. Below an overview of the various data sources that form the basis of CLERUS is provided. The process of defining the various fields has been iterative and resulted in a CLERUS database model, a diagram of which can be accessed [here](/0_1_datamodel_CLERUS.md). 

CLERUS consists of a core version and an extended version. The core version of CLERUS is focused on individuals that actually were Protestant ministers in the Netherlands and we are quite confident that it actually contains all Dutch Protestant ministers that acted as such in the Netherlands between 1555 and 2004. 

It also contains information about roles abroad as well as other roles they had during their careers (e.g., professor, school teacher, medical doctor, etc.). However, using that information for analysis purposes should be done with care, since the dataset only contains information about individuals that have acted as Protestant ministers, which means it does not contain individuals that have been, for example, a medical doctor, but not acted as Protestant minister. In addition, we are certain that we have all roles where they acted as Protestant ministers in the Netherlands, but are uncertain about roles abroad. For instance, individuals that had the right to act as Protestant ministers, but never acted as such in the Netherlands, but for instance in the West or East Indies, are not systematically present in CLERUS.  

The extended version of CLERUS, CLERUS+, is focused on all individuals that passed the so-called *proponenten* exam, which gave them the right to act as Protestant ministers. CLERUS+ also includes, for example, individuals that had the right to act as Protestant ministers, but that followed a different career path and ministers that had this function abroad. For CLERUS+, the data model of CLERUS is extended to allow adding information about the so-called proponenten exam (e.g., the location where individuals were registered and when and where their exam took place, etc.). Ideally, CLERUS would contain all individuals that did this *proponenten* exam or were registered as students, however since this data is not yet systematically collected we decided to have CLERUS focused on individuals that acted as Protestant ministers and leave CLERUS+ for the moment that the archival sources have been transcribed (manually or by applying for instance Handwritten Text Recognition (HTR) algorithms). Yet, we do provide a first version of the CLERUS+ data model and diagram based on the data that we have available.



## Data sources for CLERUS

### Datasource 1 - Database Dutch Reformed Clergy (DRC) 1555-1816

The core dataset of CLERUS is the Database Dutch Reformed Clergy (DRC) 1555-1816 (which was available as a word document Repertorium.docx). This dataset contains biographical information and career path information of Dutch Protestant ministers that started after 1555 until the starting date 1816. DRC forms the basis of CLERUS since it is aimed to contain all Protestant ministers that have been assigned to a parish. The year 1816 is set as a cut-off point, meaning that career paths that started before or in 1816 have been included. Ministers that started after 1816 have not been included. The dataset is the result of archival research performed in the context of van Lieburg’s dissertation [van Lieburg, F. A. (1997). Profeten en hun vaderland. De geografische herkomst van de gereformeerde predikanten in Nederland van 1572 tot 1816. [PhD-Thesis - Research and graduation internal, Vrije Universiteit Amsterdam]. Boekencentrum.](https://hdl.handle.net/1871.1/e1bfb2c9-8d30-42b4-8edf-83b20bd6c5a7), and ever since maintained and updated by van Lieburg. DRC contains 12,579 individuals who are semi-systematically registered in a text file (provided as Repertorium.docx).

The processing steps to transform the word document into a relational database are described [here](/1_1_DRC_1555-1816.ipynb). It however appeared that around 5% of the harmonization steps could not be scripted except by single line conversions for which domain knowledge was required, therefore-case specific the dataset 

### Datasource 2 - Dutch Ministers (DM) 1572-2004

The second dataset of CLERUS is teh Dutch Ministers (DM) 1572-2004 (predikantenbestand ca1572-ca2004.accdb) database. This dataset contains information about the careers of Dutch ministers between 1572 and 2004. It overlaps with DRC, but continues after 1816. It has been created by analyzing the archives of parishes / *gemeentes*. It thus has not been focused on individual careers, but on the parishes/ *gemeentes*. Yet, if the registration is correct on its content and spelling, it is possible to derive career paths from this dataset. The processing steps for this harmonization are available [here](/1_2_DM_1572-2004.ipynb).



## Data sources for CLERUS+

### Datasource 3 - Acta der particuliere synoden from 1620 ~ 1735

This data source is constructed by analyzing and transcribing the records from the various *Acta der particuliere synoden*, which are recordings or yearly meetings of Protestant administrative entities (classis). These records are derived from Protestant institutes where students could take their proposition exam which gave them the right to act as Protestant ministers; this however did not mean that these individuals actually chose that career path. Some of them became medical doctors, whereas others chose a career path as university professors or school teachers. The various registrations contain the year of their proposition exam, often followed by their first assignment, which thus does not necessarily is a Protestant minister.

For the construction of the dataset, a start has been made allowing it to distinguish the various data items/fields it contains. As of August 2024, the collection of the data is not yet complete, yet it is clear which data fields it contains, thus can be integrated into the CLERUS+ data model. This data source will form a clear basis for all the individuals in CLERUS. For this data source, no further processing needs to take place since the fields to which the information in this data source are collected have been determined before the data collection takes place, thus no further conversions or data processing need to take place. 

### Datasource 4 - Boekzaallijst 1736 - 1816

This data source is the result of analyzing so-called "Boekzaallijsten" and converting these into structured cards. These cards have been digitized in a structured table. It contains information about when students were registered, when they went for their proposition exam, and where they had their first assignment (if any). In some cases, it also contains information about their second assignment. The dataset has a temporal coverage from 1735-1816. The dataset contains xxx records and has been curated manually in order to identify individuals that are within CLERUS as well. In order to link the individuals from this data source, a joining method using [Levenshtein](https://maxbachmann.github.io/Levenshtein/levenshtein.html#distance) has been applied to facilitate the curation process. The description of this dataset and accompanying script are available [here](/1_4_Boekzaallijst.md). This data source is ready to be integrated into CLERUS, yet it had been decided to not yet include it, since it will generate a strong bias. Also, it would make much more sense to include this data once the Acta data has been transcribed.

### Datasource 5 - Keppel 1747

This data source was recorded in 1747 and gave an overview of all the individuals that acted as Protestant ministers at that moment including the date of their proposition exam. The temporal coverage of the dataset runs from approximately 1700 to 1747. Like Datasource 4, this dataset has not yet been integrated with CLERUS, since it would result in a bias and would much better be done once the Acta data source has been transcribed.

### Datasource 6 - Naamregister 1717-1739

The data source Naamregister provides an overview of all the proposition exams that have been executed between 1717 and 1739. Furthermore, it provided the first role of the proponent. It contains volumes for 1717 to 1739, excluding the years 1729, 1734, and 1735.

For data sources 5 and 6, a process of manual curation has taken place and individuals that are part of CLERUS are identified. A linking and conversion script to CLERUS are relatively straightforward and can be accessed [here](/1_56_Keppel_Naamregister.md).
