import csv
import pandas as pd
            
data = []
df = pd.read_csv("Brown_star_main.csv")
df = df[df["Star_Name"].notna()]
df = df[df["Star_Mass"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Star_Radius"].notna()]
del df["Unnamed"]
df.to_csv('brown_star_Nan_free.csv', index = False) 
with open("brown_star_Nan_free.csv" , "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
headers = data[0]
planet_data = data[1:]

for row in planet_data:
        row[2] = float(row[2])*0.102763
        row[3] = float(row[3])*0.000954588
    
with open("scaled_brown_star.csv" , "w" , newline="") as final:
    writer = csv.writer(final)
    writer.writerow(headers)
    writer.writerows(planet_data)