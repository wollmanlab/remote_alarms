from pi_remote_alarm import checkDSBtemperature, sendMail, checkRemoteAlarm, checkIP

no_pin = 10
nc_pin = 8

alarm = checkRemoteAlarm(no_pin, nc_pin)
ip = checkIP(interface='eth0')
sendMail('minus80', alarm+'\n'+ip)
print(alarm, ip)


