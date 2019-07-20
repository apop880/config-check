<a href="https://www.buymeacoffee.com/uMhxJCzPS" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

*In addition to configuring this app in `apps.yaml`, you will also need to add a
few lines to `scripts.yaml` and your Lovelace configuration.*

## App Configuration

```yaml
night_mode:
  module: checkconfig
  class: CheckConfig
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `checkconfig`
`class` | False | string | | `CheckConfig`

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