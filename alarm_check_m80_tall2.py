from pi_remote_alarm import checkDSBtemperature, sendMail, checkRemoteAlarm, checkIP

# Pin configuration for specific device
no_pin = 10
nc_pin = 8

# DSB Temperature Sensor creates a folder with random characters to save temp
minus20_tall_2 = '28-00042b357fff'

#Check IP Address
ip = checkIP(interface='eth0')

# Check minus80
try:
	minus80_alarm = checkRemoteAlarm(no_pin, nc_pin)
	sendMail('minus80', minus80_alarm+'\n'+ip)
except:
	minus80_alarm = 'Failed to acquire minus80'

# Check minus 20 tall 2
minus20tall2_temp = checkDSBtemperature(minus20_tall_2)
sendMail('minus_20_tall_2', str(minus20tall2_temp)+'\n'+ip)


print(minus80_alarm, minus20tall2_temp,  ip)


