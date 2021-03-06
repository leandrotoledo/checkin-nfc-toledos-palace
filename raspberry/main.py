import serial
import re
from bot import ToledosPalaceBot

ser = serial.Serial('/dev/ttyACM0', 9600)
last_checking = '';

while True:
    line = ser.readline().strip()
    nfc_content = open('../data/tags.csv','r')
    match = re.search(line+'.*', nfc_content.read(), re.M)
    nfc_content.close()
    if len(line) == 20 and match == None:
        nfc = open('../data/tags.csv','a')
        print(line)
        nfc.write(line+'\n')
        nfc.close()
    else:
        if(match):
            line = match.group()
            find = line.find(',')
            if find > 0 and last_checking != line[find:].replace(',',''):
                last_checking = line[find:].replace(',','')
                ToledosPalaceBot.checkIn(line[find:].replace(',',''))
