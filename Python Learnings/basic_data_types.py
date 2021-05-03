import re

from collections import Counter
import time

shoe_size_cnt = Counter()

mylist = [3,4,3,3]
#shoe_size_cnt[3] += 1
#shoe_size_cnt[4] += 1
#shoe_size_cnt[3] += 1
#shoe_size_cnt[3] += 1

#print(Counter(mylist).)
shoe_size_cnt = Counter(mylist)
print(shoe_size_cnt)
deduct = {3:1}
shoe_size_cnt.subtract(deduct)
print(shoe_size_cnt)
exit(0)
#print(shoe_size_cnt.items())

#print(Counter(mylist).keys())
#print(Counter(mylist).values())

deduct = {3, 1}
Counter(mylist).subtract(deduct)
print(Counter(mylist).items())

cnt = Counter({5:3,2:4})
print(cnt)
#deduct = {1:1, 2:2}
deduct = {5:1}
cnt.subtract(deduct)
print(cnt)

#Counter(mylist).pop(str("3"))
#print(Counter(mylist))

time.sleep(3)

#for i in range(1,10+1):
#        print(i)
exit(0)
#121426 # Here, 1 is an alternating repetitive digit.
#523563 # Here, NO digit is an alternating repetitive digit.
#552523 # Here, both 2 and 5 are alternating repetitive digits.

#525 false
#123 true

while True:
        p = input("input a number:")
        regex_integer_in_range = r"^[1-9]\d\d\d\d\d$"	# Do not delete 'r'.
        regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"	# Do not delete 'r'.

        #print (bool(re.match(regex_integer_in_range, p)) and len(re.findall(regex_alternating_repetitive_digit_pair, p))<2)
        print (bool(re.match(regex_integer_in_range, p)))
        print(p)
        print(re.findall(regex_alternating_repetitive_digit_pair, p))
exit(0)
'''
while True:
        p = input("input a number:")
        pattern_match=r"(\d)(.\1)"
        print(re.findall(pattern_match, p))
        print(len(re.findall(pattern_match,p)))

exit(0)

while True:
        x=input("Input any pattern")
        pat_obj = re.compile('[a-z]+',re.IGNORECASE)
        print(pat_obj)


        result = pat_obj.match(x)
        print (result)

        s = pat_obj.search('1hello')
        print(s)

while True:
    x = (input("please input an integer number of your choice:"))
    #regex_integer_in_range=r"[0-9]"
    if (bool(re.match(r"[^\d]", x))) == True:
        result= re.match(r"[^\d]", x))
        print(result)
    else:
        print("false")
        print(type(x))

line = "dance more"
result = re.match(r"[^\d+]", line)
print result     # Prints out 'dance'

    line = "dance more"
    result = re.match(r"[^\d+]", line)
    result  # Prints out 'dance'

while True:
    x = int(input("please input an integer number of your choice:"))
    if 100000 <= x and x <= 999999:
        print('pincode entered ', x)
    else:
        print("not a correct pincode", x)
'''
