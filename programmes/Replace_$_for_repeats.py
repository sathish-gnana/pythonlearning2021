'''
Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$$'
'''

#string_val = input ("Please input your sting:")
#print("entered text is:",string_val)

rever_val = input ("Please input your sting:")
string_val = rever_val[::-1]
#print(string_val)

for string_index in string_val:
    #print(string_index)
    lowest = string_val.index(string_index)
    highest = string_val.rindex(string_index)
    count_seen = string_val.count(string_index)
    #if lowest == highest:
    #    print("no repitions of string: ",string_index)
    if lowest != highest:
        #print(count_seen," repitions of ",string_index, "seen in the string")
        #print("index: ",highest)
        string_val = string_val.replace(string_index,"$",count_seen-1)


print(string_val[::-1])

'''
    if "$" not in string_index:
        repitions_seen = string_val.count(string_index)
        if repitions_seen > 1:
            print("duplicate found:", string_index)
            count = 0
            while (count < repitions_seen):
                count += 1
                lowest =string_val.index(string_index)
                highest = string_val.rindex(string_index)
                if lowest == highest:
                    print ("no repitions")
'''
