import csv
import pandas as pd
filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)
#print(df)

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    query = f"(iso_a3 == '{country_code}' and date >= '{year}-01-01'and date <= '{year}-12-31')"
    #print(query)
    result_df = df.query(query)
    return(round(result_df['dollar_price'].mean(),2))
def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}')"
    result_df = df.query(query_text)
    return(round(result_df['dollar_price'].mean(),2))

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    result_df = df.query(query)
    minidx = result_df["dollar_price"].idxmin()
    result_series = result_df.loc[minidx]
    result_message = f"{result_series['name']}({result_series['iso_a3']}): ${round(result_series['dollar_price'],2)}"
    return result_message
def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_1 = get_big_mac_price_by_year(2014,'can')
    print(result_1)
    result_2 = get_big_mac_price_by_country("can")
    print(result_2)
    result_3 =  get_the_cheapest_big_mac_price_by_year(2014)
    print(result_3)
   