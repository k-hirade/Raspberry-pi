#!/usr/bin/python

import Adafruit_DHT
import datetime

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
pin =4 
try:
     while True:
        date2 = datetime.datetime.now()
        print(date2)
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
except KeyboardInterrupt:
            print('!!FINISH!!')

now_data = datetime.datetime.now()

file = open('/home/hirade/getTemp/Adafruit_Python_DHT/ras_log/ras_log.txt', 'a+')
file.write('{0:%Y/%m/%d %H:%M:%S}, {2:3f}, {1:3f}\n'.format(now_data, temperature,humidity))
