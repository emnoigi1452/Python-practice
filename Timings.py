import time
import pyautogui

class Timings:
   def __init__(self, data):
      self.data = data
      self.raw_objects = []
      self.objects = []
   def format_file(self):
      reader = False
      for line in self.data.readlines():
         if reader: self.raw_objects.append(line.replace("\n", ""))
         if line.find("HitObjects") != -1:
           reader = True
         pass
   def string_handler(self):
      prev = 0
      for obj in self.raw_objects:
         params = obj.split(',')
         x,y = int(params[0]),int(params[1])
         hit_time = int(params[2]) - prev
         self.objects.append([hit_time, x, y])
         prev = int(params[2])
   def play_the_game(self):
      screen_x,screen_y = pyautogui.size()
      x_multiplier = float(screen_x/640)
      y_multiplier = float(screen_y/480)
      for i in range(len(self.objects)):
         object_info = self.objects[i]
         print("Waiting...")
         time.sleep(float(object_info[0]/1000))
         pyautogui.click(x=int(object_info[1]*x_multiplier), y=int(object_info[2]*y_multiplier))
         print("Clicked: %d and %d" % (int(object_info[1]*x_multiplier), int(object_info[2]*y_multiplier)))
         pass
      print("Map complete")

test = Timings(open("C:\\Users\\Stella\\AppData\\Local\\osu!\\Songs\\1200218 The Living Tombstone - Goodbye Moonmen- Rick and Morty Remix\\The Living Tombstone - Goodbye Moonmen- Rick and Morty Remix (Kyrian) [Pog].osu", "r", encoding='utf-8'))
test.format_file()
test.string_handler()
print("Five seconds to begin")
time.sleep(5)
print("Begin")
pyautogui.press('enter')
test.play_the_game()
pass
