# Viết 1 chương trình cho phép nhập vào số n (n >= 0)
# Tạo một dãy số [array] với độ dài n+1 (với các số trong dãy nhập bởi người dùng)
# In ra màn hình tất cả các số bị lặp trong dãy
# Ghi chú : Các số nhập bởi người dùng là x (với điều kiện 1 <= x <= n), và không được chỉnh sửa dãy số (tức thêm hoặc xóa số nào đi)

def checkDupe(num, array):
    b = False
    for k in array:
        if k == num:
            b = True
            break
        else:
            pass
    return b


def findDuplicate(array):
    listD = []
    for j in range(0, len(array)):
        if not checkDupe(array[j], listD):
            for z in range(j + 1, len(array)):
                if array[j] == array[z]:
                    listD.append(array[j])
                    break
                else:
                    pass
            pass
        else:
            pass
    for x in listD:
        print(str(x) + " is a duplicate value!")
        pass
    pass


l = []
n1 = input("Input array length: ")
if not n1.isnumeric():
    print("Invalid value...")
    exit(-1)
else:
    exception = 0
    print("Please type in the array's elements: ")
    for p in range(0, int(n1) + 1):
        n2 = input("")
        if n2.isnumeric():
            if 1 <= int(n2) <= int(n1):
                l.append(int(n2))
            else:
                print("Invalid value, skipping...")
                exception += 1
                pass
        else:
            print("Invalid value, skipping...")
            exception += 1
            pass
    print("Confirmed array with " + str(len(l)) + " elements")
    print("Skipped " + str(exception) + "invalid values")
    print("")
    findDuplicate(l)
    print("Array: " + str(l))
