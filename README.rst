# MR61xx
MR61xx series is a kind of uhf rfid reader and writer witch can read uhf rfid tag in long distance.

Dependencies :
============
.. code::
    pip install pyserial
 
Usage Code :
============
To import this library in your code. First, download and copy uhf.py file in your main-code directory.

```python
  from uhf import uhf
  import serial 
  sr = serial.Serial('/dev/ttyUSB0' , 115200 , timeout=1)
  rfid = uhf(sr)
  print( rfid.get_version )
```
