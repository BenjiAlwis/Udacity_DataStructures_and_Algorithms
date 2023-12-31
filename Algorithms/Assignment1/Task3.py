import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""   
    
    
    
def Is_Banglore(phone_num):
    return phone_num[:5]=="(080)"
    

def GetCode(phone_num):
    if phone_num[:2]=="(0":
       return phone_num[1:].split(sep=")")[0] 
    if phone_num[:3]=="140":
        return phone_num[:3]
    return phone_num[:4]


def bangalore_call(call):
    return call[0][0:5] == '(080)'


def extract_area_code(call):
    call_other_interloc = call[1]

    if call_other_interloc[:2] == '(0':  # Fix land case
        return call_other_interloc.split(sep=')')[0] + ')'

    if call_other_interloc[:3] == '140':  # Telemarketer case
        return call_other_interloc[:3]

    else:  # Mobile case
        return call_other_interloc[:4]

#Part A
call_codes=[]
for call in calls:
    if Is_Banglore(call[0]):
       call_codes.append(GetCode(call[1]))
codes_rel_banglore=list(set(call_codes))
codes_rel_banglore.sort()
print("The numbers called by people in Bangalore have codes:")
for code in codes_rel_banglore:
    print(code)
    
#Part B
num_banglore=0                         
for code in call_codes:
    if code=="080":                         
       num_banglore+=1                  
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(num_banglore*100/len(call_codes),2)))

﻿

