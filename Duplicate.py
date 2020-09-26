# Viết 1 chương trình cho phép nhập vào số n (n >= 0)
# Tạo một dãy số [array] với độ dài n+1 (với các số trong dãy nhập bởi người dùng)
# In ra màn hình tất cả các số bị lặp trong dãy

# Tạo một function để xử lý các số bị lặp, xóa số đó khi bị phát hiện trong dãy
# array - Tên dãy số [array] ; dupeVal - giá trị bị lặp
def duplicateRemover(array, dupeVal):
    for x in range(0, array.count(dupeVal)):
        array.remove(dupeVal)
    pass

# Tạo một function để tìm ra số bị lặp
# Áp dụng function đã tạo ở trên
def duplicateHandler(array):
    duplicate = []
    if len(array) == 0:
        print("Array is empty!")  # Xử lý khi dãy số trống không
        pass
    elif len(array) == 1:
        print("Array only has one element, that is " + str(array[0]))  # Xử lý khi dãy số chỉ có một giá trị
        pass
    else:
        for j in range(0, len(array)):
            for k in range(j + 1, len(array)):
                if array[j] == array[k]:
                    print(str(array[j]) + " is the duplicate value!")  # Báo cho hệ thống
                    duplicate.append(array[j])
                    duplicateRemover(array, array[j])
                    break
                else:
                    pass
    if len(duplicate) == 0:
        print("No duplicate values found within the given array!")
        pass


ar = []
exceptionCount = 0
reader = input("Input array length: ")  # Nhập độ dài
if not reader.isnumeric():
    print("Array length has to be numeric!")
    exit(-1)
else:
    print("Input array elements:")
    for i in range(0, int(reader) + 1):
        k = input("")
        if not k.isnumeric():
            print("Invalid value, input is not an integer, skipping...")
            exceptionCount += 1
            pass
        else:
            if int(k) > int(reader) or int(k) <= 0:
                print("You can only input integers within the range from 1 - " + str(reader))
                print("Skipping value...")
                exceptionCount += 1
                pass
            else:
                ar.append(int(k))
    print("Confirm array. Containing " + str(len(ar)) + " elements, skipping " +
          str(exceptionCount) + " invalid values")
print("Given array: " + str(ar))
print("List of duplicate values: ")
duplicateHandler(ar)
