def rotated_array_search(input_list, number):

    if len(input_list)==0:
        return -1
    first_i = 0
    last_i = len(input_list) - 1
    mid_i = (first_i + last_i) // 2
    first_item = input_list[first_i]
    last_item = input_list[last_i]
    if first_item <= last_item:#in order
        return search(input_list, number)
    else:
        while first_i <= last_i:
            mid_i = (first_i + last_i) // 2
            first_item = input_list[first_i]
            last_item = input_list[last_i]
            mid_item = input_list[mid_i]
            if first_item <= last_item: #now in order
                    target_i=search(input_list[0:first_i], number)
                    if(target_i!=-1 and input_list[target_i]==number):
                        return target_i
                    target_i=search(input_list[first_i:], number)
                    if(target_i!=-1 and input_list[first_i+target_i]==number):###
                        return first_i+target_i
                    break
            elif first_item <= mid_item: 
                    first_i = mid_i + 1 
            elif mid_item <= last_item: 
                    last_i = mid_i
            else: # index not found
                    return -1
    return -1
        
def search(input_list, number):
    
    first_i = 0
    last_i = len(input_list) - 1

    while first_i <= last_i:

        mid_i = (first_i + last_i) // 2
        if number == input_list[mid_i]: 
            return mid_i
        if number < input_list[mid_i]: 
            last_i = mid_i - 1
        else: 
            first_i = mid_i + 1

    return -1
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[], 10])        
test_function([[8], 8])
test_function([[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 13])
test_function([[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 3])

        
﻿

