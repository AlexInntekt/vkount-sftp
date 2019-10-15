import requests
import json

url = "https://cloud.v-count.com/api/v4/clientstores"
payload = {'username':'ROMDemo',
		'password':'ROMDemo1007',
		'format':'json'}

response = requests.post(url, data=payload)

print(response.json())