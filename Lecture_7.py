#filename = "./big-mac-full-index.csv"
#file_object = open(filename)

#for line in file_object:
    #if 'Mexico' in line:
    #print(line.split(','))


   # country_code = line.split(',')[2]
    #print(country_code)
    #if country_code == "GBP":
    #print(line.split(',')[2])
#the line split is able to split it into commons and the third column

#import csv

#file_object = open(big_mac_file)

#csv_reader = csv.reader(file_object)

import pandas as pd

filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)
#print(df)
#print(df.columns) shows the columns in the chart
#print(df['dollar_price'])
#this is series data
#query = f"(iso_a3 == 'Mex')"
#mxn_df = df.query(query)
#print(mxn_df)
#year code

#print(type(df.columns))
#print(df['dollar_price'].iloc[1626])
#one of the questions
query_string = "(iso_a3 == 'ARG')"
print(query_string)
arg_df = df.query(query_string)
print(arg_df)
#print(arg_df.iloc[997]) wont work iloc goes over specific record. iloc[36] would work. iloc is location in the series such a 1,2,3 and loc is all the index
#print(type(arg_df.loc[997]))
#print(arg_df.iloc[36],['dollar price']) should work
query = f"(iso_a3 == 'Mex')"
mxn_df = df.query(query)

print(mxn_df.median()) #this is not the median
print(arg_df['dollar_price'].min())
min_df__idx = df['dollar_price'].idxmin()
max_df__idx = df['dollar_price'].idxmax()

print(min_df__idx)
print(max_df__idx)

min_item = df.loc[min_df__idx]
max_item = df.loc[max_df__idx]
print(min_item)
print(max_item)

print(f"{min_item['name']}({min_item['iso_a3']}):{round(min_item['dollar_price'],2)}")

arg_df.to_csv("arg_df.csv")

import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
fhand = open('./big-mac-full-index.csv')
count = 0
for line in fhand:
    if line.endswith("USA", 10 , 14) :
        count = count + 1
print('There were', count, "lines of " "USA", filename)
for linelowercase.startwith in fhand
