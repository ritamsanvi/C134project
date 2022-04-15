
import pandas as pd
import csv

df=pd.read_csv("orgi.csv")
df['distance']=df['distance'].str.replace(',','')
df['luminosity']=df['luminosity'].str.replace(',','')
df['luminosity']=df['luminosity'].str.replace('?','1')
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.to_csv('cleaned.csv')
df.head()


rows = []

with open("cleaned.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
names = []
distance = []
mass = []
radius = []
gravity = []

final_list=[]

for row in star_data_rows:
    if float(row[2]) < 100:
        if float(row[5]) > 150 and float(row[5]) < 350:
            final_list.append(rows)

for i in final_list:
    names.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])

df = pd.DataFrame(
    list(zip(names, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)
df.to_csv('Final.csv')