from pi_remote_alarm import sendMail, checkDSBtemperature, checkIP

device_name = 'minus_20_tall_1'
dsb_folder_name = '28-00042e07f8ff'

temp = checkDSBtemperature(dsb_folder_name)
ip = checkIP(interface='eth0')
print(temp)
sendMail(device_name, str(temp)+'\n'+ip)

