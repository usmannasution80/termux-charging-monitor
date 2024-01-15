import time
import os
from Battery import Battery

status = None
battery = Battery()
root_path = os.path.dirname(os.path.realpath(__file__)) + '/'

while True:

  battery_status = battery.get_status()

  if status == None:
    status = battery_status
    time.sleep(1)
    continue

  if status != battery_status:
    status = battery_status
    os.system(
      'termux-media-player '
      + 'play '
      + root_path + status.lower() + '.mp3'
    )