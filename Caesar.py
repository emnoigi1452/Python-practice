import string

# Caesar cipher - Encode / Decode
mode = input("Chọn chế độ (Decode / Encode): ")
# Validates mode
if(['decode', 'encode'].count(mode.lower()) == 0):
    print("Chế độ không hợp lệ! Hãy thử lại sau")
else:
    # The default english alphabet, with 26 characters
    alphabet = [c for c in string.ascii_lowercase]
    # The given string
    text = input("Nhập vào xâu kí tự: ").lower()
    # Validates string, check if string has invalid characters
    for i in text:
        if(alphabet.count(i) == 0):
            print("Dãy chữ có chứa kí tự không hợp lệ!")
            exit()
    # Input shift amount
    shift = int(input("Nhập độ lệch: "))
    # Given shift value of x, validates if 1 <= x <= 26
    if(shift < 1 or shift > 26):
        print("Độ lệch không hợp lệ!")
        exit()
    indexes = []; count = 0; i = shift
    # Shift the indexes of the characters
    while count < 26:
        if(i == 26): i = 0
        indexes.append(i)
        count += 1; i += 1
    # Encode / Decode the character
    process = '';
    for c in text:
        revert = ''
        # What the hell did I do here? I have no idea
        if(mode == 'decode'):
            revert = alphabet[indexes.index(alphabet.index(c))]
        else:
            revert = alphabet[indexes[alphabet.index(c)]]
        process += revert
    print('Xâu được phân tích (%s): %s' % (mode,process))
