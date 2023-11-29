def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        return
    if number <2:
        return number
    first=1
    last=number
    while first<=last:
        target=(first+last)//2
        squared=target*target
        if squared==number:
            return target
        elif squared>number:
            last=target-1
        else:
            first=target+1
            val=target
    return val


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("Pass" if (sqrt(None) is None) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")

