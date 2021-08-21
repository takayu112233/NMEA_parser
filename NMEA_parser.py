#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

class NMEA_parser():
    GPZDA = [] #時間
    GPRMC = [] #位置情報
    GPVTG = [] #移動情報
    GPGSV = [] #GPS情報

    time_difference = 0

    def __init__(self, time_difference):
        # 時差の指定
        self.time_difference = time_difference

    def set_data(self,line_str):
        # 取得したgpsデータをもとに格納
        #print(line_str)
        split_data = line_str.split(',')
        #print(split_data)
        if(split_data[0] == "$GPZDA"):  self.GPZDA = split_data
        if(split_data[0] == "$GPRMC"):  self.GPRMC = split_data
        if(split_data[0] == "$GPVTG"):  self.GPVTG = split_data
        if(split_data[0] == "$GPGSV"):  self.GPGSV.append(split_data)
    
    def get_gps_time(self):
        #gps取得した時間を返却
        if(self.GPZDA == []):
            return -1
        else:
            time_str = "%s/%s/%s %s" % (self.GPZDA[4],self.GPZDA[3],self.GPZDA[2],self.GPZDA[1].split('.')[0])
            time_datetime = datetime.datetime.strptime(time_str, '%Y/%m/%d %H%M%S') + datetime.timedelta(hours=self.time_difference)
            return time_datetime
    
    def dmm_to_deg(self,dmm):
        #DMM形式からDEG形式に変換
        d1 = int(dmm/100)
        d2 = (dmm - d1*100) / 60
        dmm = d1 + d2
        return dmm
        
    def get_location_data(self):
        #時間・緯度・経度・位置取得情報記号・位置取得方法・速度を返却
        time = "-"
        latitude_deg = -1
        longitude_deg = -1
        gps_method_e = "-"
        gps_method = "-"
        speed = "-"
        gps_cnt = "-"

        try:
            if(self.GPVTG != []): speed = self.GPVTG[7]
        except:
            speed = "-"

        try:
            if(self.GPRMC != []):
                latitude_dmm = float(self.GPRMC[3]) #緯度
                if(self.GPRMC[4] != "A"): latitude_dmm * -1
                longitude_dmm = float(self.GPRMC[5]) #経度
                if(self.GPRMC[6] != "E"): longitude_dmm * -1
            
                latitude_deg = format(self.dmm_to_deg(latitude_dmm), '.6f')
                longitude_deg = format(self.dmm_to_deg(longitude_dmm), '.6f')

                gps_method_key = {"N" : "データなし", "A" : "自立方式", "D" : "干渉測位方式", "E" : "推定"}
                gps_method = gps_method_key[self.GPRMC[12][0]]
                gps_method_e = self.GPRMC[12][0]
        except:
            pass
        
        try:
            if(self.GPGSV != []):
                gps_cnt = self.GPGSV[0][1]
        except:
            pass

        try:
            time = self.get_gps_time().strftime("%Y/%m/%d %H:%M:%S")
        except:
            pass
     
        return (time,latitude_deg,longitude_deg,gps_method_e,gps_method,speed,gps_cnt)
        
    def data_clear(self):
        #取得データのリセット
        self.GPZDA = []
        self.GPRMC = []
        self.GPVTG = []
        self.GPGSV = []