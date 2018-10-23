import serial

arduino = serial.Serial('/dev/cu.usbmodem146101',
                     baudrate=9600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=1,
                     xonxoff=0,
                     rtscts=0
                     )
# Toggle DTR to reset Arduno
arduino.setDTR(False)
# toss any data already received, see
# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
arduino.flushInput()
arduino.setDTR(True)

arduino.write(b'1')

running = True
with arduino:
    while running:
        arduino.write(b'1')
        input = arduino.readline().decode()
        print(input)

        if input == "1":
            running = False;
