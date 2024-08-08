# 2. Linking Dutch protestant minister data with external sources

With CLERUS in place, various option to link this data with other datasources arrise. By linking protestant ministers with external data like book titles bottom-up reconstruction of trends and changes in thematization can be delivered. Below a description of linking three external data sources is provided. 

## 2.1 Biography portal 
In order to connect individuals from the [Dutch Biography Portal](http://www.biografischportaal.nl/en/) we have been provided with a dump of the data in the form of an excel sheet from the datacurator of this portal. A notbook with which CLERUS is linked with this excel sheet is provided [here](2_1_biography_portal_data.ipynb). The linkage has been done by combining the first letter, with the surname and year of birth. Other options like Levenshtein, as done for [1_6_Boekzaallijst](..\1_Data_Harmonization\1_6_Boekzaallijst.ipynb) would also be possible depending on the user's research purposes. Probably a curation would still be required to be entirely sure it is the same person. 

## 2.2 Linking Book titles
To link book title data with the CLERUS, a series of scripts has been created that first extracts the data from the [Royal Library’s Linked Data SPARQL endpoint](http://data.bibliotheken.nl/sparql) and translates these to separate tables.  
Two notebooks are provided. 

1. A selection of certain attributes from Short-Title Catalogue Netherlands ([STCN](http://data.bibliotheken.nl/doc/dataset/stcn). See [2_2_Export_KB_data_stcn](2_2_Export_KB_data_stcn.ipynb)
2. A selection of attributes from the [Nederlandse Bibliografie Totaal (NBT)](http://data.bibliotheken.nl/doc/dataset/nbt) (which also includes entries from STCN) data. See [2_3_Export_KB_data_nbt](2_3_Export_KB_data_nbt.ipynb)
3. A selection of attributes from the [Nederlandse Bibliografie Totaal (NBT)](http://data.bibliotheken.nl/doc/dataset/nbt) (which also includes entries from STCN) data, where the type of publication is added as well. See [2_4_Export_KB_data_nbt_rdf_types](2_4_Export_KB_data_nbt_rdf_types.ipynb)
4. A selection of attributes from NBT including author information. This export is used in [3_3_clerus_kb](../3_Data_Analysis/3_3_clerus_kb.ipynb). See [2_5_Export_KB_data_nbt_authorinfo](2_5_Export_KB_data_nbt_authorinfo.ipynb)

The linkage with individuals is done based on the First letter, Surname and the year of Birth between the metadata of the Royal Library and CLERUS. This is done in [3_Data_Analysis](../3_Data_Analysis/README.md). 

## 2.3 Enriching location information
In order to allow for spatial analysis a script has been developed based on string matching of place names from [geonames.org](https://www.geonames.org/). See [2_6_geocoder](2_6_geocoder.ipynb). This script functions as an example on what is possible and which location related fields can be connected. 

Depending on the research question, linkages should be made with resources like the historical geometries published by IISG researcher Rombert Stapel: Stapel, Rombert, 2018, "Historical Atlas of the Low Countries (1350–1800)", [https://hdl.handle.net/10622/PGFYTM](https://hdl.handle.net/10622/PGFYTM), IISH Data Collection, V13. 




