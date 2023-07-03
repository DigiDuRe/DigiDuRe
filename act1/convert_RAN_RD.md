# Conversion steps Database Dutch Reformed Clergy 1555-2004 text file into RD.
Below a simplified workflow on the transformation steps that are taken to transform the text file into a RD is provided.

A jupyter nodebook containing all the details can be accessed [here](act1/conversion_text_to_tables_minister.ipynb)

The overall principle for the steps that have been taken is that the information of an individual is stored on a single line and that all characteristics are parsed into separate columns. This is done by adding a semicolon ; between distinguishable items. 

## Step 1.
To get alle the information of the file into single rows per individual the first step was to remove all the enters in the file so that all the information of an individual is stored in a single row. Since all the individuals have a unique ID structured as <x> where x is the id. The next step thus was to add an enter after every ID creating a file that has information of every individual in a single row. 

> Aalst, van; Cornelius Geb. Castricum ca. 1686; ambassadepred. in Parijs maart tot dec. 1715; pred. Kalslagen ber. 21 febr. 1717, emer. 1751; overl. Amsterdam 27 aug. 1756.<2>
> Aalst, van; Gerardus Geb. xxx sept. 1678; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, emer. 1755; overl. 29 juni 1759.<3>

## Step 2.
To isolate the IDs into a column once read as a .csv file a semicolon is added in front of the < and after the > sign. 

## Step 3. 
In the original dataset the various characteristics of an individual are distinguished using s semicolon. However, this is not done in a systematic way (e.g Geb. and  emer. Are not separated with a semicolon. Therefore, a search on the various distinguishable key strings is performed and a semicolon is added. Key strings that we searched for are: 

``` "Geb.","pred.","overl.","Gedoopt","legerpred.","pastoor","garnizoenspred.","emer.","begraven","conrector","rector","monnik","schoolmeester","hoogleraar","chirurgijn","praeceptor","ziekentrooster","vlootpred.","legerpred.","ambassadepred." ```

By added a “; ” in front of these key strings the various will be handled as separate columns when imported as .csv file.

> Aalst, van; Cornelius ; Geb. Castricum ca. 1686; ; ambassadepred. in Parijs maart tot dec. 1715; ; pred. Kalslagen ber. 21 febr. 1717, ; emer. 1751; ; overl. Amsterdam 27 aug. 1756.;<2>;
> Aalst, van; Gerardus ; Geb. xxx sept. 1678; ; pred. Vuren en Dalem 10 aug. 1704, Sommelsdijk 13 juni 1706, West Zaandam 4 aug. 1715, ; emer. 1755; ; overl. 29 juni 1759.;<3>;

## Step 4.
When importing this dataset, it will create a lot of empty cells and obviously does not structure the data according to the distinguishable key string. Therefor the next step is to create columns based on the key strings and add information from cells that contain the key string into that column. To improve the readability of the information in the new columns the key strings are also removed. 

In the example information about Cornelius´s death will be stored into column **overl.** and will initially contain the value *“ overl. 29 juni 1759.”*, however once the distinguishable string is removed from the cell it will contain as value *“29 juni 1759.”*.  

An important issue here is that in some cases the distinguishable key string is used multiple times for an individual. For ministers this issue has been solved by counting the number of time the string “ pred.” is in a line and add a number to the position. These are later on integrated into one cell called minister. 

## Step 5. 
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

## Step 6. 
The surnames and names of the individuals in the dataset are always stored in the first and second column of the dataset. When the text file has been imported as csv, the information in these columns have been called accordingly. These field also contain nicknames individuals have been given and possible information about family relations. In the original text files all information about nicknames is provided between ( ) and about family relationships between [ ]. As a next step we thus have cutted information between ( ) in the field “name” into a new field called “name_info_family” and from “surname” information between [ ] into a new field called “nickname”. Now that the additional information is moved from the name and “surname” column, the infixes of the various individuals can be isolated by searching for a comma in the column “surname”.  

## Step 7.
Since an individual might have had multiple positions as minister, the relation between an individual and a role is considered one-to-many. The process above added all the information of a minister career into one field, where every new location and year is distinguished by a , . The next step has therefore been to isolate the information from the column “minister” into a new table where every role has a separate row contain the unique ID (step 2) and the information about the role. 

## Step 8. 
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


Dataset 2 - Dutch Ministers 1572-2004
