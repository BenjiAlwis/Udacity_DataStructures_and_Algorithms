import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""    
    
telephone_numbers = set()
for index in range(2):
 temp_telephone_numbers = [text[index] for text in texts]
 telephone_numbers.update(temp_telephone_numbers)
 temp_telephone_numbers = [call[index] for call in calls]
 telephone_numbers.update(temp_telephone_numbers)
    

print("There are {} different telephone numbers in the records.".format(len(telephone_numbers)))

﻿

