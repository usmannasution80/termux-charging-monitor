from Battery import Battery
from time import sleep

class ChargingObserver:

  battery = None
  status = None

  def __init__(self):
    self.battery = Battery()

  def on_discharging(self):
    pass

  def on_charging(self):
    pass

  def run(self):

    battery_status = self.battery.get_status()

    if self.get_status() == None:
      self.set_status(battery_status)

    elif self.get_status() != battery_status:

      self.set_status(battery_status)

      if self.get_status() == 'DISCHARGING':
        self.on_discharging()

      else:
        self.on_charging()

    sleep(1)
    self.run()

  def set_status(self, status):
    self.status = status

  def get_status(self):
    return self.status