# HA-getAir-HRV: Home Assistant Integration for getAir SmartFan ComfortControl Pro BT / SmartControl HUB

A fully local, HACS-compatible custom component for Home Assistant to control ComfortControl Pro BT / SmartControl HUB for getAir SmartFan Heat Recovery Ventilation units via Wi-Fi.

**Overview**

This repository includes documentation and source code examples to integrate the getAir REST-API in Home Assistant (https://github.com/getaireu/REST-API).


**Prerequisites:**

getAir REST-API will need to be installed. Also, you may need to install HACS, bubble-card, button-card, but you can also adapt the code to properly match your dashboard view as well.


**Installation:**

Make sure all the .py files reside in the **/*homeassistant/custom_components/getAir*** folder from your Home Assistant machine. Copy the information from _**script.yaml**_ file in the ***/homeassistant/scripts.yaml*** file.  On your Dashboard, you can use the _**bubble_Card-getAir_SpeedFan_BT_Pro.yaml**_ or you can make your own with a mushroom-card or any other card, as per your liking.

Make sure the _**scripts.yaml**_ is referred in the _**/homeassistant/configuration.yaml file**_, something like: ***script: !include scripts.yaml*** should be there; if not, add such a line yourself.

_**number.py**_ contains the code for setting Fan Speeds (from 0 to 4, increments of 0.5), while _**select.py**_ (Heat Recovery Ventilation, Ventilate from Left to Right or vice-versa and Boost) has the code for setting the Modes properly.

**Configuration:**

While adding the getAir integration you will be able to enter credentials from your getAir Family account. If you don't have one yet, you'll need to create it. Contact getAir support if in trouble.


**Examples of Dashboard Cards:**

Main bubble-card from the bubble_Card-getAir_SpeedFan_BT_Pro.yaml. You can turn OFF the getAir SmartFan BT / BT Pro unit by pressing on the main icon (HVAC) or you can turn it ON by choosing the desired fan speed, from level 0.5 to level 4. Changing fan speed status can be done after a 10 seconds waiting time, due to how getAir REST-API operates. Also, speed can be changed from the up / down fan arrows too, in increments of 0.5. Delays of up to 10 seconds are to be expected, due to how the getAir REST-API works.

![Example of card on the Dashboard](/images/Dashboard_Card_01.jpg)

Changing operation mode can be easily done from the submenu (Heat Recovery is recommended choice for most cases).
Main bubble-card from the bubble_Card-getAir_SpeedFan_BT_Pro.yaml.

![Example of card on the Dashboard](/images/Dashboard_Card_02.jpg)

If all good, then the integration will appear in Home Assistant Integration. Restart might be required thoug.

![Example of bubble-card on the Dashboard](/images/getAir_Integration_.jpg)

Lookup for the getAir entities.

![Example of bubble-card on the Dashboard](/images/getAir_Entities.png)

getAir  - device info dashboard.

![Example of bubble-card on the Dashboard](/images/getAir_DeviceInfo.jpg)

### This integration if for personal use only, not for comercial! If you like it, feel free to [buy me a cofee](https://buymeacoffee.com/raoultrifan) or to [paypal.me](https://paypal.me/raultrifan1).
