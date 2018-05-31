import subprocess
import os
devices = {'D4:63:C6:3B:B9:BD': 0}
print(subprocess.Popen("cmdout=$(hcitool rssi " + list(devices.keys())[0] + ")", shell=True, stdout=subprocess.PIPE).stdout.read())

btconnected=0
btcurrent=-1
counter=0
notconnected="0"
connected="1"
rssi=-1

#Command loop:
while (True):
    
    cmdout= os.popen("hcitool rssi " + list(devices.keys())[0]).read()
    '''
    btcurrent= os.popen("echo " + cmdout + " | grep -c \"RSSI return value\") 2> /dev/null").read()
    rssi= os.popen("echo " + cmdout + " | sed -e 's/RSSI return value: //g')").read()                                   


    if (btcurrent == notconnected ):
        print(subprocess.Popen("echo Attempting connection...", shell=True, stdout=subprocess.PIPE).stdout.read())
        print(subprocess.Popen("rfcomm connect 0 $device 1 2> /dev/null >/dev/null &", shell=True, stdout=subprocess.PIPE).stdout.read())
        print(subprocess.Popen("sleep 1", shell=True, stdout=subprocess.PIPE).stdout.read())        
        
    if (btcurrent == connected):
        print(subprocess.Popen("echo \"Device connected. RSSI: \"$rssi", shell=True, stdout=subprocess.PIPE).stdout.read())

    if (btconnected != btcurrent):
        if (btcurrent != 0 ):
                print(subprocess.Popen("echo GONE!", shell=True, stdout=subprocess.PIPE).stdout.read())
        if (btcurrent != 1 ):
                print(subprocess.Popen("echo HERE!", shell=True, stdout=subprocess.PIPE).stdout.read())

        btconnected = btcurrent


print(subprocess.Popen("sleep 1", shell=True, stdout=subprocess.PIPE).stdout.read())

print(subprocess.Popen("done", shell=True, stdout=subprocess.PIPE).stdout.read())
''                              
