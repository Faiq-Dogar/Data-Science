from bs4 import BeautifulSoup as bts
import pandas as pd
import requests as req
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page_data = bts(req.get(url).text, "html");
#print(page_data)

print("-------------------------------------------")

target_table = page_data.find("table" , class_ = "wikitable sortable")
#print(target_table)

headers = target_table.find_all("th")
print(headers)

headers = [i.text.strip() for i in headers]
print(headers)

df = pd.DataFrame(columns = headers)
print(df)

table_rows = target_table.find_all("tr")

for row in table_rows[1:]:
    row_data = row.find_all("td")
    indiviual_row = [i.text.strip() for i in row_data]
    length = len(df)
    df.loc[length] = indiviual_row

print(df)
df.head()

flag = df.to_csv(r"C:\Users\faiqd\Desktop\Data Analysis\Datasets\Companies.csv", index = False)
print(flag)