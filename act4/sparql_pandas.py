import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

def sparql_to_dataframe(sparql_endpoint, sparql_query):
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
    return df
