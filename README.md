# Check Config
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

_Allows you to check your Home Assistant configuration from within Lovelace, or
automatically using when configuration.yaml is updated.
Outputs the results to a sensor and can automatically restart HASS if
configuration is valid._

## Installation

This app is best installed using
[HACS](https://github.com/custom-components/hacs), so that you can easily track
and download updates. Currently, the repository must be added manually on the
Settings page. Once the app moves out of pre-release status, I will submit it to
the default list.

Alternatively, you can download the `check-config` directory from inside the `apps` directory here to your
local `apps` directory, then add the configuration to enable the `checkconfig`
module.

## How it works

The app will auto-generate an entity called `sensor.config_result`. It has an
initial value of `-` until a configuration check is actually run. After running
a check, it will change to `valid` or `invalid`. If it is invalid, the `detail`
attribute on the sensor will include additional data about the specific failure.
If it is valid, Home Assistant can restart automatically, or you can configure
it to not restart until you do so manually.

## App configuration

Add the following to your `apps.yaml` file:
```yaml
check_config:
  module: checkconfig
  class: CheckConfig
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `checkconfig`
`class` | False | string | | `CheckConfig`
`restart` | True | boolean | True | By default, Home Assistant will be restarted if the configuration is valid. Setting this to false will allow you to restart at the time of your choosing.
`folder_watcher` | True | boolean | False | If you are using the `folder_watcher` component (see "Using with Folder Watcher" below), the app can automatically monitor for changes to `configuration.yaml` and run the check any time the file is changed.

## Using With Lovelace

You will need to create an entity called `script.check_config`, but this script
can be blank and won't actually perform any steps. It simply allows us to call
the config check from Lovelace. Copying and pasting the following into your
`scripts.yaml` file will add the proper script.

```yaml
check_config:
  sequence: []
  alias: Check Configuration
```

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

## Using with Folder Watcher

As of version 0.3.0, the [Folder
Watcher](https://www.home-assistant.io/components/folder_watcher/) component can
be integrated into this app. The app will then automatically trigger a
configuration check when your `configuration.yaml` file is updated. You can then
either have Home Assistant restart automatically, or continue to utilize the
sensor updating as you see fit. For example, I have Telegram set up on the
computer I perform my configuration updates on. So, I now receive a notification
from Telegram on my desktop seconds after saving a change to
`configuration.yaml`. If the config is invalid, the specific issue is called out
in the notification. Otherwise, if it's valid, I have an inline keyboard button
that will restart Home Assistant when pressed.

The example code for this notification setup is included in `confignotify.py` in
this repository. Since everyone's notification setup is different, I am not
attempting to include it in the main app at this time, but you are free to use
what I have created as a starting point.

<img
src="https://raw.githubusercontent.com/apop880/config-check/master/telegram.png">

Here is the YAML I'm using to include `folder_watcher` in my setup to monitor
`configuration.yaml`:
```yaml
folder_watcher:
  - folder: /config
    patterns:
      - '*.yaml'
```

You also need your `config` directory under `whitelist_external_dirs` in the
`homeassistant` section of `configuration.yaml`:
```yaml
homeassistant:
  whitelist_external_dirs:
    - /config
```

## Example Screenshots
<img src="https://raw.githubusercontent.com/apop880/config-check/master/lovelace-example.png">
<img
src="https://raw.githubusercontent.com/apop880/config-check/master/result-error.png">

## Advanced Lovelace Config Examples

As a picture elements card with options to reload elements of your
configuration, or a full restart:
```yaml
type: custom:vertical-stack-in-card
cards:
  - type: picture-elements
    image: /local/images/BG_blank_slim.png
    elements:

      - type: image
        image: /local/images/icons8-administrative-tools-80.png
        tap_action:
          action: call-service
          service: script.check_config
        style:
          top: 50%
          left: 10%
          width: 10%

      - type: image
        image: /local/images/icons8-restart-80.png
        tap_action:
          action: call-service
          service: homeassistant.restart
        style:
          top: 50%
          left: 26%
          width: 10%

      - type: image
        image: /local/images/icons8-source-code-80.png
        tap_action:
          action: call-service
          service: homeassistant.reload_core_config
        style:
          top: 50%
          left: 42%
          width: 10%

      - type: image
        image: /local/images/icons8-variation-80.png
        tap_action:
          action: call-service
          service: group.reload
        style:
          top: 50%
          left: 58%
          width: 10%
            
      - type: image
        image: /local/images/icons8-automation-80.png
        tap_action:
          action: call-service
          service: automation.reload
        style:
          top: 50%
          left: 74%
          width: 10%

      - type: image
        image: /local/images/icons8-note-80.png
        tap_action:
          action: call-service
          service: script.reload
        style:
          top: 50%
          left: 90%
          width: 10%


  - type: entities
    show_header_toggle: false
    entities:
      - sensor.config_result
```
<img src="https://raw.githubusercontent.com/apop880/config-check/master/picture-elements-example.jpeg">

## Issues/Feature Requests

Please log any issues or feature requests in this GitHub repository for me to review.