import RPi.GPIO as io
#from motor1 import *
import time
io.setwarnings(False)
io.setmode(io.BOARD)
trig,echo =3,5
io.setup(trig,io.OUT)
io.setup(echo,io.IN)
def ultraa():
    io.output(trig,1)
    time.sleep(0.00001)
    io.output(trig,0)
    while(io.input(echo)==0):
        pass
    start=time.time()
    while(io.input(echo)==1):
        pass
    stop=time.time()
    tym=stop-start
    dis=tym*34300
    dis=dis/2
    return dis
        #keshav agrawal




