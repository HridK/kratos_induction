def jump_check(distance, length):
    if distance == (length-1):
        return True
    return False


def array_input():
    arr_str = input()
    arr_list = list(map(int,arr_str.split(" ")))
    return arr_list


# __main__
length = int(input())
#Takes the input and changes the input to list of numbers
arr = array_input()
print(jump_check(arr[1],length))
