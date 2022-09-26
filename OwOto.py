# Core modules
import pyautogui as BOT
import time as CLOCK

# Profile handlers
import os as SYSTEM
import re as REGEX
FILE = SYSTEM.path

# Utils
import random
import math

DELAY = 15
RATE = 70
REPOSITORY = "OwOto-Profiles"

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
    return commands[prod]
  
  # Check if a random command should be executed
  @staticmethod
  def check():
    return random.randint(1,100) > RATE
  
  # Parse delay from params input
  @staticmethod
  def gen_cap(params):
    node = 1.5
    try:
      if params[-2] != "-d":
        raise Exception("No delay")
      node = float(params.pop())
      params.pop()
    except:
      pass
    return node
  
  # Generate a path to the profile with the given name
  def gen_path(name):
    return REPOSITORY + "/" + name + ".txt"
  
# Create and save different profiles
class Profile:
  
  # Save the current profile as a configuration
  @staticmethod
  def update_profile(name, delay_map):
    update = FILE.exists(FakeNode.gen_path(name)); data = []
    with open(FakeNode.gen_path(name), 'w') as f:
      
      # Header
      f.write('<--------------------------------->\n')
      
      # Encode to data array
      keys = list(delay_map.keys())
      for k in keys:
        pre = len(str(delay_map[k]).split('.')[1])
        bind = []; base = 10 ** pre
        for c in k:
          bind.append(str(ord(c)))
        bind.append(bin(int(base * delay_map[k])).replace('0b',''))
        bind.append(str(pre))
        data.append(bind)
      
      # Write encoded data to file
      for instance in data:
        for note in instance:
          f.write(note + " ")
        f.write('\n')
        
      # Footer
      f.write('<--------------------------------->\n')
      
      # Close file
      f.close(); status = update and "update" or "created"
    print("Successfully " + status + " profile with ID \'" + name + "\'")
    
  # Load a pre-existed profile into the client
  @staticmethod
  def load_profile(name):
    profile_map = {}
    with open(FakeNode.gen_path(name), 'r') as f:
      
      print("------------------------")
      
      # Initialize the readable data
      data = f.readlines()
      data.pop(); data.pop(0)
      
      # Analyze the data
      for ecmd in data:
        parts = ecmd.split(" "); parts.pop(); float_acc = int(parts.pop())
        delay = float(int(parts.pop(), 2) / (10 ** float_acc))
        parse_cmd = ''.join(chr(int(x)) for x in parts)
        profile_map.update({parse_cmd: delay})
        print("Added command \'%s\' with delay %ss" % (parse_cmd, str(delay)))
      
      print("------------------------")
    
    return profile_map
  
# The main client framework  
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
          cm = FakeNode.gen_command(list(self.commands.keys()), 255)
          if cm.count("#a") > 0:
            self.gamble_execution(cm)
          else:
            self.normal_execution(cm)
          # Pretending to wait for random command output
          _d_ = FakeNode.gen_delay(2,1,5)
          CLOCK.sleep(_d_)
        print("Chosen command: %s" % (cm,))
        print("-----------------------------")
        BOT.write('sh', interval=0.12); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(1,1,9))
        BOT.write('sb', interval=0.15); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(15,9,9))
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
  
  # Prefix checker
  is_prefix = lambda a,b: a[:len(b)] == b
  
  # Random setup for the bot
  bans = 0
  try:
    bans = int(input("How many times have you been banned?: "))
  except:
    print("Invalid number of bans! Using default count of 0")
  _client_ = AutoHandle(bans)
  print('--------------------------------------')
  
  # Init profile repository
  if not FILE.exists(REPOSITORY):
    SYSTEM.mkdir(REPOSITORY)
    print("Generated new profile repository!")
  
  print("Client has been initialized! Size = %d loops" % (_client_.loops))
  CLOCK.sleep(1.5)
  print('--------------------------------------')
  print("Entering command line...")
  
  # Console output
  while True:
    cmd = input(">> ")
    
    # Adding commands to the randomizer
    if is_prefix(cmd, "?a"):
      params = cmd.split(" "); delay = FakeNode.gen_cap(params)
      params.pop(0); perf = ''.join((r+' ') for r in params)
      _client_.add_command(perf[:-1], delay)
      print("Added \'" + perf[:-1] + "\' to command map with delay of " + str(delay) + "s")
    
    # Saving current profile to repository
    elif is_prefix(cmd, "?sp"):
      if len(_client_.commands.keys()) == 0:
        print("No custom commands assigned! Unable to generate a profile!")
        continue
      cmd_params = cmd.split(" ");
      if(len(cmd_params) == 1):
        print("No profile name identified!")
        continue
      sample = REGEX.search('\w+', cmd_params[1])
      if sample is None:
        print("Invalid name!")
        continue
      name = (cmd_params[1])[sample.start():sample.end()]
      Profile.update_profile(name, (_client_.commands))
    
    # Load a pre-existed profile as the current profile
    elif is_prefix(cmd, "?lp"):
      cmd_params = cmd.split(" ");
      if(len(cmd_params) == 1):
        print("No profile name identified!")
        continue
      sample = REGEX.search('\w+', cmd_params[1])
      if sample is None:
        print("Invalid name!")
        continue
      name = (cmd_params[1])[sample.start():sample.end()]
      if not FILE.exists(FakeNode.gen_path(name)):
        print("No profile with the specified name \'%s\' was found!" % (name))
        continue
      _client_.commands = Profile.load_profile(name)
      print("Loaded profile with ID \'%s\' into the client." % (name))
      
    # Display info about all custom commands
    elif is_prefix(cmd, "?info"):
      commands = list(_client_.commands.keys())
      if len(commands) == 0:
        print("You have not set any custom commands")
        continue
      print("----------------------")
      for n in commands:
        print("Command name: %s" % (n))
        print("Max delay: %ss" % (str(_client_.commands[n])))
        print("----------------------")
      
    # Execute the client 
    elif is_prefix(cmd, "?exec"):
      print("You have 5 seconds to prepare! Get ready")
      CLOCK.sleep(FakeNode.gen_delay(4,1,7))
      _client_.execute()
    
    # Quit command
    elif is_prefix(cmd, "?q"):
      print("Quitting process....")
      CLOCK.sleep(FakeNode.gen_delay(0,1,8))
      print("---------------------------")
      break
    
    # Shenanigans
    else:
      print("Unrecognized command! Please check your syntax...")
print("Program has been ended! Hope you enjoyed using it!")
