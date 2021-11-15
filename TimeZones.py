import re

degs = []
for w in range(180, 14, -15):
    degs.append(str(w) + 'T')
degs.append('0')
for e in range(15, 181, 15):
    degs.append(str(e) + 'D')
while True:
    # Câu lệnh chỉ định: y = yes, n = no
    command = input('Bạn còn muốn tiếp tục không? (y/n): ')
    if command == 'y':
        # Nhập vĩ độ theo định dạng độHướng (VD: 150T, 150D)
        # Với 0Đ (Tại đài thiên văn greenwich), nhập mẹ số 0 hộ bố
        kd = input("Nhập vĩ độ của giờ đã biết (vd: 150T): ")
        if kd != '0' and re.search("\d{3}[T,D]", kd) == None:
            print("Định dạng vĩ độ không hợp lệ!")
        if kd != '0':
            objt = int(kd[0:-1]) / 15
        else: objt = 0
        if objt < 0 or objt > 12:
            print("Vĩ độ không hợp lệ!"); break
        # Nhập giờ theo định dạng: 00h00P (vd: 08h45p, 15h00p)
        time = input("Nhập giờ đã biết: ")
        if re.search('\d{2}h\d{2}p', time) == None:
            print("Định dạng giờ không hợp lệ!"); break
        hour = int(time[0:2]); min = time[3:]
        mint = int(min[:-1])
        if mint > 60:
            print("Định dạng giờ không hợp lệ!"); break
        tw = kd[-1] == 'D' and 1 or -1
        greenwich = hour - (objt * tw); node = ''; back = '0'
        if greenwich < 0:
            greenwich += 24
            back = '-1'
        elif greenwich > 24:
            greenwich -= 24
            back = '+1'
        else: pass
        pin = greenwich;
        board = {'0': greenwich}
        day = {'0': back}
        node = back
        for x1 in range(15, 181, 15):
            wk = str(x1) + "T"
            pin -= 1
            if pin == -1:
                if node == "+1": node = "0"
                elif node == "0": node = "-1"
                else: node = node[0] + str(int(node[1])-1)
                pin = 23
            if list(board.keys()).count(wk) == 0:
                board.update({wk: pin})
                day.update({wk: node})
            else: continue
        pin = greenwich; node = back
        for x2 in range(15, 181, 15):
            ek = str(x2) + "D"
            pin += 1
            if pin == 24:
                if node == "-1": node = "0"
                elif node == "0": node = "+1"
                else: node = node[0] + str(int(node[1])-1)
                pin = 0
            if list(board.keys()).count(ek) == 0:
                board.update({ek: pin})
                day.update({ek: node})
            else: continue
        print("Từ thông tin đã có, ta lập ra bảng thời gian sau:", end="\n\n")
        print("   Vĩ độ     |     Thời điểm")
        for placement in degs:
            print("--------------------------------------")
            moment = int(board[placement])
            h = str(moment)
            if len(h) == 1: h = '0' + h
            format = h + "h" + min
            pointer = 4 - len(placement);
            adeg = placement + (''.join(' ' for i in range(pointer)))
            print("   " + adeg + "              " + format + " [Ngày: " + day[placement] + "]")
    elif command == "n":
        print("Mong là bạn thích :) Coded by Đức Hải Cẽo"); break
    else:
        print("Lệnh gì đây :\ Mình không hiểu đâu, thôi tắt luôn vậy..."); break
