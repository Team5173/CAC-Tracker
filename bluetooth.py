import subprocess
import os
devices = {'D4:63:C6:3B:B9:BD': 0}

btconnected=0
btcurrent=-1
counter=0
notconnected=0
connected=1
rssi=-1

#Command loop:
while (True):
    cmdout= os.system("hcitool rssi " + list(devices.keys())[0])
    btcurrent= int(os.popen("echo " + str(cmdout) + " | grep -c \"RSSI return value\" 2> /dev/null").read().replace('RSSI return value: ', '').replace('\n', ''))    
    
    rssi= os.system("echo " + str(cmdout) + " | sed -e 's/RSSI return value: //g'")                                  


    if (btcurrent == notconnected):
        os.system("echo Attempting connection...")
        os.system("rfcomm connect 0 " + list(devices.keys())[0] + " 1 2> /dev/null >/dev/null &")
        os.system("sleep 1")        
        '''
    if (btcurrent == connected):
        os.system("echo \"Device connected. RSSI: \"" + str(rssi))

    if (btconnected != btcurrent):
        if (btcurrent != 0 ):
            os.system("echo GONE!")
        if (btcurrent != 1 ):
            os.system("echo HERE!")

        btconnected = btcurrent
'''

os.system("sleep 1")

os.system("done")

