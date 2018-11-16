# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:54:42 2018

@author: hongf
"""

# import the main function of optimizing programm

import random
# creat the process of sub processes with n sub processes and r scheduling in each sub process
def createList(n,r):
    
    m = 100
    originalLists=[]
    for i in range (n):
        listOfRandomNumbers = []
         
    # here r is the limitation of the number of the scheduling in process
   
        for j in range (r):
            listOfRandomNumbers.append(random.randrange(m))
            #append is a function in python, which is uesd to append elements in an empty sub list 
        
        originalLists.append(listOfRandomNumbers)
            #append is a function in python, which is uesd to append sub lists in an empty list
    return originalLists

# import the optimizing implementation 
import functions
# running of the whole optimizing prgramm
# n is the amount of sub processes and r is the amount of scheduling in each sub process        
def testSpecificValue(n,r):    
    testList=createList(n,r)
    
    reduceList = list_Reduce(testList)
    listStandard =list_Standard_3(list_Standard_2( list_Standard_1(reduceList,0)[0],0)[0],0)[0]
    list_ReverseList = list_Reverse(listStandard)
    tree = MinHeap()
    endindex = end_index(listStandard)
    m_0=left_scan_algo(listStandard)
    m_1=right_scan_algo(list_ReverseList)
    
    return 0

# calculate the running time and show it directly
def runTestTime(n,r):
    # import time calculate libray
    from timeit import timeit
    repetitions=1

    t1=timeit(lambda:testSpecificValue(n,r),number=repetitions)
    print("Runtime",t1/repetitions)
runTestTime(10000,10000)    

# import library numerical mathematics             
import matplotlib.pyplot as plt
# import library, support for large, multi-dimensional arrays and matrices,
import numpy as np
# we test the running time for the whole programm and make it as diagram 
def runTestN(n):
    # import time calculate libray
    from timeit import timeit
    repetitions=1
    step=500
    # conforms the big of the x and y
    xValues=np.zeros(int(n/step))
    yValues=np.zeros(int(n/step))
    k=0
    
    for i in range(100,n,step):
        if i%2==0:
            print("Percent done:",100*(k/(n/step)))
        # x is range of r*n
        r=1 * i
        
        xValues[k]=r*n
        # y is range of running time
        t1=timeit(lambda:testSpecificValue(i,r),number=repetitions)
        yValues[k]=t1/repetitions
        k=k+1
    plt.plot(xValues,yValues,marker='+',linestyle='-',color=(1,0,0))
    plt.savefig("Running Time", dpi=300)
    plt.show()
    
runTestN(10000) #here we test the program with the input from 100*100 to 100000*100000.
  