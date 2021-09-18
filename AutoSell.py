import pyautogui
import time

print("Please enter the game at fullscreen mode! Preparing actions...")
default_resolution = [1366, 768]
resolution = list(pyautogui.size())

res_handler = lambda old,new,x,y: list([(x*new[0])/old[0], (y*new[1])/old[1]])

storage_size = int(input("Enter storage size (divisible by 500k): "))
fortune = int(input("Enter fortune level: "))
selling = input("Enter sold items (e.x.: coal, lapis, redstone): ").split(", ")
# default coords
coords_map = dict({"coal": list([538,304]),
                   "lapis": list([574, 304]),
                   "redstone": list([611, 304]),
                   "iron": list([647, 304]),
                   "gold": list([683, 304]),
                   "diamond": list([717, 304]),
                   "emerald": list([752, 304]),
                   "stone": list([793, 304])})
# modes status
status = dict({"coal": False,
               "lapis": False,
               "redstone": False,
               "iron": False,
               "gold": False,
               "diamond": False,
               "emerald": False,
               "stone": False})
# pre-execution steps
for values in selling:
   status.update({values: True})
else:
   print("Keys initialized")
afk_time = (storage_size/500000) * (60*(25-fortune)) # random formula xd

print("Time to start, you have 10 seconds to enter the client in FullScreen")
time.sleep(10)

# farming module
try:
   pyautogui.mouseDown(button='left')
   time.sleep(afk_time)
   pyautogui.mouseUp(button='left')
   time.sleep(1)
   pyautogui.press('t'); pyautogui.write('/kho', interval=0.1)
   pyautogui.keyDown('shift')
   for keys in status.keys():
      if status[keys]:
         coords = coords_map[keys]
         relative = res_handler(default_resolution, resolution, coords[0], coords[1])
         pyautogui.rightClick(x=relative[0], y=relative[1])
      else:
         pass
      time.sleep(0.15) # 15ms delay
except KeyboardInterupt:
   # press CTRL+C or Delete to cancel
   print("Task terminated")
pass
print("Task complete, Coded by Seal - Build v01")
