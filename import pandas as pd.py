import pandas as pd
filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

query_string = "(iso_a3 == 'USA')"
print(query_string)