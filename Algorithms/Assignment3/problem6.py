import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min_val = ints[0]
    max_val = ints[0]

    for num in ints:
        if num < min_val:
            min_val = num

        if num > max_val:
            max_val = num
        
    return (min_val, max_val)
   
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


m = [i for i in range(10, 20)]  # a list containing 10 - 19
random.shuffle(m)

print ("Pass" if ((10, 19) == get_min_max(m)) else "Fail") 

n = [i for i in range(10, 80)]  # a list containing 10 - 79
random.shuffle(n)

print ("Pass" if ((10, 79) == get_min_max(n)) else "Fail") 


l = [i for i in range(750, 751)]  # a list containing just one value
random.shuffle(l)
print("Pass" if ((750, 750) == get_min_max(l)) else "Fail")


l = []  # an empty array
print("Pass" if (None == get_min_max(l)) else "Fail")


l = [i for i in range(-35, -7)]  # a list containing negative values
random.shuffle(l)
print("Pass" if ((-35, -8) == get_min_max(l)) else "Fail")
