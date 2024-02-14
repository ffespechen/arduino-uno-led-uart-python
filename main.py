import serial
import random
import time

ser = serial.Serial(port='/dev/ttyACM0', baudrate=57600)
comandos = {b'R': ">> ROJO", b'A': ">> AMARILLO", b'V': ">> VERDE", b'Z': ">> AZUL", b'*': " >> no procesable"}
claves = list(comandos.keys())

while True:
    opcion = random.choice(claves)
    print(F"Elegido  {comandos.get(opcion)}")
    ser.write(opcion)
    time.sleep(2)