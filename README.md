# MR61xx

MR61xx series is a kind of UHF-RFID reader and writer witch can read UHF-RFID tags in long distances.

Dependencies :
============
```bash
pip install pyserial
 ```
USAGE :
============
> To import this library in your code. First, download and copy uhf.py file in your main-code directory.

## Preparing rfid object
```python
from uhf import uhf
import serial 
sr = serial.Serial('/dev/ttyUSB0' , 115200 , timeout=1)
rfid = uhf(sr)
print(rfid.reset())
```
```
Result :

--Marktrace RFID Reader Bootloader.
>>Version   : V1.3
>>Release   : Apr  2 2019,14:45:31
>>Device ID : 2019102500
>>Ip Addr   : 192.168.001.200
>>SubMask   : 255.255.255.000
>>GateWay   : 192.168.001.001
>>Mac       : 20-19-10-25-00-07
net init ok.
--Jump to main...

```
## Identity and read tag :
```python
count = 0
while(1):
    result = rfid.identity_and_read_tag()
    if result[3] == 0 and result[4] != 0 :
        count+=1
        print(str(count)+'  ' , end='')
        print(result[5:-1])
```
```
Result :

1  b'\r\x00\xe2\x00\x00\x1bp\r\x02\x02!\x904\xc5'
2  b'\r\x00\xe2\x00\x00\x1bp\r\x02\x02!\x904\xc5'
3  b'\r\x00\xe2\x00\x00\x1bp\r\x02\x02!\x904\xc5'
```

