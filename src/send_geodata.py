from os import listdir,rename, makedirs
import requests
from datetime import datetime, timezone
import pathlib



data_list = listdir('/home/pi/get_gps_python/new')
now = datetime.now(timezone.utc)

db = 'collected_data'
influx = 'https://influx.rotekekse.de'

url = influx + '/write?db=' + db


for file in data_list:
    with open ('/home/pi/get_gps_python/new/' + file, "r") as data_point:
        data=data_point.readlines()
    for line in data:
        r = requests.post(url, data=line)
        if '204' == str(r.status_code):
            dt = datetime.fromtimestamp(int(file) // 1000000000)
            dt_s = dt.strftime('%Y-%m-%d')
            makedirs("/home/pi/get_gps_python/" + dt_s, exist_ok=True)
            rename("/home/pi/get_gps_python/new/" + file, "/home/pi/get_gps_python/" + dt_s + "/" + file)

