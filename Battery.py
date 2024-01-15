import os
import json

class Battery:

  def get_status_all(self):

    root_path = os.path.dirname(os.path.realpath(__file__)) + '/'
    temp_path = root_path + 'temp'
    battery_status_prompt = 'termux-battery-status > ' + temp_path
  
    os.system(battery_status_prompt)
  
    temp_file = open(temp_path)
    battery_status = json.loads(temp_file.read())
    temp_file.close()

    os.system('rm ' + temp_path)

    return battery_status

  def get_status(self):
    return self.get_status_all()['status']