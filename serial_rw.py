import serial

ser = serial.Serial("/dev/serial0", baudrate=115200, timeout=1.0)

def serialRead():
    while True:
        if(ser.in_waiting > 0):
            line = ser.readline()
            return line

def serialWrite(x,y):
        ser.write("!")
        print("X=")
        print(x)
        ser.write(str(x))
        ser.write("|")

        ser.write("@")
        print("Y=")
        print(y)
        ser.write(str(y))
        ser.write("|")

        ser.write("\r\n")

#while True:
#    serialWrite(x,y)
