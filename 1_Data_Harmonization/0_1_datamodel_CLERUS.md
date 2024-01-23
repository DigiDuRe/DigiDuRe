# Data model CLERUS

The development of the data model for CLERUS has been a dynamic process. Initially we applied a top down approach in which we defined all the various field that we would want it to exist. However in the process of the datacollection it appeared that the various datasets which are integrated for CLERUS did not contain the requested information.

The datamodel that has been created can be accessed [here](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=CLERUS_design.drawio#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FMorrizzzzz%2FDigiDuRe%2Fmain%2F1_Data_Harmonization%2FCLERUS_design.drawio).

The database exists of seven tables. At the core of the database the table **01_clerus_bio** is put with the basic biographical information about an individual. it contains for instanc the name, surname, year of birth, year of death etc. for every person. The information from  **01_clerus_bio** is rather generic and is in theory not bound ministers only. Making a distinction between generic data and more contextual data is a deliberate decision in the design of the datamodel.

A SQL code to create **01_clerus_bio** is provided below.

```sql

DROP TABLE IF EXISTS "01_clerus_bio";

CREATE TABLE "01_clerus_bio" (
  "clerus_id" INTEGER,                              --Unique identifyer and primary key in the database
  "first_name" TEXT,                                --First name
  "infix" VARCHAR(255),                             --infix of name
  "surname" VARCHAR(255),                           --surname
  "initials" VARCHAR(255),                          --initials
  "sex" VARCHAR(255),                               --sex
  "info_family" TEXT,                               --information about familiy relations. For instance son of (Z.V. Zoon Van or brother of etc.)
  "birth_place" TEXT,                               --place of birth
  "birth_place_id" INTEGER DEFAULT 0,               --place of birth id to allow for adding alternative spellings for the placename 13_birth_place
  "birth_year" INTEGER,                             --year of birth
  "birth_date_exact" INTEGER DEFAULT 0,             --exact date of birth ddmmyyyy
  "birth_year_accuracy" VARCHAR(255),               --comments about the accuracy of the birth date e.g. circa , ca. etc.
  "baptism_place" VARCHAR(255),                     --place of baptism
  "baptism_place_id" INTEGER DEFAULT 0,             --place of baptism id to allow for adding alternative spellings for the placename 14_baptism_place
  "baptism_year" INTEGER,                           --year in which the baptism took place
  "baptism_date_exact" INTEGER DEFAULT 0,           --exact date of the baptism
  "baptism_date_accuracy" VARCHAR(255),             --comments about the accuracy of the baptism date e.g. circa , ca. etc.
  "death_place" VARCHAR(255),                       --place of death
  "death_place_id" INTEGER DEFAULT 0,               --place of death id to allow for adding alternative spellings for the placename in 15_death_place
  "death_year" INTEGER,                             --year of death
  "death_date_exact" INTEGER DEFAULT 0,             --exact date of death
  "death_date_accuracy" VARCHAR(255),               --comments about the accuracy of the death date e.g. circa , ca. etc.
  "burried_place" VARCHAR(255),                     --place where someone is burried
  "burried_place_id" INTEGER DEFAULT 0,             --id for place where someone is burried to allow for adding alternative spellings for the placename in 16_burried_place
  "funeral_year" INTEGER DEFAULT 0,                 --year of funeral
  "funeral_date_exact" INTEGER DEFAULT 0,           --exact date of funeral
  "funeral_data_accuracy" VARCHAR(255),             --comments about the accuracy of the death date e.g. circa , ca. etc.
  "remarks" TEXT,                                   --remarks about the individual
  "remarks_source" TEXT,                            --remarks about the source (e.g. a reference to a source)
);
```
As a one to one relationship with **01_clerus_bio** the table **02_drc_org** is installed. This table contains the original input form the [DRC text file](1_1_DRC_1555-1816.ipynb). The reason to not integrate this into **01_clerus_bio** is because in the final version of CLERUS this field will not be filled for every individual since it will also contain information from for instance [DM](1_2_DM_1572-2004.ipynb). This is also in line with the database design strategy to make a distinction between generic and more contextual data.

```sql
DROP TABLE IF EXISTS "02_drc_org";

CREATE TABLE "02_drc_org" (
  "drc_id" INTEGER,                                 --Key the corresponds with the clerus_id in 01_clerus_bio
  "original_input_drc" TEXT                         --The original input text string from DRC
);
```

clerus exam

--
-- Table structure for table '03_clerus_exam'
--

DROP TABLE IF EXISTS "03_clerus_exam";

CREATE TABLE "03_clerus_exam" (
  "clerus_id" VARCHAR(255),
  "prep_exam_classis" VARCHAR(255),
  "prep_exam_date_exact" INTEGER DEFAULT 0,
  "prep_exam_year" VARCHAR(255),
  "prop_exam_classis" VARCHAR(255),
  "prop_exam_date_exact" INTEGER DEFAULT 0,
  "prop_exam_date_year" INTEGER DEFAULT 0,
  "commendati_classis" VARCHAR(255),
  "commendati_classis_date_exact" INTEGER DEFAULT 0,
  "commendati_classis_year" INTEGER DEFAULT 0
);

--
-- Table structure for table '11_clerus_alt_name'
--

DROP TABLE IF EXISTS "11_clerus_alt_name";

CREATE TABLE "11_clerus_alt_name" (
  "clerus_id" INTEGER,
  "alt_name" TEXT,
  "alt_first_name" VARCHAR(255),
  "alt_infix" VARCHAR(255),
  "alt_surname" VARCHAR(255),
  "alt_info_family" VARCHAR(255),
  "remarks_alt_name" TEXT,
  "alt_initials" VARCHAR(255)
);

--
-- Table structure for table '12_clerus_role'
--

DROP TABLE IF EXISTS "12_clerus_role";

CREATE TABLE "12_clerus_role" (
  "clerus_id" INTEGER,
  "role_type" VARCHAR(255),
  "role_place" TEXT,
  "role_place_id" INTEGER DEFAULT 0,
  "role_classis_code" INTEGER DEFAULT 0,
  "role_classis" VARCHAR(255),
  "role_parish" VARCHAR(255),
  "role_province" VARCHAR(255),
  "role_region" VARCHAR(255),
  "role_start_year" INTEGER,
  "role_start_date_exact" INTEGER DEFAULT 0,
  "role_start_year_accuracy" VARCHAR(255),
  "role_end_year" INTEGER DEFAULT 0,
  "role_end_date_exact" INTEGER DEFAULT 0,
  "role_end_year_accuracy" VARCHAR(255),
  "role_residence_place" VARCHAR(255),
  "role_residence_place_id" INTEGER DEFAULT 0,
  "role_remarks" TEXT
);

--
-- Table structure for table '13_clerus_place'
--

DROP TABLE IF EXISTS "13_clerus_place";

CREATE TABLE "13_clerus_place" (
  "birth_place_id" INTEGER DEFAULT 0,
  "baptized_place_id" INTEGER DEFAULT 0,
  "death_place_id" INTEGER DEFAULT 0,
  "burried_place_id" INTEGER DEFAULT 0,
  "role_place_id" INTEGER DEFAULT 0,
  "role_place_residence_id" INTEGER DEFAULT 0,
  "alt_place_name" VARCHAR(255)
);







