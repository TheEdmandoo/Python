import serial 

port = serial.Serial("/dev/tty.usbmodem1421",9600,timeout=2) 

input = port.readline()
print(input)

port.write("Wassup")
port.close()
