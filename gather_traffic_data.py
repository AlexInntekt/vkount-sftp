import requests
import json
import csv
import sys
from datetime import date, datetime
import time


def return_current_day():
	today = date.today()
	return today


def run():
	today = return_current_day()

	url = "https://cloud.v-count.com/api/v4/vcountapi"
	payload = {'username':'ROMDemo',
			'password':'ROMDemo1007',
			'format':'json',
			'start_date': today,
			'finish_date': today,
			'store':'RAV_DEMO'}

	print("Calling endpoint..")
	response = requests.post(url, data=payload)

	

	handle_response(response)

	
def handle_response(response):

	json_resp = response.json()

	if(response.status_code==200):

		print(datetime.now(), ' Status code: ', response.status_code)

		writeCSV(json_resp)
	else:
		print("The call failed: ", response.status_code)


def writeCSV(json):
	outputFile = open("traffic_data_showroom.csv", 'w')
	output = csv.writer(outputFile)
	output.writerow(json[0].keys())  # header row

	for row in json:
	    output.writerow(row.values())


def manager():
	while True:
		run()
		time.sleep(60 * 60)

manager()