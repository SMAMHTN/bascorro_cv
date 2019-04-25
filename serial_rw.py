import serial

ser = serial.Serial("/dev/serial0", baudrate=115200, timeout=1.0)

def serialRead():
    while True:
        if(ser.in_waiting > 0):
            line = ser.readline()
            return line

def serialWrite(x,y):
        ser.write("!".encode())
        #print("X=")
        #print(x)
        ser.write(str(int(x)).encode())
        ser.write("|".encode())

        ser.write("@".encode())
        #print("Y=")
        #print(y)
        ser.write(str(int(y)).encode())
        ser.write("|".encode())

        ser.write("\r\n".encode())

#while True:
#    serialWrite(x,y)
