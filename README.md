# Check Config
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

_Allows you to check your Home Assistant configuration from within Lovelace.
Outputs the results to a sensor and will automatically restart HASS if
configuration is valid._

## Installation

This app is best installed using
[HACS](https://github.com/custom-components/hacs), so that you can easily track
and download updates.

Alternatively, you can download the `check-config` directory from inside the `apps` directory here to your
local `apps` directory, then add the configuration to enable the `checkconfig`
module.

## How it works

You will need to create an entity called `script.check_config`, but this script
can be blank and won't actually perform any steps. It simply allows us to call
the config check from Lovelace. Copying and pasting the following into your
`scripts.yaml` file will add the proper script.

```yaml
check_config:
  sequence: []
  alias: Check Configuration
```

The app will auto-generate an entity called `sensor.config_result`. It has an
initial value of `-` until a configuration check is actually run. After running
a check, it will change to `valid` or `invalid`. If it is invalid, the `detail`
attribute on the sensor will include additional data about the specific failure.
If it is valid, Home Assistant will restart automatically.

The following is a basic example of a Lovelace example to run the check and show
the results.

```yaml
type: entities
title: Check Configuration
show_header_toggle: false
entities:
  - script.check_config
  - sensor.config_result
```

## App configuration

```yaml
night_mode:
  module: checkconfig
  class: CheckConfig
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `checkconfig`
`class` | False | string | | `CheckConfig`

## Screenshots
<table><tr><td>
<img src="https://raw.githubusercontent.com/apop880/check-config/master/lovelace-example.jpg" width=200>
<img src="https://raw.githubusercontent.com/apop880/check-config/master/result-error.jpg" width=200></td></tr></table>

## Issues/Feature Requests

Please log any issues or feature requests in this GitHub repository for me to review.