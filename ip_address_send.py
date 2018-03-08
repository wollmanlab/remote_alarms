from pi_remote_alarm import sendMail, checkIP

ip = checkIP(interface='eth0')
sendMail("IP Address", "minus80"+" ip="+ip)
