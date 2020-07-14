import mysql.connector
import time
from datetime import datetime
import numpy as np
import simpleaudio as sa

def sound(x,z):
     frequency = x 
     fs = 44100  
     seconds = z  
     t = np.linspace(0, seconds, seconds * fs, False)
     note = np.sin(frequency * t * 2 * np.pi)
     audio = note * (2**15 - 1) / np.max(np.abs(note))
     audio = audio.astype(np.int16)
     play_obj = sa.play_buffer(audio, 1, 2, fs)
     play_obj.wait_done()

intervall_var = input("intervall (in sek[int]): ")

sound(500,2)
print("successful")
i = 1

while True:
    i += 1
    time_set = datetime.now()
    print(str(time_set) + "-"*8)
    try:
        mydb = mysql.connector.connect(
          host="##",
          user="##",
          passwd="##",
          database="##")
        mycursor = mydb.cursor()
        
        print("successfully connected")
        break
    
    except:
        print(str(i) + "failed, connect again in " + str(intervall_var) + "sek.")
        time.sleep(int(intervall_var))

while True:
    sound(500,2)
    time.sleep(3)
