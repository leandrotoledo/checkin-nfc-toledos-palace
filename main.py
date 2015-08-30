import serial
import re
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    line = ser.readline().strip()
    nfc_content = open('nfc','r')
    match = re.search(line, nfc_content.read(), re.M)
    nfc_content.close()
    if len(line) == 20 and match == None:
        nfc = open('nfc','a')
        nfc.write(line+'\n')
        nfc.close()
