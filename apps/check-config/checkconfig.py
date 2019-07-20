import appdaemon.plugins.hass.hassapi as hass
import requests
import json

# Check Home Assistant Configuration

class CheckConfig(hass.Hass):

	def initialize(self):
		# create a sensor to track check result
		self.set_state("sensor.config_result", state="-", attributes = {"friendly_name": "Config Result", "detail": None})
		
		# get config data
		self.apiurl = "{}/api/config/core/check_config".format(self.config["plugins"]["HASS"]["ha_url"])
		
		# token or key
		if "token" in self.config["plugins"]["HASS"]:
			self.auth = "token"
			self.listen_state(self.check_config, "script.check_config")
		elif "ha_key" in self.config["plugins"]["HASS"]:
			self.auth = "key"
			self.listen_state(self.check_config, "script.check_config")
		else:
			self.log("AppDaemon config must use a token or key to authenticate with HASS")
		
	def check_config(self, entity, attribute, old, new, kwargs):
		if self.auth == "token":
			self.headers = {'Authorization': "Bearer {}".format(self.config["plugins"]["HASS"]["token"])}
		else: #key
			self.headers = {'x-ha-access': self.config["plugins"]["HASS"]["ha_key"]}
		r = requests.post(self.apiurl, headers=self.headers)
		self.log(r)
		if json.loads(r.text)['result'] == "valid":
			self.set_state("sensor.config_result", state="valid", attributes = {"detail": None})
			self.call_service("homeassistant/restart")
		else:
			self.set_state("sensor.config_result", state="invalid", attributes = {"detail": json.loads(r.text)['errors']})