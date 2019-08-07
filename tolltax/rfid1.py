import serial
def rfidd():
    s=serial.Serial('dev/ttyUSB0',9600)
    #print(s.read(12))
    rd=s.read(12)
    return rd
