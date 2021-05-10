from gpiozero import PWMLED
from time import sleep
from datetime import datetime
pumpL = PWMLED(17)
pumpR = PWMLED(18)
pump_l_on = 0
pump_r_on = 1

def get_milli():
  dt = datetime.now()
  return dt

start_millis = get_milli()
mode = "tail"

pump_power = 1
tail_hz = .5
pumptime = 1000/(tail_hz) # Time to turn the pumps on
starting = True
switch = True
print("pumptime: ", pumptime)

tail_time = start_millis # Last time that the tail was switched
print("starttime: ", start_millis)
while True:
    ## Main Control loop
    # Check for keypresses

    curr_time = get_milli()
    if mode == "tail":

      if starting:
        print("starting")
        # Doa half sequence for starting!
        pumpL.value = pump_power*pump_l_on # off
        pumpR.value = pump_power*pump_r_on  # off
        # Somehow 
        if (curr_time-tail_time).total_seconds()*1000 >= pumptime/2:
          starting = False
          switch = True
          print("Normal operation")
          tail_time = curr_time
      if switch:
        print("Switch the pumps!!")
        temp = pump_r_on 
        pump_r_on = pump_l_on
        pump_l_on = temp
        pumpL.value = pump_l_on*pump_power  # off
        pumpR.value = pump_r_on*pump_power  # off
        tail_time = curr_time
        switch = False
      else: 
        if (curr_time-tail_time).total_seconds()*1000 >= pumptime:
          switch = True

    sleep(.01)
pump.value = 0
