
import math
lst1 = [1, 3, 6, 2, -1, 2, 8, -2, 9,-1,-3,0,0,0, 2]
lst2 =[1, 3, 6, 2, -1, 2, 8,-2, 9]



def main(myList):
    #checks to make sure the lenght of the list is at least 3
    if len(myList)<3:
        print("please input a list with more than 3 numbers:")
    #checks all posible sollutions Big O n^3
    for i in range(len(myList) - 2):
        for j in range(i+1,len(myList)-1) :
            for k in range(j+1, len(myList)):
                #if equal to the target display result
                if myList[i] +myList[j]+myList[k] ==0:
                    print([myList[i],myList[j],myList[k]])




main(lst1)
main(lst2)

