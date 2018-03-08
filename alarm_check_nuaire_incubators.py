"""
Monitors the nuaire incubator bank in the Wollman Lab.

device_map specifies a device name key with tuple of 
(normally_open, normally_closed) Pi pins as values.
Rob Foreman October 2016 
"""
import pi_remote_alarm as alarm
import subprocess

device_map = {'mufasa': (11, 13), 'pumba': (8, 10), 'nala': (12, 16), 'timon': (18, 22)}

try:
    ip = alarm.checkIP(interface='eth0')
except:
    ip = 'unavailable'

for device, pins in device_map.items():
    nc, no = pins
    alarm_state = alarm.checkRemoteAlarm(no, nc)
    print(device, alarm_state)
    try:
        alarm.sendMail(device, alarm_state+'\n'+ip)
    except:
        print(device, 'failed to send')
        continue


#p = subprocess.Popen('ifconfig', shell=True, stdout=subprocess.PIPE)
#data = p.communicate()

#alarm.sendMail('IP:Incubators', data)
