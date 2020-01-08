import serial,time

ser = serial.Serial()
ser.baudrate = 9600
ser.port= 'COM3'
ser.open()

while True:
    data=[]
    for index in range(0,10):
        datum=ser.read()
        data.append(datum)
        print(data[index])  
    pmtwofive =int.from_bytes(b''.join(data[2:4]), byteorder='little')/10
    print(pmtwofive)
    time.sleep(2)
