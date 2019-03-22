##pip install serial
import serial
##import MySQLdb as mdb
import time

while True:
      arduino_data = serial.Serial("/dev/ttyACM0")
      arduino_data.baudrate = 57600

      data = arduino_data.readline()
      time.sleep(1)
      data = arduino_data.readline()
##      print(data)
##      new_data = str(data).split(" ")
##      temp = new_data[0]
##      hum = new_data[1]
##      brig = new_data[2]
      print("vrednosti: ", data)
      
      f = open("data.txt", "w")
      f.write(str(data))
      f.close()

##      conn = mdb.connect('localhost', 'username', 'passw', 'bazadb') #phpmyadmin
##      with conn:
##            cursor = conn.cursor()
##            cursor.execute("""INSERT INTO bazadb VALUES('', %s, %s, %s)""", (temp, hum, brig))
##            conn.commit()
##            conn.close()

