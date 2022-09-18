# Core modules
import pyautogui as BOT
import time as CLOCK

# Utils
import random
import math

DELAY = 15
RATE = 70

# Simulate the patterns to match that of someone who has too much free time
# This does not make it impossible to be asked a verification
class FakeNode:
  
  # Generate a custom delay
  @staticmethod
  def gen_delay(base, seed, acc):
    start = 10 ** acc
    p = random.randint(start, (seed*start))
    return float(base + (p / start))
  
  # Generate a random index and return the corresponding command
  @staticmethod
  def gen_command(commands, layer):
    mix = lambda x: bin(x).replace('0b','')
    t = random.randint(1, layer)
    x = t; y = t << 1; n = len(commands)
    for i in range(layer):
      repstr = mix(x) + mix(y)
      x = int(repstr[:7],2)
      y = random.randint(1, x)
    prod = int(math.sqrt(x*y)) % n
    if prod < 0:
      prod = prod * (-1)
    if prod >= n:
      prod = prod % n
    return commands[prod]
  
  # Check if a random command should be executed
  @staticmethod
  def check():
    return random.randint(1,100) > RATE
  
class AutoHandle:
  
  # Constructor
  def __init__(self, bans):
    self.loops = 500 - (int(bans)*80)
    if self.loops < 0:
      self.loops = 500
    self.commands = {}
    self.gamble = [10,50]
    
  # Add a command to the automation belt
  # Param(s): [command, <base delay>]
  def add_command(self, command, seed):
    self.commands.update({command: seed})
    
  # Execute a normal command
  def normal_execution(self, id):
    BOT.write(id, interval=0.1); BOT.press('enter')
    CLOCK.sleep(FakeNode.gen_delay(self.commands[id], 2, 6))
  
  # Execute a gambling command
  def gamble_execution(self, id):
    func = lambda: random.randint(self.gamble[0], self.gamble[1])
    a, b = func(), func()
    bet = int(math.sqrt(a*b)) * 100
    BOT.write(id.replace('#a', str(bet))); BOT.press('enter')
    CLOCK.sleep(FakeNode.gen_delay(self.commands[id], 2, 6))
  
  # Main core of the client, where everything runs
  def execute(self):
    for i in range(self.loops):
      try:
        # Function
        print("Starting loop #%d in process..." % (i+1)); cm = None
        if FakeNode.check():
          cm = FakeNode.gen_command(list(self.commands.keys()), 16)
          if cm.count("#a") > 0:
            self.gamble_execution(cm)
          else:
            self.normal_execution(cm)
          # Pretending to wait for random command output
          _d_ = FakeNode.gen_delay(2,1,5)
          CLOCK.sleep(_d_)
        print("Chosen command: %s" % (cm,))
        BOT.write('sh', interval=0.12); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(1,1,9))
        BOT.write('sb', interval=0.15); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(15,9,9))
        print("-----------------------------")
      except:
        # Handle external script pausing
        pause = input("Pause requested! Do you wish to continue?: ")
        if pause == "n":
          break
        else:
          print("Returning to loop...")
          CLOCK.sleep(FakeNode.gen_delay(1,1,6))
      '''
      finally:
        print("meh")
      '''
        

if __name__ == '__main__':
  print("OwO Auto - emnoigi1452 (Đức Hải Cẽo) - v0.2")
  
  # Random setup for the bot
  bans = int(input("How many times have you been banned?: "))
  _client_ = AutoHandle(bans)
  
  print("Client has been initialized! Size = %d" % (_client_.loops))
  print("Entering command line...")
  
  # Console output
  while True:
    cmd = input(">> ")
    
    # Adding commands to the randomizer
    if cmd.count("?a") > 0:
      params = cmd.split(" ");
      params.pop(0); perf = ''.join((r+' ') for r in params)
      _client_.add_command(perf, 2.5)
      print("Added \'" + perf + "\' to command map!")
      
    # Execute the client 
    elif cmd.count("?exec") > 0:
      print("You have 5 seconds to prepare! Get ready")
      CLOCK.sleep(FakeNode.gen_delay(4,1,7))
      _client_.execute()
    
    # Other commands = quit
    else:
      break
print("Program has been ended! Hope you enjoyed using it!")
      
        
