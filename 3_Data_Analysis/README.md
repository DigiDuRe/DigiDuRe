# 3 Analysis scripts
With the [CLERUS dataset](../1_Data_Harmonization/README.md) available and the other external [datasets](../2_Linking_data/README.md) scraped, a series of analysis scripts have been developed to explore the data and add to the analysis of book titles. The scripts presented here are example scripts and would form the basis of computational historical research which would allow for a bottom-up reconstruction of trends and changes in thematization.

The scripts are presented are dynamic and presented for CLERUS v1, but can easily be rerun once CLERUS_v2 and CLERUS+ are processed and curated see[1_Data_Harmonization](../1_Data_Harmonization/README.md).


## 3.1 Basic Statistics on CLERUS. 
In order to explore the dataset of CLERUS a series of basic statics are are performed in this [notebook](3_1_basic_stats_clerus.ipynb). 
It shows:
- How to load the data
- How to count the number of roles
- How to plot the birth years of every minister
- How to plot the year of death for every minister


## 3.2 Number of active ministers per period
A more complex notebook is provided [here](3_2_active_ministers.ipynb) where the number of active ministers per period is generated.  


## 3.3 Number of titles published by protestant ministers per year
When linking book titles with CLERUS a series of analysis can be performed. In [this notebook](3_3_clerus_kb.ipynb) a series of explorative analyses are explored.