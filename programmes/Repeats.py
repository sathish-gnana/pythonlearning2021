''''
#Write a Python program to find the first repeated character in a given string
'''

string_val = "world hello"
#print(len(string_val))
for index in range(0,len(string_val)):
    #print(string_val[index])
    count_repitions = int(string_val.count(string_val[index]))
    if count_repitions > 1:
        print("first repeated character in your string is",string_val[index])
        break

exit (0)