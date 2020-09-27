def removeElement(array, index):
    if index >= len(array):
        print("Index is out of bound!")
        pass
    else:
        for i in range(0, len(array)):
            if i == index:
                array.remove(array[i])
                pass
            else:
                pass
    print("Element with index " + str(index) + " was removed from array!")
