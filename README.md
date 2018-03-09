This repository stores code for running temperature and alarm sensing with remote monitoring.

Alarms are monitored by using integrated normally open (NO) -> close and normally closed (NC) -> open during device alarm (common in -80 freezers and other lab equipment such as cryogen storage containers). These are monitored with raspberry pi's supplying +5V to the common line and the NO and NC are connected to board GPIOs as inputs. The python scripts are run as cron jobs every 30 minutes.

Temperature monitoring is accomplished using Waterproof DS18B20 Digital temperature sensors that can be run into -20 freezers through the drainage plug. These are also monitored with raspberry pis that report the device temperature every 30 minutes.
https://www.adafruit.com/product/381

Python scripts monitor the state of the NO and NC circuits in order to detect whether the device is an a normal or alarm state. These are relayed via email to a gmail account that is monitored by a javascript routine. This routine texts/emails/slacks individuals in the lab whenever a device responds in the alarm state or when a device fails to respond.

https://docs.google.com/spreadsheets/d/1EwrXbQ0DDQ0LmQT0OZ_jR8LQn1u8QbbIwCFUJAgKtTs/edit?usp=sharing

https://docs.google.com/spreadsheets/d/1vHfT5MPXS-1faRCtToCsE8a9VPQ3o-E6-MVruje0zYA/edit?usp=sharing
