import requests
import json

url = "https://api.microshare.io/share/this.is.buzz.decoded"

querystring = {"details":"true","page":"","perPage":""}

headers = {
    'authorization': "Bearer 5e8987b0475ef7b5e433ea360a7daf59d108a37d2338f72f340a18c70a8c74cc",
    'cache-control': "no-cache",
    'postman-token': "b8c29d8a-9fd9-9769-3185-21c8982c43bd"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data={}
for point in json.loads(response.text)["objs"]:
	dataType=point["data"]["type"]
	timeStamp=point['createDate']["$date"]
	measurement=point["data"]["measure"]
	measureStr=point["data"]["value"]
	print dataType
	for i in point["data"]:
		print i, point["data"][i]
	print ""
	print point['createDate']["$date"]
	if dataType not in data:
		data[dataType]=[]
	data[dataType].append({"timeStamp":timeStamp, "dataType":dataType, 'measurement':measurement, 'measureStr':measureStr})
print json.dumps(data, indent=2)
print data.keys()


# print(json.dumps(json.loads(response.text), indent=2))