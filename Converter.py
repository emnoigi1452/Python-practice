print('Nhấn stop để dừng chương trình!')
while True:
   # input handler
   raw_data = input('Nhập số cần đổi và hệ quy đổi: ').split(' ')
   if raw_data[0] == 'stop':
      break
   value,bf,bt = raw_data[0],int(raw_data[1]),int(raw_data[2])
   # data filter
   valids = [2, 10, 16]
   if valids.count(bf) == 0 or valids.count(bt) == 0:
      print('Hệ số nhập vào không hợp lệ!')
      continue
   # result generation
   output = ''
   if bt == 16:
      output = hex(int(value, bf)).replace('0x', '')
   elif bt == 10:
      output = str(int(value, bf))
   else:
      output = bin(int(value, bf)).replace('0b', '')
   bases = {16: 'Hệ Hexa', 10: 'hệ thập phân', 2: 'hệ nhị phân'}
   print(" => Quy đổi '%s' từ %s sang %s: %s" % (value,bases[bf],bases[bt],output))
print('Kết thúc! Mong là bạn thích :)')
