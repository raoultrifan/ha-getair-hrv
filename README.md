**Overview**

This repository includes documentation and source code examples to integrate the getAir REST-API in Home Assistant.


**Prerequisites:**

getAir REST-API will need to be installed. Also, you may need to install HACS, bubble-card, button-card, but you can also adapt the code to properly match your dashboard view as well.


**Installation:**

Unzip the folder, then copy the information from script.yaml file into the ***/homeassistant/scripts.yaml*** file. Place all the .py files from the ***"getAir"*** folder in the **/*homeassistant/custom_components*** folder from your Home Assistant machine. On your Dashboard, you can use the bubble_Card-getAir_SpeedFan_BT_Pro.yaml or you can easily make your own with a mushroom-card or any other card, as per your liking.

Make sure the scripts.yaml is referred in the /homeassistant/configuration.yaml file, something like: ***script: !include scripts.yaml*** should be there; if not, add yourself such a line.


**Configuration:**

While adding the getAir integration you will be able to enter credentials from your getAir Family account. If you don't have one yet, you'll need to create it. Contact getAir support if in trouble.


**Examples of Dashboard Cards:**

Main bubble-card from the bubble_Card-getAir_SpeedFan_BT_Pro.yaml. You can turn OFF the getAir SmartFan BT / BT Pro unit by pressing on the main icon (HVAC) or you can turn it ON by choosing the desired fan speed, from level 0.5 to level 4. Changing fan speed status can be done after a 10 seconds waiting time, due to how getAir REST-API operates. Also, speed can be changed from the up / down fan arrows too, in increments of 0.5. Delays of up to 10 seconds are to be expected, due to how the getAir REST-API works.

![Example of bubble-card on the Dashboard](https://github.com/raoultrifan/HomeAssistant-getAir-HRV/blob/main/Dashboard_Card_01.jpg)

Changing operation mode can be easily done from the submenu (Heat Recovery is recommended choice for most cases).
Main bubble-card from the bubble_Card-getAir_SpeedFan_BT_Pro.yaml.
![Example of bubble-card on the Dashboard](https://github.com/raoultrifan/HomeAssistant-getAir-HRV/blob/main/Dashboard_Card_02.jpg)


