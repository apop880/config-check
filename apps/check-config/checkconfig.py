import appdaemon.plugins.hass.hassapi as hass
import requests
import json

# Check Home Assistant Configuration

class CheckConfig(hass.Hass):

	def initialize(self):
		# is auto-restart set?
		if "restart" in self.args and self.args["restart"] == False:
			self.restart = False
		else:
			self.restart = True

		# create a sensor to track check result
		self.set_state("sensor.config_result", state="-", attributes = {"friendly_name": "Config Result", "detail": None})
		
		# get HASS URL
		self.apiurl = "{}/api/config/core/check_config".format(self.config["plugins"]["HASS"]["ha_url"])
		
		# token or key to authenticate
		if "token" in self.config["plugins"]["HASS"]:
			self.auth = "token"
			self.listen_state(self.check_config, "script.check_config")
		elif "ha_key" in self.config["plugins"]["HASS"]:
			self.auth = "key"
			self.listen_state(self.check_config, "script.check_config")
		else:
			self.log("AppDaemon config must use a token or key to authenticate with HASS")
			self.set_state("sensor.config_result", state="ERROR", attributes = {"friendly_name": "Config Result", "detail": "AppDaemon config must use a token or key to authenticate with HASS"})
		
	def check_config(self, entity, attribute, old, new, kwargs):
		# set headers for auth
		if self.auth == "token":
			self.headers = {'Authorization': "Bearer {}".format(self.config["plugins"]["HASS"]["token"])}
		else: #key
			self.headers = {'x-ha-access': self.config["plugins"]["HASS"]["ha_key"]}
		# make the request
		r = requests.post(self.apiurl, headers=self.headers)
		# evaluate result
		if json.loads(r.text)['result'] == "valid":
			self.set_state("sensor.config_result", state="valid", attributes = {"detail": None})
			# restart if auto-restart is on
			if self.restart == True:
				self.call_service("homeassistant/restart")
		else:
			self.set_state("sensor.config_result", state="invalid", attributes = {"detail": json.loads(r.text)['errors']})