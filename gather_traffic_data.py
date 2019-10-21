import requests
import json
import csv
import sys
from datetime import date



def return_current_day():
	today = date.today()
	print(today)


def run():
	url = "https://cloud.v-count.com/api/v4/vcountapi"
	payload = {'username':'ROMDemo',
			'password':'ROMDemo1007',
			'format':'json',
			'start_date':'2019-10-02',
			'finish_date':'2019-10-15',
			'store':'RAV_DEMO'}

	response = requests.post(url, data=payload)

	json_resp = response.json()




	outputFile = open("traffic_data_showroom.csv", 'w')
	output = csv.writer(outputFile)
	output.writerow(json_resp[0].keys())  # header row

	for row in json_resp:
	    output.writerow(row.values())


	# print(json.dumps(json_resp, sort_keys=True, indent=4))
	# print(response.text)

return_current_day()