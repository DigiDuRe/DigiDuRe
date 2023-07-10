# Activity 1. Harmonization of Database Dutch Reformed Clergy (DDRC).

As part of the data harmonization phase, two datasets need to be integrated which together form the Database Dutch Reformed Clergy 1555-1816 dataset (Repertoriummetoudepersoonsnummers.docx) and Dutch Ministers 1572-2004 dataset(predikantenbestand ca1572-ca2004.accdb).

## Dataset 1 - Database Dutch Reformed Clergy (DDRC) 1555-1816
The first dataset is the Database Dutch Reformed Clergy 1555-2004 (stored as Repertoriummetoudepersoonsnummers.docx) provided by the lead applicant. This dataset contains biographical information and career path information of Dutch ministers that started after 1555 until the starting data 1816. This means that it does contain careers that continue after 1816. The dataset contains 12558 individuals which are systematically registered in a text file of which a sample is provided below.

> Aalst; Wilhelmus Gedoopt Biggekerke 5 jan. 1664; pred. Aardenburg 22 mei 1695, overl. 19 dec. 1700.<4>
>
> Aalst, van; Cornelius Geb. Castricum ca. 1686; ambassadepred. in Parijs maart tot dec. 1715; pred. Kalslagen ber. 21 febr. 1717, emer. 1751; overl. Amsterdam 27 aug. 1756.<2>
>
> Aalst, van; Gerardus Geb. xxx sept. 1678; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, emer. 1755; overl. 29 juni 1759.<3>
>

In its current form it is not possible to for instance categorize persons based on the place that they were born or years that they were active in a certain church. Therefore, the first steps that need to be taken is to map the dataset into a relation database (RD). By doing so a series of basic and more analysis methods will become present. Putting it into a RD would allow to for instance make a sub- selection of persons that were active in a specific decade in a certain province. Furthermore, it allows for more complex analyses such as network analysis to see which individuals lived near to each other and eventually allowing it to be linked with other datasets such as STCN.

# Conversion steps Database Dutch Reformed Clergy 1555-2004 text file into RD.

Below a simplified workflow on the transformation steps that are taken to transform the text file into a RD is provided. The jupyter notebook provides the actual code.

The overall principle for the steps that have been taken is that the information of an individual is stored on a single line and that all characteristics are parsed into separate columns. This is done by adding a semicolon ; between distinguishable items. 

### Step 1.
To get alle the information of the file into single rows per individual the first step was to remove all the enters in the file so that all the information of an individual is stored in a single row. Since all the individuals have a unique ID structured as <x> where x is the id. The next step thus was to add an enter after every ID creating a file that has information of every individual in a single row. 

> Aalst, van; Cornelius Geb. Castricum ca. 1686; ambassadepred. in Parijs maart tot dec. 1715; pred. Kalslagen ber. 21 febr. 1717, emer. 1751; overl. Amsterdam 27 aug. 1756.<2>
> Aalst, van; Gerardus Geb. xxx sept. 1678; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, emer. 1755; overl. 29 juni 1759.<3>

### Step 2.
To isolate the IDs into a column once read as a .csv file a semicolon is added in front of the < and after the > sign. 

### Step 3. 
In the original dataset the various characteristics of an individual are distinguished using s semicolon. However, this is not done in a systematic way (e.g Geb. and  emer. Are not separated with a semicolon. Therefore, a search on the various distinguishable key strings is performed and a semicolon is added. Key strings that we searched for are: 

``` "Geb.","pred.","overl.","Gedoopt","legerpred.","pastoor","garnizoenspred.","emer.","begraven","conrector","rector","monnik","schoolmeester","hoogleraar","chirurgijn","praeceptor","ziekentrooster","vlootpred.","legerpred.","ambassadepred." ```

By added a “; ” in front of these key strings the various will be handled as separate columns when imported as .csv file.

> Aalst, van; Cornelius ; Geb. Castricum ca. 1686; ; ambassadepred. in Parijs maart tot dec. 1715; ; pred. Kalslagen ber. 21 febr. 1717, ; emer. 1751; ; overl. Amsterdam 27 aug. 1756.;<2>;
> Aalst, van; Gerardus ; Geb. xxx sept. 1678; ; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, ; emer. 1755; ; overl. 29 juni 1759.;<3>;

### Step 4.
When importing this dataset, it will create a lot of empty cells and obviously does not structure the data according to the distinguishable key string. Therefor the next step is to create columns based on the key strings and add information from cells that contain the key string into that column. To improve the readability of the information in the new columns the key strings are also removed. 

In the example information about Cornelius´s death will be stored into column **overl.** and will initially contain the value *“ overl. 29 juni 1759.”*, however once the distinguishable string is removed from the cell it will contain as value *“29 juni 1759.”*.  

An important issue here is that in some cases the distinguishable key string is used multiple times for an individual. For ministers this issue has been solved by counting the number of time the string “ pred.” is in a line and add a number to the position. These are later on integrated into one cell called minister. 

### Step 5. 
In order to make the various field into understandable entities, the names of the columns have been translated as follows.

```python
'Geb.': 'birth', 
    ' pred.': 'minister', 
    'overl.': 'death', 
    'Gedoopt':'baptized', 
    'legerpred.':'legerpredikant',
    'pastoor':'pastoor',
    'garnizoenspred.':'garnizoenspredikant',
    "emer.":'emeritus_status',
    "begraven":'burried',
    "conrector":'conrector',
    " rector":'rector',
    "monnik":'monnik',           
    "schoolmeester":'schoolmeester',
    "hoogleraar":'hoogleraar',
    "chirurgijn":'chirurgijn',
    "praeceptor":'praeceptor',
    "ziekentrooster":'ziekentrooster',
    "vlootpred.":'vlootpredikant',
    "legerpred.":'legerpredikant',
    "ambassadepred.":'ambassadepredikant'}
```

### Step 6. 
The surnames and names of the individuals in the dataset are always stored in the first and second column of the dataset. When the text file has been imported as csv, the information in these columns have been called accordingly. These field also contain nicknames individuals have been given and possible information about family relations. In the original text files all information about nicknames is provided between ( ) and about family relationships between [ ]. As a next step we thus have cutted information between ( ) in the field “name” into a new field called “name_info_family” and from “surname” information between [ ] into a new field called “nickname”. Now that the additional information is moved from the name and “surname” column, the infixes of the various individuals can be isolated by searching for a comma in the column “surname”.  

### Step 7.
Since an individual might have had multiple positions as minister, the relation between an individual and a role is considered one-to-many. The process above added all the information of a minister career into one field, where every new location and year is distinguished by a , . The next step has therefore been to isolate the information from the column “minister” into a new table where every role has a separate row contain the unique ID (step 2) and the information about the role. 

### Step 8. 
In order to isolate the year and for instance the place names in the distinguishable key strings (listed under step 3 and step 5) a search is done on 4 number digits in the field of the various columns and a new column is created with the string “year_“+ distinguishable key string added to the fieldname. Furthermore, a search is performed looking for the string “ca.”, which stands for “circa” and once found the word “circa” is added to the a new field “accu_year_”+ distinguishable key string. To isolate the place names, all information about a possible date and strings xxx and yyy have been removed. (this information is only available for a limited sample, we have therefore decided to keep that information in the original field and remove it here.

For instance:
> Aalst, van; Cornelius Geb. Castricum ca. 1686; ambassadepred. in Parijs maart tot dec. 1715; pred. Kalslagen ber. 21 febr. 1717, emer. 1751; overl. Amsterdam 27 aug. 1756.<2>
> Aalst, van; Gerardus Geb. xxx sept. 1678; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, emer. 1755; overl. 29 juni 1759.<3>

Will result in following:
| id  | surname | infix | name | birth | year_birth | accu_year_birth | ... | ... | etc. |
|---|---|---|---|---|---|---|---|---|---|
| 2 |	Aalst |	van	| Cornelius	| Castricum	| 1686	|circa | | | |				
| 3	| Aalst	| van |	Gerardus |	|	1678	|	|	|	|	|

NB: Step 8 has also been performed for the child table produced for ministers under step 7.  

The jupyther notebook that converts the textfile into a relational database can be accessed [here](/conversion_text_to_table_minister.ipynb)

# Dataset 2 - Dutch Ministers (DM) 1572-2004

Besides dataset 1, presented above, an integration with another dataset, Dutch Ministers (DM) 1572-2004 (predikantenbestand ca1572-ca2004.accdb) containing information about the careers, needs to be made as well. The dataset that needs to be integrated has been created by one of Van Lieburg´s student assistants in the past and is said to **contain more up to date information** where individuals acted as ministers. The dataset contains the careers of the various ministers and tells where they have acted as “predikant” (minister). The data is stored as a separate table where every moment a new position as minister was taken have been stored in a separate row (figure 2). In case an individual had more positions as minister in its career this dataset contains multiple rows for that individual. For instance, Isaäc Abbema in the example had two posts one from 1618 to 1635 in Berkenwoude and from 1635 to 1637 in Gouda.  

![Figure 2 Dutch Ministers 1572-2004](/images/figure2.png)

**Figure 2 Dutch Ministers 1572-2004**

Contrary to Dataset 1/ DDRC, this dataset also contains data about ministers that started their careers after 1815. For the DDRC van Lieburg (the Lead Applicant of the project) wants to use this dataset as the starting point for the individual ministers. However, something that makes this dataset complicated to work with is that over time people had the same name and individuals are not easily distinguishable since no unique ID is provided. Yet, the Lead applicant is certaOut of the 53646 records this dataset contains, 25082 times exactly the same name is used. However, counting the number of times a name is used, where every count would be a step in its career, results in unfeasible career paths. J. de Jong would have had 30 positions over an unfeasible long period of time. Looking closely at the dataset “J. de Jong” appears to be a name that, not surprisingly in the Netherlands, represents multiple individuals. 

![Figure 3](/images/figure3.png)

As a strategy in this harmonization process we have decided to take the DDRC as a starting point. To take DM as starting point is currently not feasible, since individuals are difficult to distinguish. However taking DDRC as a starting point is also difficult since the locations where ministers were stationed seems to be not accurate. We have therefore made a join between locations that came out of the notebook above on the combination name, infix, surname, placename, year and counted the number of ministers where these where exactly the same. Next we compared the number of identical positions minister had in DDRC and DM that exactly matched (thus where name, infix, surname, placename and year are identical). By comparing the counts of fields there are exactly the same with each other we are able to see if the individual ministers in DDRC are complete. For those where the number of matching positions do not match a database is created that needs to be curated.

However before performing this harmonzation step, the DM needs to be cleaned. A thorough analysis scan of the dataset revealed a series of errors listed below. 
-	Information is stored in wrong column. 
-	Spaces in front of name (make it difficult to link)
-	; between name and surname is lacking, making it at a later stage difficult to split these
-	Many individuals have only one value in the field predikant, making it difficult to link these thus it is difficult to distinguish surname or name 

A round of corrections has been executed and produced an updated list. Furthermore, it contains 131 records that still needs to be checked. This however does not mean that the rest of the file does not contain any errors. This data cleaning only looked at the following issues:
-	whether “jaar intrede” has a numeric value
-	“predikant” does not start with a number
-	how many semicolons there are in field “predikant” (and if not 1 put in the list to check)
-	whether “predikant” starts with a space

With this cleaned dataset the datasets from DM and DDRC are checked. The script that we developed for this can be accessed [here](/db_check_id.ipynb) 
  
