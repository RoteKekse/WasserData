from datetime import datetime, timezone
import gpsd
import geohash2


gpsd.connect()

packet = gpsd.get_current()
try:
    ghash = geohash2.encode(packet.position()[0],packet.position()[1])
except:
    ghash = 'u'


epoch = datetime(1970,1,1,tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
nano = int((now - epoch).total_seconds() * 1000000000)
val = 10

line = 'test,geohash=' + ghash + ' metric=' + str(val) + ' ' + str(nano) + '\n'


with open('/home/pi/get_gps_python/new/' + str(nano), 'a') as file:
    file.write(line)