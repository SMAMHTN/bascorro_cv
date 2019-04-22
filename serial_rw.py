import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

def serialRead():
    while True:
        if(ser.in_waiting > 0):
            line = ser.readline()
            return line

def serialWrite(params):
    params = params.encode()
    ser.write(params)

while True:
    serialWrite(str(input("input:")))
