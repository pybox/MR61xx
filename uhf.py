class uhf(object):
    def __init__(self , Serial):
        self.Serial = Serial
        self.status = {
            0x00 : "ERR_NONE",
            0x01 : "ERR_ GENERAL_ERR",
            0x02 : "ERR_PAR_SET_FAILED",
            0x03 : "ERR_PAR_GET_FAILED",
            0x04 : "ERR_NO_TAG",
            0x05 : "ERR_READ_FAILED",
            0x06 : "ERR_WRITE_FAILED",
            0x07 : "ERR_LOCK_FAILED",
            0x08 : "ERR_ERASE_FAILED",
            0x09 : "None",
            0x0A : "None",
            0xFE : "ERR_CMD_ERR",
            0xFF : "ERR_UNDEFINED",
            0xBF : "TIMED_OUT"
        }
        #BINARY COMMANDS
        self.b_interactive_identity = b"\x03\x80\x01"
        self.b_stop_interactive_identity = b"\x02\x81"
        self.head = b'\x0A\xFF'
        self.b_reset = b'\x02\x21'
        self.b_get_tag_data = b'\x03\x41\x01'
        self.b_single_read = b'\x03\x80\x00'
    def calculate_checksum(self , packet : bytes) :
        """
        Calculate checksum for the pac
        :param packet: Binary string to calculate the checksum forr
        :rtype: int
        :return: Checksum value
        """
        checksum = 0
        for x in packet:
            checksum = checksum + int(x)
            if checksum > 255:
                checksum = checksum.to_bytes(2 , 'big')[1]
        checksum = ((~checksum) + 1) & 0xff
        if checksum > 255:
            checksum = checksum.to_bytes(2 , 'big')[1]
        if type(checksum) == int:
            checksum = checksum.to_bytes(1 , 'big')
        return checksum

    def cmd(self , command , is_r):
        pack = self.head + command + self.calculate_checksum( self.head + command )
        self.Serial.flushInput()
        #self.Serial.any()
        self.Serial.write(pack)
        if ( is_r ):
            d = self.Serial.read(1)
            if d == None :
                return 0xbf
            for i in range(2):
                d += self.Serial.read(1)
            for i in range(d[-1]):
                d+= self.Serial.read(1)
            return d
        else :
            return 0
    def reset(self):
        result = self.cmd(self.b_reset , True)
        if result != 0xbf :
            return self.status[result[3]]
        else :
            return self.status[result]
    def identity_single_tag(self):
        result = self.cmd(self.b_single_read , True)
        if result != 0xbf :
            if result[3] == 0 and result[4] != 0 :
                return self.cmd(self.b_get_tag_data , True)
            else :
                return 0
        else :
            return self.status[result]

