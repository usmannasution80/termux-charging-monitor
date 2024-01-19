import time
import os
from ChargingObserver import ChargingObserver

root_path = os.path.dirname(os.path.realpath(__file__)) + '/'

class MyChargingObserver(ChargingObserver):

  def on_discharging(self):
    os.system(
      'termux-media-player '
      + 'play '
      + root_path + self.get_status().lower() + '.mp3'
    )

  def on_charging(self):
    os.system(
      'termux-media-player '
      + 'play '
      + root_path + self.get_status().lower() + '.mp3'
    )

MyChargingObserver().run()
