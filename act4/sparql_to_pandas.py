sparql = SPARQLWrapper(sparql_endpoint)
sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

bindings = results["results"]["bindings"]
data = []

for item in bindings:
    row = {}
    for key in item:
        row[key] = item[key]["value"]
    data.append(row)

df = pd.DataFrame(data)

# Panda settings for showing data
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

output_file = folderlink+folder_output+"stcn_q1_nbt.csv"
df.to_csv(output_file, sep=';', encoding='utf-8', index=False)

df.describe()