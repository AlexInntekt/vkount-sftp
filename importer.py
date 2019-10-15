import csv

with open('data_pack.csv', newline='') as File:  
    reader = csv.DictReader(File)
    for row in reader:
        print(row['store'])