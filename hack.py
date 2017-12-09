import requests
import json

url = "https://api.microshare.io/share/us.philadelphia.senet.sodaq.fancierfish.decoded"

querystring = {"details":"true","page":"","perPage":""}

headers = {
    'Authorization': "Bearer 5326dd877f61485f8f4146aa2d5662693a5c69b503c29d547d0e84cbcbbc3932",
    'Cache-Control': "no-cache",
    'Postman-Token': "31bcb656-8b2a-8810-2dbc-2201d0e104b7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data={}
for point in json.loads(response.text)["objs"]:
	dataType=point["data"]["type"]
	timeStamp=point['createDate']["$date"]
	measurement=point["data"]["measure"]
	measureStr=point["data"]["value"]
	# print dataType
	# for i in point["data"]:
	# 	print i, point["data"][i]
	# print ""
	# print point['createDate']["$date"]
	if dataType not in data:
		data[dataType]=[]
	data[dataType].append({"timeStamp":timeStamp, "dataType":dataType, 'measurement':measurement, 'measureStr':measureStr})
print json.dumps(data, indent=2)
print data.keys()


# print(json.dumps(json.loads(response.text), indent=2))