import os
import json
import time

status = None

while True:
  root_path = os.path.dirname(os.path.realpath(__file__)) + '/'
  temp_path = root_path + 'temp'
  battery_status_prompt = 'termux-battery-status > ' + temp_path

  os.system(battery_status_prompt)

  temp_file = open(temp_path)
  battery_status = json.loads(temp_file.read())
  temp_file.close()

  if status == None:
    status = battery_status['status']
    time.sleep(1)
    continue

  if status != battery_status['status']:
    status = battery_status['status']
    os.system(
      'termux-media-player '
      + 'play '
      + root_path + status.lower() + '.mp3'
    )