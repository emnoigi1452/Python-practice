import random

player = input("Hãy chọn đi [Kéo, Búa, Bao]: ")
computer = ["Kéo", "Bao", "Búa"][random.randint(0,2)]

result = 0

if player == "Kéo":
	if player == computer: result = 0
	elif computer == "Bao": result = 1
	else: result = 2 
elif player == "Búa":
	if player == computer: result = 0
	elif computer == "Kéo": result = 1
	else: result = 2 
elif player == "Bao":
	if player == computer: result = 0
	elif computer == "Búa": result = 1
	else: result = 2 
else:
	print("Thưa bạn ơi, {} là cái đéo gì thế?".format(player))

if result == 1: print("Ơ kìa, sao mình lại thua :(( Nhường m đấy")
elif result == 2: print("Chetmemaydi con chó rách")
else: print("Tạm hoà nhé! Lần sau bố mày sẽ thắng :'(")

print("Bạn đã chọn: {} - Python đã chọn: {}".format(player, computer))
print("Trò chơi sẽ khép lại sau 10 giây! Chụp gì thì chụp đi :v")
time.sleep(10)
