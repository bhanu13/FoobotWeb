
# Testing encoding for Basic Authorization
# Testing the different URLs - Look at foobot.py
# import base64
import requests
import json

# format = "username:password"

# def encode(STRING):
# 	encoded = base64.b64encode(STRING)
# 	return encoded

# example = "Aladdin:open sesame"
# print encode(example)



# username = "magnetog@gmail.com"
# login_URL = "https://api.foobot.io/v2/user/%s/login/" % username

# password = "magnet0"

# auth_str = username + ":" + password

# auth = "Basic " + encode(auth_str)
# header = {"Authorization": auth}

# r = requests.get()
# X-AUTH-TOKEN

# r = requests.get(login_URL, auth=(username, password))
# print r.headers


# token = r.headers["X-AUTH-TOKEN"]

# headers = {"X-AUTH-TOKEN": token}

# device_URL = "https://api.foobot.io/v2/device/%s/" % username
# user_URL = "https://api.foobot.io/v2/user/%s/" % username
# owner_URL = "https://api.foobot.io/v2/owner/%s/" % username

# devicedata = dict()

# # def get_userID():
# URL = owner_URL + "/device/"
# r = requests.get(URL, headers = headers)
# devicedata = json.loads(r.content)

# uuid = devicedata["uuid"]

# print uuid

# def sampleinterval():
# 	pass

# def getlastdatapoint():
# 	period = 0
# 	sampling = 0
# 	pass

from datetime import tzinfo, timedelta, datetime
import time

# dt = datetime.now()

# print datetime(dt, tzinfo=TZ()).isoformat('T')

# import pytz
# from datetime import datetime
# now = datetime.now().replace(tzinfo = TZ(), microsecond=0)


def format(time):
	class TZ(tzinfo):
		def utcoffset(self, dt): 
			return timedelta(minutes=+330)	# For India
	
	time = time.replace(tzinfo = TZ(), microsecond=0)
	return time.isoformat('T')

# print datetime.now()
# datetime_now = datetime.utcnow()
now = datetime.now()

print format(now)
last_30 = now - timedelta(minutes=-30)
print format(last_30)
last_day = now - timedelta(days = 1)
print format(last_day)

# dt = datetime(year=2015, month=8, day=10, hour=0, minute=0, second=0, microsecond=0)

# print dt.isoformat('T')




# Converting the different timestamps to actual date and time

latest = datetime.fromtimestamp(1436957462)

print latest
