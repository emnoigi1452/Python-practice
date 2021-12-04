import time
import re

# Note (Ghi chú):
#   [1] - Khi nhập sát thương/sức thủ, hãy nhập theo định dạng sau:
#                (min)-(max) hay (const)
#       VD: 10-20,
#           15.75-20.25,
#           8.5-12.75,
#           10.5,
#           25,
#           31.25
#   [2] - Khi nhập cấp độ của vật phẩm, chỉ được nhập số nguyên từ 1-30
#   [3] - Khi nhập chế độ hiển thị kết quả tính toán, bạn có thể chọn
#         một trong các chế độ sau đây:
#       [-] f: Hiển thị tất cả chỉ số từ level hiện tại - level max (30)
#       [-] a: Hiển thị tất cả chỉ số từ level 1 - 30
#       [-] <Một số nguyên x>: Hiển thị chỉ số của level x

print('Máy tính chỉ số - MyItems - Coded by Stella')
print('-------------------------------------------')
print('Lưu ý: Đọc phần ghi chú của code để biết cách dùng <3')
time.sleep(1); actions = 0
while True:
    if actions > 0:
        poll = input('Bạn muốn tiếp tục không? (yes/no): ')
        if poll == 'yes': pass
        elif poll == 'no': break
        else:
            print('Lệnh không hợp lệ! Tự động bỏ qua...')
            pass
    actions += 1; print('')
    stats1 = input('  - Nhập vào sát thương/sức thủ: ')
    if (re.search('\S{1,}-\S{1,}', stats1) == None) and (re.search('\S{1}', stats1) == None):
        print('  [!] Định dạng chỉ số vật phẩm không hợp lệ!')
    else:
        loader = [float(arg) for arg in stats1.split('-')]; level = 1; scale = float(1)
        if (len(loader) == 2) and (loader[0] > loader[1]):
            temp = loader[1]
            loader[1] = loader[0]
            loader[0] = temp
        if len(loader) == 2: scale = float(loader[1] / loader[0])
        try:
            level = int(input('  - Nhập vào cấp độ của vật phẩm (1-30): '))
            if (level < 1) or (level > 30):
                print('  [!] Cấp độ vật phẩm không hợp lệ!')
            else: pass
        except ValueError:
            print('  [!] Định dạng số không hợp lệ!')
        float_calculation = (1 + 0.05 * level) / (1 + 0.05 * (level-1))
        next = loader[0] * float_calculation
        diff_base = next - loader[0]; roller = loader[0]
        node = (len(loader) == 2) or scale != 1
        for x in range((level-1)):
            roller -= diff_base
        stats_map = dict({})
        for i in range(30):
            base = roller + diff_base * i
            if node:
                stats_map.update({i+1: str(round(base, 2)) + " - " + str(round(float(base*scale), 2))})
            else:
                stats_map.update({i+1: str(round(base, 2))})
        print('------------------------------------------------')
        time.sleep(1)
        display = input('  - Nhập chế độ hiển thị kết quả tính toán: ');
        print('------------------------------------------------')
        if (display.lower() == 'a') or (display.lower() == 'f'):
            start = display.lower() == 'a' and 1 or level
            print('  - Đang hiển thị tất cả chỉ số từ level %d-30...' % (start)); print('')
            time.sleep(1.5)
            for keys in range(start, 31):
                print('  [+] Cấp %d: %s' % (keys, stats_map[keys]))
                print('--------------------------')
        elif re.search('\d{1,2}', display.lower()) != None:
            handle = int(display[:re.search('\d{1,2}', display.lower()).end()])
            print('  [+] Chỉ số của cấp %d: %s' % (handle, stats_map[handle]))
        else:
            print('  [!] Tùy chọn không hợp lệ! Vui lòng đọc kĩ hướng dẫn!')
            print('--------------------------')
        print('')
print('Mong là bạn thích! - Made by DucTrader')
