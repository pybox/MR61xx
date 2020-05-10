# MR61xx
MR61xx series are kinds of uhf rfid reader and writer witch can read uhf rfid tag in long distance.

Dependencies :
============
```bash
pip install pyserial
 ```
USAGE :
============
> To import this library in your code. First, download and copy uhf.py file in your main-code directory.

```python
from uhf import uhf
import serial 
sr = serial.Serial('/dev/ttyUSB0' , 115200 , timeout=1)
rfid = uhf(sr)
print(rfid.reset())
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
