# GPSデータ生成プログラムについて
![gps](https://user-images.githubusercontent.com/41888037/130320820-0c53f230-eb60-4d82-b0cb-3903a17afb5b.png)

このプログラムはのNMEAフォーマットに基づいてGPSのデータを整形するプログラムです。

# 使用方法
オブジェクトを作成する際に、引数に時差を指定してください。日本の場合は9です。    

GPSのデータ(string)をset_data()関数に渡すと、get_location_data()関数で日付・緯度・経度・測位方式の記号・測位方式の説明・スピード（時速）・取得GPS数のタプルを返却します。   
位置情報はGoogle Mapで使用されるDEG形式です。

# サンプルプログラムについて
サンプルプログラムは受信機器がRaspberryPi用に作成されています。シリアル通信を有効にした上でGPSモジュールを接続し、プログラムを実行してください。
![rspi_gps](https://user-images.githubusercontent.com/41888037/130320813-0aa22e4d-886b-4800-a817-0f763eb5763a.jpg)
	
秋月電子通商で販売されているＧＰＳ受信機キット
[AE-GYSFDMAXB](https://akizukidenshi.com/catalog/g/gK-09991/ "AE-GYSFDMAXB") で動作確認が取れています。
# 参考ページ
[GPSのNMEAフォーマット](https://www.hiramine.com/physicalcomputing/general/gps_nmeaformat.html "GPSのNMEAフォーマット")   
[NMEAフォーマットまとめ](http://www.hdlc.jp/~jh8xvh/jp/gps/nmea.html "NMEAフォーマットまとめ")