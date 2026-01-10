#Problem: Reverse a string using a loop.


def reverse_string(string):
    str_list = string.split("")
    print(str_list)
    for i in range(len(str_list)):
        if i == len(str_list) // 2:
            break   
        str_list[i], str_list[len(str_list) - 1 - i] = str_list[len(str_list) - 1 - i], str_list[i]
    
    return " ".join(str_list)


print(reverse_string("Hello"))