def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    exp = 0
    val1 =0
    val2 =0

    # Sorted input in reverse order
    sorted_array = mergesort(input_list)
    for num in range(0, len(sorted_array), 2):
        val1 += (10 ** exp) *  sorted_array[num]
        exp+=1

    exp = 0
    for num in range(1, len(sorted_array), 2):
        val2 += (10 ** exp) *  sorted_array[num]
        exp+=1
    print(val1," ",val2)
    return [val1, val2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[2, 8, 5, 7, 9, 1], [972, 851]])

test_function([[2, 8, 5, 7, 5, 2], [852, 752]])
test_function([[2, 8, 5, 7, 5, 2,22], [22752, 852]])
test_function([[2, 8, 5, 7, 5, 2,0], [8520, 752]])
test_function([[], []])
test_function([[1], [1,0]])

