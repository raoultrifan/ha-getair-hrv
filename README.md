**Overview**

This repository includes documentation and source code examples to integrate the getAir REST-API in Home Assistant.



**Prerequisites:**

You may need to install HACS, bubble-card, button-card, but you can also adapt the code to properly match your dashboard view as well.



**Installation:**

Unzip the folder, then copy the information from script.yaml file into the ***/homeassistant/scripts.yaml*** file. Place all the .py files from the ***"getAir"*** folder in the **/*homeassistant/custom_components*** folder from your Home Assistant machine. On your Dashboard, you can use the bubble_Card-getAir_SpeedFan_BT_Pro.yaml or you can easily make your own with a mushroom-card or any other card, as per your liking.

Make sure the scripts.yaml is referred in the /homeassistant/configuration.yaml file, something like: ***script: !include scripts.yaml*** should be there; if not, add yourself such a line.



**Configuration:**

While adding the getAir integration you will be able to enter credentials from your getAir Family account. If you don't have one yet, you'll need to create it. Contact getAir support if in trouble.
