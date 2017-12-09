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

def knn(k, datapoint, dataset):
	best=float('inf')
	bestPoint=dataset[0]
	for d in dataset:
		current=distance(datapoint, d)
		if current<best:
			best=current
			bestPoint=d
	print bestPoint
	print datapoint
	print "answer: "
	return bestPoint["classification"]

print "What type of Jacket should I wear?"
print "Thinking....."

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
training=[
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 2.8, 'Barometer': 1010.3, 'classification': 'heavy'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 5, 'Barometer': 1010.3, 'classification': 'heavy'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 7.7, 'Barometer': 1010.3, 'classification': 'heavy'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 10.8, 'Barometer': 1010.3, 'classification': 'heavy'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': -3.3, 'Barometer': 1010.3, 'classification': 'heavy'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 12.8, 'Barometer': 1010.3, 'classification': 'light'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 14.2, 'Barometer': 1010.3, 'classification': 'light'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 17.8, 'Barometer': 1010.3, 'classification': 'light'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 16.3, 'Barometer': 1010.3, 'classification': 'light'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 18.0, 'Barometer': 1010.3, 'classification': 'light'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 19.8, 'Barometer': 1010.3, 'classification': 'none'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 23.0, 'Barometer': 1010.3, 'classification': 'none'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 18.9, 'Barometer': 1010.3, 'classification': 'none'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 20.0, 'Barometer': 1010.3, 'classification': 'none'},
		{'Humidity Sensor': 25.5, 'Temperature Sensor': 21.8, 'Barometer': 1010.3, 'classification': 'none'}
	]

m=0
for i in data.keys():
	# pass
	# print time.ctime(float(i)), data[str(i)] 
	
	if int(i)>m:
		m=int(i)

print time.ctime(m)
print ""
print knn(0,  data[str(i)], training)
print ""
print knn(0, {u'Humidity Sensor': 26.5,  u'Barometer': 1010.3, u'Temperature Sensor': 1.8,}, training)


