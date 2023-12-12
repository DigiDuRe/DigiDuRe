# Connecting dataset from Biography portal of the Netherlands to RAN

In order to connect inidividuals from the [Dutch Biography Portal](http://www.biografischportaal.nl/en/) we have been given an excel sheet from the datacurator from behind this portal. The dataset we have been provided with contains the following fields.

|Fieldname | Description|
|----|---|
|Badge| internal badge id|
|Bioport_id| unique id in bioportal to link it to other datasources |
|Person_id|unique id of individual|
|prepositie| preposition, an official title like duke or dr.|
|voornaam| first name|
|intrapositie| infix |
|pnv_infixTitle| infix title |
|geslachtsnaam| surname |
|postpositie| postposition |
|person_sex| gender |
|VIAF_id_1| Virtual International Authority File Id to link with other datasources |
|VIAF_id_2| Virtual International Authority File Id to link with other datasources when a second is known |
|Wikidata_id| Id to wikidata |
|event_birth_when| Birth date |
|event_birth_text| additional information about the birth, mostly date of baptism | 
|event_birth_place| place of birth or baptism |
|event_death_when| date of death |
|event_death_text| additional information about the death, e.g. date of funeral |
|event_death_place| place of death or burial | 
|category-1| category for which the inidivual was known for |
|category-2| second category for which the inidivual was known for |
|category-3| additional category for which the inidivual was known for |
|category-4| additional category for which the inidivual was known for |
|religion| information about the relgion of an individual |

*Table 1 - fields Dutch Biography portal*

To link individuals from the our dataset with this portal we looked at the first letter of the name, the infix, the surname and the year of birth.

From CLERUS these are the first letter from name followed by infix, surname and year_birth. From BP these are the first letter of voornaam, intrapositie, geslachtsnaam, event_birth_when. For event_birth_when the first 4 digital number has been isolated assuming that is the year of birth.

For field where these corresponded we have created a list containing the Bioport_id and clerus_id. In total this resulted in 1199 matches between the biography portal and the CLERUS created in [activity 1](../act1). 

The script that executed this analysis can be found [here](../act1/biography_portal_data.ipynb) in the form of a Jupyter Notebook.






....
