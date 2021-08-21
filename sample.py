#!/usr/bin/env python
# -*- coding: utf-8 -*-
import NMEA_parser
import serial
import time
import threading

# 設定(ここから)
time_difference = 9     # 時差(日本+9時間)
# 設定(ここまで)

nmea_parser = NMEA_parser.NMEA_parser(time_difference)

def get_gps_data():
    s = serial.Serial('/dev/serial0', 9600, timeout=None)
    while True:
        try:
            line = s.readline().decode('utf-8')
            if line[0] == '$': nmea_parser.set_data(line)
        except:
            print("deta_err")

if __name__ == "__main__":
    thread_get_gps = threading.Thread(target=get_gps_data, args=())
    thread_get_gps.start()

    while True:
        now_gps_data = nmea_parser.get_location_data()
        print(now_gps_data)
        nmea_parser.data_clear()
        time.sleep(1)