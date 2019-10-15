import csv
import requests
import json

url = "https://cloud.v-count.com/api/v4/sales"

with open('data_pack.csv', newline='') as File:  
    reader = csv.DictReader(File)
    for row in reader:
        #print(row['sales'])

        
        payload = {'username':'ROMDemo',
        'password':'ROMDemo1007',
        'date':row['date'],
        'sales': row['sales'],
        'store':'RAV_DEMO',
        'transaction':row['transaction'],
        'checkouts':'1',
        'units':'33'
        }

        response = requests.post(url, data=payload)
