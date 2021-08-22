import time
import pyautogui

inval = int(input("Enter amount of times: "))
print("Bạn có năm giây để chuẩn bị!")
time.sleep(5)


for i in range(0, inval):
	time.sleep(0.05)
	pyautogui.click(button='right')
	time.sleep(0.05)
	pyautogui.mouseDown(button='left')
	time.sleep(0.4)
	pyautogui.mouseUp(button='left')
	print("Đã đặt: ", end=str(i+1) + "\n")
print("Xong rồi nhé! Hẹn gặp lại lần sau")
