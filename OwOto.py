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

# Language option for the command interface
# 'en' (English) or 'vn' (Vietnamese)
# You can change this value to change the language.
LANG = "vn"

# Locales for the script
Locale = {
  'vn': {
    'lang-note': 'Đang tiến hành khởi động - Ngôn ngữ: VN (Tiếng Việt)',
    'ban-input': 'Bạn đã bị ăn ban mấy lần rồi :3 ? ',
    'invalid-bans': 'Số lần không hợp lệ! Đặt mặc định là chưa bị ban!',
    'repo-gen': 'Đã tạo thành công kho lưu trữ config!',
    'client-init': 'Cài đặt hoàn tất! Số lần chạy lệnh: {0}',
    'command-line': 'Đang khởi động bảng điều khiển lệnh... Nhấn \'?help\' để xem lệnh',
    'profile-creation': {
      'update': 'cập nhật',
      'create': 'tạo',
      'msg': 'Đã {0} config cho script với tên \'{1}\'',
    },
    'command-add': 'Đã thêm lệnh \'{0}\' với thời gian chờ {1}s',
    'paused': 'Đã tạm dừng? Bạn có muốn tiếp tục không? (y/n): ',
    'resume': 'Đang tiến hành quay lại vòng lặp...',
    'loop': 'Đang tiến hành chạy vòng lặp #{0}...',
    'cmd-info': 'Lệnh được chọn: {0}',
    'no-cmd': 'Bạn chưa cài đặt lệnh gì cả! Không thể tạo config được đâu!',
    'no-profile-name': 'Vui lòng nhập tên config muốn tải!',
    'invalid-name': 'Tên config có kí tự không hợp lệ! Hãy kiểm tra lại!',
    'unknown-profile': 'Không có config nào mang tên \'{0}\' được lưu cả :(',
    'profile-loaded': 'Đã tải thành công config \'{0}\'!',
    'unset-cmd': 'Hình như bạn chưa thêm lệnh nào vào ._.',
    'msg-info': {
      'name': 'Tên lệnh: \'{0}\'',
      'delay': 'Thời gian chờ: {0}s',
    },
    'prep': 'Bạn có 5 giây để chuẩn bị, nhanh lên nào ~',
    'unknown-cmd': 'Lệnh gì lạ thế :3 ? Kiểm tra lại xem có bấm sai không nào ~',
    'no-lang': 'Vui lòng nhập tên ngôn ngữ muốn chuyển!',
    'unknown-lang': 'Ngôn ngữ này lạ thế :3 ? Chắc là không có rồi ~',
    'lang-change': 'Đã đổi ngôn ngữ thành \'{0}\' thành công!',
    'quitting': 'Đang dừng chương trình...',
    'credits': 'Đã hoàn tất đóng gói, mong là bạn thích ~',
    'help-cmd': [
      'Ghi chú: <> = Bắt buộc có; [] = Tùy chọn',
      '--------------------',
      '?a <(lệnh)> [-d] [(thời gian chờ)]: Thêm lệnh mới (Thời gian chờ mặc định = 1.5s)',
      '?sp <(tên config)>: Lưu config hiện chương trình đang dùng vào kho chứa',
      '?lp <(tên config)>: Tải một config lưu từ trước vào chương trình',
      '?info: Liệt kê các lệnh đã tải vào chương trình',
      '?exec: Bắt đầu chạy bot! Thời gian chuẩn bị = 5s',
      '?q: Thoát chương trình (Thao tác này không lưu config)',
      '?lang: Thay đổi ngôn ngữ của chương trình!'
    ]
  },
  'en': {
    'lang-note': 'Setting things up, wait a moment... Language: English',
    'ban-input': 'How many times have you been banned? ',
    'invalid-bans': 'Invalid number of bans! Using default count of 0',
    'repo-gen': 'Generated new profile repository!',
    'client-init': 'Client has been initialized! Loop size = {0}',
    'command-line': 'Entering command line... Type \'?help\' for more info.',
    'profile-creation': {
      'update': 'updated',
      'create': 'created',
      'msg': 'Successfully {0} profile with ID \'{1}\''
    },
    'command-add': 'Added command \'{0}\' with a delay of {1}s',
    'paused': 'Pause requested! Do you wish to continue? (y/n): ',
    'resume': 'Attempting to resume the loop...',
    'loop': 'Starting loop #{0} in process...',
    'cmd-info': 'Chosen command: {0}',
    'no-cmd': 'No custom commands assigned! Unable to generate a profile!',
    'no-profile-name': 'No profile name specified',
    'invalid-name': 'Invalid profile name!',
    'unknown-profile': 'No profile with the name \'{0}\' exists!',
    'profile-loaded': 'Loaded profile with ID \'{0}\' into the client!',
    'unset-cmd': 'You have not set any custom commands!',
    'msg-info': {
      'name': 'Command name: \'{0}\'',
      'delay': 'Max delay: {0}s'
    },
    'prep': 'You have 5 seconds to prepare! Get ready...',
    'unknown-cmd': 'Unrecognized command! Please check your syntax!',
    'no-lang': 'No language specified! Please check again...',
    'unknown-lang': 'Invalid language name! Please check again...',
    'lang-change': 'Language set to: \'{0}\'',
    'quitting': 'Quitting process...',
    'credits': 'Program has ended! Hope you enjoyed using it!',
    'help-cmd': [
      'Note: <> = Required; [] = Optional',
      '--------------------',
      '?a <(command)> [-d] [(delay)]: Add a custom command (default delay is 1.5s)',
      '?sp <(name)>: Attempt to save the current configuration to the repository',
      '?lp <(name)>: Load a pre-existed configuration to the client',
      '?info: Lists all the custom commands added',
      '?exec: Executes the script! Preparation period: 5s',
      '?q: Quits the program (This action does not automatically save your config)',
      '?lang: Change the program\'s active language'
    ]
  }
}

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
      creation = (Locale[LANG])['profile-creation']
      f.close(); status = update and creation['update'] or creation['create'] 
    print(creation['msg'].format(status, name))
    
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
        print((Locale[LANG])['command-add'].format(parse_cmd, str(delay)))
      
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
        print((Locale[LANG])['loop'].format(str(i+1))); cm = None
        if FakeNode.check():
          cm = FakeNode.gen_command(list(self.commands.keys()), 255)
          if cm.count("#a") > 0:
            self.gamble_execution(cm)
          else:
            self.normal_execution(cm)
          # Pretending to wait for random command output
          _d_ = FakeNode.gen_delay(2,1,5)
          CLOCK.sleep(_d_)
        print(((Locale[LANG])['cmd-info']).format(cm))
        print("-----------------------------")
        BOT.write('sh', interval=0.12); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(1,1,9))
        BOT.write('sb', interval=0.15); BOT.press('enter')
        CLOCK.sleep(FakeNode.gen_delay(15,9,9))
      except:
        # Handle external script pausing
        pause = input((Locale[LANG])['paused'])
        if pause == "n":
          break
        else:
          print((Locale[LANG])['resume'])
          CLOCK.sleep(FakeNode.gen_delay(1,1,6))
      '''
      finally:
        print("meh")
      '''
        

if __name__ == '__main__':
  print("\nOwO Auto - emnoigi1452 (Đức Hải Cẽo) - v0.3.1\n")
  print((Locale[LANG])['lang-note'])
  print("")
  
  # Prefix checker
  is_prefix = lambda a,b: a[:len(b)] == b
  
  # Random setup for the bot
  bans = 0
  try:
    bans = int(input((Locale[LANG])['ban-input']))
  except:
    print((Locale[LANG])['invalid-bans'])
  _client_ = AutoHandle(bans)
  print('--------------------------------------')
  
  # Init profile repository
  if not FILE.exists(REPOSITORY):
    SYSTEM.mkdir(REPOSITORY)
    print((Locale[LANG])['repo-gen'])
  
  print((Locale[LANG])['client-init'].format(str(_client_.loops)))
  CLOCK.sleep(1.5)
  print('--------------------------------------')
  print((Locale[LANG])['command-line'])
  
  # Console output
  while True:
    cmd = input(">> ")
    
    # Adding commands to the randomizer
    if is_prefix(cmd, "?a"):
      params = cmd.split(" "); delay = FakeNode.gen_cap(params)
      params.pop(0); perf = ''.join((r+' ') for r in params)
      _client_.add_command(perf[:-1], delay)
      print((Locale[LANG])['command-add'].format(perf[:-1], str(delay)))
    
    # Saving current profile to repository
    elif is_prefix(cmd, "?sp"):
      if len(_client_.commands.keys()) == 0:
        print((Locale[LANG])['no-cmd'])
        continue
      cmd_params = cmd.split(" ");
      if(len(cmd_params) == 1):
        print((Locale[LANG])['no-profile-name'])
        continue
      sample = REGEX.search('\w+', cmd_params[1])
      if sample is None:
        print((Locale[LANG])['invalid-name'])
        continue
      name = (cmd_params[1])[sample.start():sample.end()]
      Profile.update_profile(name, (_client_.commands))
    
    # Load a pre-existed profile as the current profile
    elif is_prefix(cmd, "?lp"):
      cmd_params = cmd.split(" ");
      if(len(cmd_params) == 1):
        print((Locale[LANG])['no-profile-name'])
        continue
      sample = REGEX.search('\w+', cmd_params[1])
      if sample is None:
        print((Locale[LANG])['invalid-name'])
        continue
      name = (cmd_params[1])[sample.start():sample.end()]
      if not FILE.exists(FakeNode.gen_path(name)):
        print((Locale[LANG])['unknown-profile'].format(name))
        continue
      _client_.commands = Profile.load_profile(name)
      print((Locale[LANG])['profile-loaded'].format(name))
      
    # Display info about all custom commands
    elif is_prefix(cmd, "?info"):
      commands = list(_client_.commands.keys())
      if len(commands) == 0:
        print("You have not set any custom commands")
        continue
      print("----------------------")
      info = (Locale[LANG])['msg-info']
      for n in commands:
        print(info['name'].format(n))
        print(info['delay'].format(str(_client_.commands[n])))
        print("----------------------")
      
    # Execute the client 
    elif is_prefix(cmd, "?exec"):
      print((Locale[LANG])['prep'])
      CLOCK.sleep(FakeNode.gen_delay(4,1,7))
      _client_.execute()
    
    elif is_prefix(cmd, "?lang"):
      params = cmd.split(" ")
      if(len(params) < 2):
        print((Locale[LANG])['no-lang'])
      locale_input = params[1]
      if(list(Locale.keys()).count(locale_input) == 0):
        print((Locale[LANG])['unknown-lang'])
      LANG = locale_input
      print((Locale[LANG])['lang-change'].format(locale_input.upper()))

    elif is_prefix(cmd, "?help"):
      help_menu = list((Locale[LANG])['help-cmd'])
      for line in help_menu:
        print(line)

    # Quit command
    elif is_prefix(cmd, "?q"):
      print((Locale[LANG])['quitting'])
      CLOCK.sleep(FakeNode.gen_delay(0,1,8))
      print("---------------------------")
      break
    
    # Shenanigans
    else:
      print((Locale[LANG])['unknown-cmd'])
print((Locale[LANG])['credits'])
