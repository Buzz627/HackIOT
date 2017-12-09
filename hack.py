import requests
import json
import time

def distance(point1, point2):
	total=0
	for key in point1.keys():
		if key=="classification":
			pass
		try:
			total+=abs(point1[key]-point2[key])
		except: return float('inf')
	return total

def findKNearest(k, datapoint, dataset):
	bestnums=[float('inf')]*k
	bestPoint=dataset.keys()[0]
	for d in dataset:
		current=distance(datapoint, dataset[d])
		if current<best:
			best=current
			bestPoint=dataset[d]
	return 



url = "https://api.microshare.io/share/this.is.buzz.decoded"

querystring = {"details":"true","page":"","perPage":""}

headers = {
    'authorization': "Bearer 5e8987b0475ef7b5e433ea360a7daf59d108a37d2338f72f340a18c70a8c74cc",
    # 'cache-control': "no-cache",
    # 'postman-token': "00156731-b784-8fe5-75f3-012afde3cf35"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
# print(json.dumps(json.loads(response.text), indent=2))

data={}
for point in json.loads(response.text)["objs"]:
	try:
		# print point["id"]
		dataType=point["data"]["type"]
		timeStamp=point['createDate']["$date"]/1000
		measurement=point["data"]["measure"]
		measureStr=point["data"]["value"]
		# print dataType
		# for i in point["data"]:
		# 	print i, point["data"][i]
		# print ""
		# print point['createDate']["$date"]
		if str(timeStamp) not in data:
			data[str(timeStamp)]={}
		data[str(timeStamp)][dataType]=measurement
		data[str(timeStamp)]['classification']=random
		# print json.dumps(data, indent=2)
		# print data.keys()


		# print(json.dumps(json.loads(response.text), indent=2))

	except:
		pass



for i in data.keys():
	print time.ctime(float(i)), data[str(i)] 
	# for j in data[i]:
	# 	if j["timeStamp"]>m:
	# 		m=j["timeStamp"]
	# print time.ctime(m)


