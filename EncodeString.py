while True:
   st = input("Nhập xâu kí tự (Nhấn 'stop' để dừng lại): ")
   if st == "stop": break
   bytear = bytearray(st, 'utf-8')
   k = list([])
   for c in bytear:
      k.append(bin(c).replace('0b', ''))
   result = ''
   for bc in k:
      if len(bc) < 8: result += ''.join('0' for i in range(8-len(bc))) + bc
      else: result += bc
      result += ' '
   else:
      print('Mã nhị phân: %s' %(result,))
else: print("Xong hết rồi đấy!")
