import serial

ser = serial.Serial(port='\\.\COM5', baudrate=9600)

def serialRead():
    while True:
        if(ser.in_waiting > 0):
            line = ser.readline()
            return line

def serialWrite(params):
    params = params.encode()
    ser.write(params)

# while True:
#     serialWrite(str(input("input something :")))

