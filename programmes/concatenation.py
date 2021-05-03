'''
#Write a Python program to remove the nth index character from a nonempty string
'''

while True:
    string_val = list(input("enter a string:"))
    index = int(input("enter the index to remove:"))

    new_string = ""

    #print(len(string_val))
    for items in range(0,len(string_val)-1):
        if items != index:
            #print(string_val[items])
            new_string = ''.join([new_string, string_val[items]])
        else:
            continue

        print("new string is forming:", new_string)

    print("final new string", new_string)

    exit (0)

exit(1)



'''
 #newstring = string_val
    #print(string_val[0],string_val[1],string_val[2],string_val[3],string_val[4])
    #string_val = "hellol"
    #index = 4
'''
