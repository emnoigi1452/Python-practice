import time
import random

possibles = ["Kéo", "Búa", "Bao"]
chart = [[2, 1, 0], [0, 2, 1], [1, 0, 2]]
user = -1
try:
	raw = input("Hãy chọn đi (Kéo, Búa, Bao): ")
	user = possibles.index(raw)
except ValueError:
	print("Chơi đàng hoàng hộ tí :/ Chọn Kéo, Búa, Hoặc Bao thôi!")
computer = random.randint(0,2)
status = chart[user].index(computer)
if status == 0:
	print("\nBạn đã thắng! Máy tính chọn: %s - Bạn chọn: %s" % (possibles[computer], possibles[user]))
	print("Python: Ăn may thôi :( Im đê")
elif status == 1:
	print("\nBạn đã thua rồi! Máy tính chọn: %s - Bạn chọn %s" % (possibles[computer], possibles[user]))
	print("Python: ohshitbanthuaroi, tiếc thật nhỉ :))")
else:
	print("\nHòa! Cả hai bên chọn %s" % (possibles[computer]))
	print("Python: -.-")
pass
print("\nTrò chơi sẽ kết thúc sau 10s!")
time.sleep(10)
