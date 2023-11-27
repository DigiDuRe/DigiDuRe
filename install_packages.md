# Setup to run the jupyter notebooks to process the data

First you will need to download the software:

1. Open https://www.anaconda.com/products/distribution with your web browser.
2. Download the Python 3 installer for Windows.
3. Double-click the executable and install Python 3 using MOST of the default settings. The only exception is to check the Make Anaconda the default Python option.

Once you installed anaconda, please open the terminal of Anaconda by pressing the windows button and type "Anaconda prompt".

Creating the environment

To make sure your python installation is not conflicting with anthing else we are going to creat a environment called ais_barcin and install the required libraries. Open a terminal and type the command:

```
conda create --name digidure python jupyter pandas
```

Now we are going to activate the newly created environment:

```
conda activate digidure
```

Next we are going to install the necessary libraries for the script that has been developed using pip. We will probably get a lot of notifications that some have already been installed.

It can happen that you would need to install pip. Pip allows you to install other libraries. 

```
conda install pip
```

Once pip is intalled you can install other packages. The first package we are installing is docx2txt, which is needed to convert .docx files to text files. This file is needed for act1.

```
pip install docx2txt
```

The next packages we need to install are networkx, fuzzywuzzy, SPARQLWrapper, pyodbc and Levenshtein.

```
pip install networkx
pip install fuzzywuzzy
pip install SPARQLWrapper 
pip install pyodbc
pip install Levenshtein
```








