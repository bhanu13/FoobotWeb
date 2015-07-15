"""
This file defines a foobotweb class for polling data out of the foobot for the user
making HTTP requests.
It implements login, logout first and then implements the different data extraction methods.

Author - bhanu13

Basic Authorization and X-AUTH-TOKEN
Time - Date ISO 8601
"""

import requests
import json
import time
import getpass

from datetime import tzinfo, timedelta, datetime

class FoobotWeb(object):
	login_URL = ""
	owner_URL = ""
	device_URL = ""
	headers = dict()
	devicedata = dict()

	def __init__(self, username = None):
		if not username:
			username = str(raw_input("Please enter your Foobot username:\n"))

		self.username = username
		print "Please enter your Foobot password"
		self.password = getpass.getpass()

		if self.login():
			if self.deviceinfo():
				print "Setup Complete"

	def login(self):
		self.login_URL = "https://api.foobot.io/v2/user/%s/login/" % self.username
		r = requests.get(self.login_URL, auth=(self.username, self.password))
		if r.status_code != requests.codes.ok:
			print "Invalid Login Information."
			return False
		token = r.headers["X-AUTH-TOKEN"]
		self.headers["X-AUTH-TOKEN"] = token
		return True

	def deviceinfo(self):
		self.owner_URL = "https://api.foobot.io/v2/owner/%s/" % self.username
		URL = self.owner_URL + "/device/"
		r = requests.get(URL, headers = self.headers)
		if r.status_code != requests.codes.ok:
			print "Unable to get device info."
			return False
		self.devicedata = json.loads(r.content)
		self.uuid = self.devicedata[0][u"uuid"]
		print "Your user ID is %s" % self.uuid
		self.device_URL = "https://api.foobot.io/v2/device/%s/" % str(self.uuid)
		return True

	def GetDatapointLast(self, period = 0, sampling = 0, save = False):
		URL = self.device_URL + "datapoint/%s/last/%s/" % (period, sampling)
		URL = str(URL)
		r = requests.get(URL, headers = self.headers)
		
		if r.status_code != requests.codes.ok:
			print "Some Error in GetDatapointLast"
			return None
		data = json.loads(r.content)
		# print data
		file_name = 'data_%s_%s.json' % (period, sampling)
		if save:
			self.SaveData(name = file_name, data = data)
		print data
		return data


	def GetLastHour(self, save = False):
		data = self.GetDatapointLast(3600, 300)
		if data and save:
			starttime = data["start"]
			starttime = datetime.fromtimestamp(starttime)
			file_name = "last_hour" + starttime.isoformat()
			self.SaveData(name = file_name, data = data)

	def GetLastDay(self, save = False):
		data = self.GetDatapointLast(86400, 3600)
		if data and save:
			starttime = data["start"]
			starttime = datetime.fromtimestamp(starttime)
			file_name = "last_day" + starttime.isoformat()
			self.SaveData(name = file_name, data = data)

	def GetDataInterval(self, starttime = datetime.now() - timedelta(minutes=-30), endtime = datetime.now(), sampling = 0, save = False):
		starttime = self.formattime(starttime)
		endtime = self.formattime(endtime)
		URL = self.device_URL + "datapoint/%s/%s/%s/" % (starttime, endtime, sampling)	# Get Method Works
		print URL
		r = requests.get(URL, headers = self.headers)

		if r.status_code != requests.codes.ok:
			print "Some Error in getting data for the given time interval"
			return

		data = json.loads(r.content)
		print data
		if save and data:
			file_name = "data_from_%s_%s" % (starttime, endtime)
			self.SaveData(name = file_name, data = data)
	

	def formattime(self, time):
		class TZ(tzinfo):
			def utcoffset(self, dt): 
				return timedelta(minutes=+330)	# For India
		
		time = time.replace(tzinfo = TZ(), microsecond=0)
		return time.isoformat('T')

	def SaveData(self, name, data):
		if name and data:
			with open('data/%s.json' % name, 'w') as outfile:
				json.dump(data, outfile)

	# def GetDatapoints(self, start = None, end = None, sampling = 0):
	# 	today == date.fromtimestamp(time.time())
