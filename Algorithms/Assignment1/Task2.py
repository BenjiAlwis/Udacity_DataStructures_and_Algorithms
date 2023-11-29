import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time_spent=dict()
for call in calls:
    if call[0] in time_spent:
        time_spent[call[0]]+=int(call[3])
    else:
        time_spent[call[0]]=int(call[3])
    if call[1] in time_spent:
        time_spent[call[1]]+=int(call[3])
    else:
        time_spent[call[1]]=int(call[3])
max_time = 0
max_num = ' '
   
for phone_num,t_val in time_spent.items():
   if t_val > max_time:
     max_time = t_val
     max_num =  phone_num  
        
   
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_num, max_time))



