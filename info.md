<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

** As of version 2.0, I am only testing against AppDaemon 4.x. The app will likely continue to work with
AppDaemon 3.x, but if you have an issue and are using AppDaemon 3.x, I will not be able to provide support. **

*In addition to configuring this app in `apps.yaml`, you will also need to add a
few lines to `scripts.yaml` and your Lovelace configuration. Or, you will need
to set up the `folder_watcher` component (see the readme for more detail if you
choose that route).*

## App Configuration

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
`folder_watcher` | True | boolean | False | If you are using the `folder_watcher` component (see "Using with Folder Watcher" in the README), the app can automatically monitor for changes to `configuration.yaml` and run the check any time the file is changed.

## `Scripts.yaml` Configuration

```yaml
check_config:
  sequence: []
  alias: Check Configuration
```

## Sample Lovelace Configuration

```yaml
type: entities
title: Check Configuration
show_header_toggle: false
entities:
  - script.check_config
  - sensor.config_result
```