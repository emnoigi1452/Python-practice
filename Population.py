import time
import re
import math

print('Máy tính dân số - Coded by Đức Hải Cẽo :3')
print('=> Hướng dẫn sử dụng')
print('------------------------------------')
print('[*] Dữ liệu nhập vào (\'Nhập vào dữ liệu: \')')
print(' - VD: 7.3 2020')
print(' [+] 7.3 là lượng dân số (đơn vị tùy thích: tr, nghìn...)')
print(' [+] 2020 là năm (chỉ chấp nhận số dương nhỏ hơn 4000!)')
print('')
print('[*] Tỉ lệ gia tăng: Chỉ cho phép số thập phân hợp lệ!')
print(' [+] VD: 0.5; 0.3; 1.7; 2.3; ...')
print('------------------------------------')
time.sleep(0.5); act = 0
while True:
    print('')
    if act > 0:
        relyInput = input('Bạn có muốn tiếp tục? (yes/no): ')
        if relyInput == 'yes': pass
        else: break
    act += 1; print('------------------------------------')
    inputManager = input('Nhập vào dữ liệu: ')
    if re.search('(\d{1,}[+.]\d{1}) \d{1,4}', inputManager) == None:
        print('Dữ liệu nhập vào không đúng định dạng!')
    else:
        array = inputManager.split(' ')
        pop = float(array[0])
        year = int(array[1])
        if pop > 0 and year > 0:
            rate = input('Nhập vào tí lệ gia tăng (%): ')
            try:
                rate = float(rate)
            except ValueError:
                print('Số nhập vào không hợp lệ!')
            calculation = (1 + (rate / 100))
            print('------------------------------------')
            print('(Phần hiển thị kết quả. Để dừng, nhập stop)')
            while True:
                result = input('Nhập năm muốn xem kết quả: ')
                if result == 'stop': break
                if re.search('\d{1,4}', result) == None:
                    print('Số nhập vào không hợp lệ!')
                popYear = int(result); value = -1
                dist = int(math.fabs(popYear-year))
                if popYear < year:
                    value = pop / (calculation ** dist)
                else:
                    value = pop * (calculation ** dist)
                print('  => Dân số năm %d là: %s' % (popYear, round(value, 1)))
            print('------------------------------------')
        else: print('Số năm hoặc lượng dân số không hợp lệ!')
print('Đã tắt máy tính...Mong là bạn thích!'); time.sleep(0.5)
print('Coded by Stella (DucTrader)'); time.sleep(0.5)
print('Source code is public on my GitHub Page :3')
