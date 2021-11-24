sublimits = dict({'s': 2, 'p': 6, 'd': 10, 'f': 14})
scripts = '¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ¹⁰ ¹¹ ¹² ¹³ ¹⁴'.split(' ')
print('\nGhi chú: Hãy nhấn -1 nếu bạn không muốn tiếp tục!')
print("-------------------------------------------------")
# Exceptions
unknown = []
for i in range(57, 72):
    unknown.append(i)
for i in range(89, 104):
    unknown.append(i)
while True:
   e = int(input('Nhập vào số electron: '));
   if unknown.count(e) != 0:
       print('Cảnh báo: Nguyên tử có cấu hình đặc biệt!')
       print('Không thể tính toán cấu hình...')
       print('--------------------------------------')
   else:
       charge = e
       if e < 0: break
       configuration = ''; shells = 0; outter = 0
       shell_info = dict({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0})
       shell_id = dict({1: 'K', 2: 'L', 3: 'M', 4: 'N', 5: 'O', 6: 'P', 7: 'Q'})
       sequence = '1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p'.split(', ')
       for level in sequence:
          t = level[1]; limit = sublimits[t]; layer = int(level[0]); addon = 0
          if e >= limit: addon = limit
          else: addon = e
          configuration += (level + scripts[addon-1])
          e -= addon; shell_info.update({layer: shell_info[layer]+addon})
          if e < 1:
             break
       print('Cấu hình của electron: %s' % (configuration))
       print('Các lớp electron:')
       for key in shell_info.keys():
           shell_name = shell_id[key]; shell_count = shell_info[key]
           if shell_count == 0: break
           else:
               print('   %s: %d' % (shell_name, shell_count))
               shells += 1; outter = shell_count

       print("Số lớp electron = %d" % (shells,))
       print("Số electron lớp ngoài cùng = %d" % (outter,))
       print("--------------------------------------")

print('Cảm ơn đã dùng :) Mong bạn thích! Made by Đức Hải Cẽo!')
