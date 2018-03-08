from pi_remote_alarm import checkDSBtemperature
device_name = '28-00042e0894ff'

temp = checkDSBtemperature(device_name)
print(temp)
log_file = open('/home/pi/scripts/temp_log.txt', 'a')
log_file.write(str(temp)+'\n')
log_file.close()
