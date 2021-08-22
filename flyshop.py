import pyautogui
import time

print("Bạn có 5 giây")
time.sleep(5)
x = 0
for i in range(0, 100):
	time.sleep(0.5)
	pyautogui.press('t')
	time.sleep(0.1)
	pyautogui.write("/flyshop", interval=0.025)
	pyautogui.press('enter')
	time.sleep(0.25)
	pyautogui.moveTo(651, 307)
	time.sleep(0.75)
	pyautogui.click()
	x += 1
	print("Đã mua: ", end=str(x) + " lần\n")
print("Mua xong rồi đấy :D")
