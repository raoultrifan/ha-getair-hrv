**Overview**

This repository includes documentation and source code examples to integrate the getAir REST-API in Home Assistant.



**Prerequisites:**

You may need to install HACS, bubble-card, button-card, but you can also adapt the code to properly match your dashboard view as well.



**Installation:**

Unzip the folder, then copy the information from script.yaml file into the ***/homeassistant/scripts.yaml*** file. Place the remaining unzipped files from the ***"getAir"*** folder in the **/*homeassistant/custom\_components*** folder from your Home Assistant machine.

Make sure the scripts.yaml is referred in the /homeassistant/configuration.yaml file, something like: ***script: !include scripts.yaml*** should be there; if not, add yourself such a line.



**Configuration:**

Show where they need to insert their specific HRV IP address or API token.

