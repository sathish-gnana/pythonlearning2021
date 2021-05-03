from collections import Counter
import time

#https://www.hackerrank.com/challenges/collections-counter/problem

profit = 0
N = 0
shoe_size_cnt = Counter()

def CollectData():

    global shoe_size_cnt
    #X = int(input ("Input number of shoes:"))
    X = int(input ())
    if not (0 < X and X < 1000):
     #   print("Not a valid shoe numbers")
        exit(0)

    #input_shoe_size = input ("Input list of all the shoes sizes:") # range between 2 and 20
    input_shoe_size = input () # range between 2 and 20
    #print("input shoe size :", input_shoe_size)
    shoe_size_list = input_shoe_size.split(" ")
    #print("shoe size list:", shoe_size_list)

    '''
    if shoe_size_list.count == X:
        print("shoe list is valid")
    else:
        print("shoe list is Invalid")
        exit(0)
    '''
    for itr in shoe_size_list:
    #    print(type(itr))
    #    print (type(int(itr)))
        if 2 < int(itr) and int(itr) < 20:
            shoe_size_cnt[itr] += 1
        else:
            dummy = 0
            #print("invalid shoe size: ", itr)

    #N = int(input ("Input number of customers:"))
    global N
    N = int(input ())
    if (0 < N and N < 1000):
     #   print("Invalid Number of customers")

    #print(shoe_size_cnt)
        CollectCustomer_purchase_data()

def CollectCustomer_purchase_data():
    #for line in input()
    #print("\nIn CollectCustomer_purchase_data()")
    count =0
    global N
    global profit
    while N > 0:
        input_customer_purchase = input()
        N -= 1
      #  print ("Current N value", N)
        #count += 1
        shoesize_purchase = list(input_customer_purchase.split(" "))
        shoesize = int(shoesize_purchase[0])
        purchase = int(shoesize_purchase[1])
     #   print("shoesize: ",shoesize, "purchase: ",purchase,"profit: ",profit)
        if check_shoesize(shoesize):
            profit = profit + purchase
            remove_shoesize(shoesize)  #remove the keypair after customer shoe purchase
        #else:
        #   print("not present in container:", shoesize)

    print(profit)
    exit(0)

def remove_shoesize(shoesize):
    #print(shoe_size_cnt)
    deduct_in_stock={str(shoesize):1}
    shoe_size_cnt.subtract(deduct_in_stock)
    #print(shoe_size_cnt)
    #time.sleep(3)

def check_shoesize(shoesize):
    #print("Check function ",list(shoe_size_cnt.elements()) )
    full_elements = list(shoe_size_cnt.elements())
    #print(type(full_elements))
    #print(type(shoesize))
    #print("count:", full_elements.count(str(shoesize)))
    if (full_elements.count(str(shoesize))):
        return True
    else:
        return False
#main
if __name__ == '__main__':
    CollectData()
    CollectCustomer_purchase_data()
