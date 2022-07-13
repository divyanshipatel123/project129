import csv
dataset1 = []
dataset2 = []
with open("Brightest_star.csv" , 'r') as f :
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)
with open("scaled_brown_star.csv" , 'r') as f :
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)
headers_dataset1 = dataset1[0]
planet_data1 = dataset1[1:]

headers_dataset2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers_dataset1 + headers_dataset2
planetdata = []

for index , data in enumerate(planet_data1):
    planetdata.append(planet_data1[index]+ planet_data2[index])

with open("mergerd_final_data.csv" , "a+" , newline="")as f:
    csv_writer  = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planetdata)