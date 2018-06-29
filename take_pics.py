from picamera import PiCamera
from time import sleep
from datetime import datetime, timezone
import pytz
from astral import Astral

Israel_TZ = pytz.timezone('Israel')
a = Astral()
a.solar_depression = 'civil'
city = a['Jerusalem']


with PiCamera() as camera:
    camera.resolution = (1296,972)
    sleep(2)
    while True:
        time_now = datetime.now(tz=Israel_TZ)
        sun = city.sun(date=time_now, local=True)
        if sun['dawn'] < time_now < sun['dusk']:
            x=time_now.strftime("%Y-%m-%d %H:%M:%S")
            camera.capture('/mnt/nas/{}.jpg'.format(x))
            print(x)
        sleep(30)
        
        
 