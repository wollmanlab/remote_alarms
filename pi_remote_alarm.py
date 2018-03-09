def checkDSBtemperature(device_name, base_pth = '/sys/bus/w1/devices/'):
    """
    Function to check the DSB1820 digital thermometers.
    
    Parameters
    ----------
    device_name : str
        String containing the directory name of the device.
        Typically will be 28-xxxx where xxxx is randomly assigned.
    """
    try:
        tfile = open("{0}{1}/w1_slave".format(base_pth, device_name))
        # Read the file generated that contains the temperature information.
        text = tfile.read()
        tfile.close()
        # Parse the file to extract the temperature information.
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        # Convert to decimal format
        temperature = float(temperaturedata[2:])
        temperature = temperature/1000.
    except Exception as e:
        temperature = str(e)
    return temperature

import RPi.GPIO as pi
def checkRemoteAlarm(normally_open_pin, normally_closed_pin, setmode=pi.BOARD):
    """
    Check the state of a remote alarm system.
    
    Parameters
    ----------
    normally_open_pin : int
        The corresponding raspberry pi pin number.
    normally_closed_pin : int
        The corresponding raspberry pi pin number.
    setmode : RPi.GPIO
        Either pi.BCM or pi.BOARD depending on which pin labeling 
        scheme is used to reference the raspberry pi pin numbers.
        pi.BOARD is the most consistent accross pi models.
    """
    pi.setmode(setmode)
    pi.setup(normally_open_pin, pi.IN, pull_up_down=pi.PUD_DOWN)
    pi.setup(normally_closed_pin, pi.IN, pull_up_down=pi.PUD_DOWN)
    functioning_state = pi.input(normally_closed_pin)
    failure_state = pi.input(normally_open_pin)
    if functioning_state and not failure_state:
        alarm_state = "Device Functioning Properly"
    elif not functioning_state and failure_state:
        alarm_state = "Remote Alarm Active"
    else:
        alarm_state = "Alarm Reporting Not Functioning Properly"
    pi.cleanup()
    return alarm_state

import smtplib
def sendMail(device, alarm):
    """
    Send email with the device name and alarm state.
    
    Parameters
    ----------
    device : str
        Name of the device being reported.
    alarm : str, float
        State of the alarm
    """
    # Convert temperature floats to string for mailing compatability
    if isinstance(alarm, float):
        alarm = str(alarm)
    # Configure email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("pi.wollmanlab", "trumpsucks")
    sendFrom = "pi.wollmanlab@gmail.com"
    # Account to receive the email
    sendTo = "wollmanlab@g.ucla.edu"
    msg = "Subject: {0}\n\nAlarm state: {1}".format(device, alarm)
    server.sendmail(sendFrom, sendTo, msg)
    server.quit()
    print('Sent mail to {0} with the message: \n{1}'.format(sendTo, msg))
    
import subprocess
def checkIP(interface = 'eth0'):
    """
    Check IP of device.
    Allows easier ssh access since IP is not static.
    
    Parameters
    ----------
    interface : str
        name of the network adapter in ifconfig to report.
        
    Returns
    -------
    ip : str
        IP address of the interface adapter as a string
    """
    try:
        network_info = subprocess.Popen(['ifconfig', interface], stdout=subprocess.PIPE).communicate()[0]
        network_info = network_info.rstrip().split('\n')[1].strip(' ')
        ip = network_info.split(' ')[1].split(':')[1]
    except Exception as e:
        ip = str(e)
    return ip
    
