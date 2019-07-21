import appdaemon.plugins.hass.hassapi as hass
import globals

# Notify after CheckConfig runs

class ConfigNotify(hass.Hass):

	def initialize(self):
		# watch for valid config
		self.listen_state(self.valid_config, "sensor.config_result")

		# listen for telegram restart callback. only need to initialize this
		# listener once
		self.listen_event(self.hass_restart, "telegram_callback", data="/restart")

	def valid_config(self, entity, attribute, old, new, kwargs):
		if new == "valid":
			keyboard = [[("Restart Now", "/restart")]]
			self.call_service("telegram_bot/send_message", message = "Config is valid", target = globals.alex_low, inline_keyboard=keyboard)
		elif new == "invalid":
			error = self.entities.sensor.config_result.attributes.detail
			self.call_service("telegram_bot/send_message", message = "Config is invalid", target = globals.alex_low)
			self.call_service("telegram_bot/send_message", message = error, target = globals.alex_low)
		
	def hass_restart(self, event_name, data, kwargs):
		self.call_service("telegram_bot/send_message", message = "Home Assistant is restarting", target = globals.alex_low)
		self.call_service("homeassistant/restart")