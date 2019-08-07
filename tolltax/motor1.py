import RPi.GPIO as io
import time
io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(8,io.OUT)
io.setup(7,io.OUT)
def motarclock():
    print("haan bhai chal gyi")
    io.output(8,1)
    io.output(7,0)
def motaranticlock():
    io.output(8,0)
    io.output(7,1)
def motarstop():
    print("bhai motar band ho gyi")
    io.output(8,0)
    io.output(7,0)
