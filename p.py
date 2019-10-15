#vkountimport json

# import requests
# import json

# data = {'username':'ROMDemo',
# 		'password':'ROMDemo2017',
# 		'date':'2019-10-10',
# 		'store':'RAV_DEMO',
# 		'sales:':'200',
# 		'transaction':'500',
# 		'checkouts':'200',
# 		'units':'330'}

# data_json = json.dumps(data)

# payload = {'json_payload': data_json}
# r = requests.post('https://cloud.v-count.com/api/v4/sales', data=payload)

# print(r)





# import urllib.request
# import json      

# body = {'username':'ROMDemo',
# 		'password':'ROMDemo1007',
# 		'date':'2019-10-10',
# 		'store':'RAV_DEMO',
# 		'sales:':'200',
# 		'transaction':'500',
# 		'checkouts':'200',
# 		'units':'330'}

# myurl = "https://cloud.v-count.com/api/v4/sales"
# req = urllib.request.Request(myurl)
# req.add_header('Content-Type', 'application/json; charset=utf-8')
# jsondata = json.dumps(body)
# jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
# req.add_header('Content-Length', len(jsondataasbytes))
# response = urllib.request.urlopen(req, jsondataasbytes)

# print (response.status)




#___________________________________________-

import requests
import json

url = "https://cloud.v-count.com/api/v4/sales"
payload = {'username':'ROMDemo',
		'password':'ROMDemo1007',
		'date':'2019-10-07',
		'store':'RAV_DEMO',
		'transaction':'77',
		'checkouts':'9',
		'units':'33',
		'sales':'200'}

response = requests.post(url, data=payload)

print(response.text)


# import requests
# import json

# url = "https://cloud.v-count.com/api/v4/clientstores"
# payload = {'username':'ROMDemo',
# 		'password':'ROMDemo1007',
# 		'format':'json'}

# response = requests.post(url, data=payload)

# print(response.json())