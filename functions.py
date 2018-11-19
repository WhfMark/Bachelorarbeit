# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:39:08 2018

@author: hongf
"""

import random       #imput the random library 
n = random.randrange(8)  # here n is the limitation of number of the processes
m = random.randrange(50) # here m is the limitation of the task

# we give n processes in random, and in every process we give n scheduling in random

originalLists=[]

for i in range (n):
    listOfRandomNumbers = []
    r = random.randrange (10,20) 
    # here r is the limitation of the number of the scheduling in process
   
    for j in range (r):
        listOfRandomNumbers.append(random.randrange(m))
        #append is a function in python, which is uesd to append elements in an empty sub list 
        
    originalLists.append(listOfRandomNumbers)
        #append is a function in python, which is uesd to append sub lists in an empty list
#originalLists= [[11, 9, 17, 24, 5, 21, 6, 31, 36, 7, 21, 11, 1, 27], [13, 4, 25, 18, 24, 30, 5, 1, 11, 10, 27], [23, 35, 37, 21, 33, 6, 5, 17, 5, 4, 36, 20, 34, 21, 6, 11]]
print("Original Lists: ") # a list of lists are generated
print(originalLists)

#Reduce Function, in oder to reduce the list of lists
def list_Reduce(lst):
    listOfLists = lst
    
    # we check whether the sub list is empty, if empty, delete it
    while [] in listOfLists:
        listOfLists.remove([])
    
    # pattern M0
    for i in range (len(listOfLists)):
        # we use 2 for-loops to visit every element in list of lists
        for j in range(len(listOfLists[i])-1,0,-1): 
            # in this loop we visit the elemens from the end to beginnig, 
            # because the big of lists is not stable after reduce operation.
           
            if  listOfLists[i][j]==listOfLists[i][j-1] :
                del listOfLists[i][j]                   
                j = j-3    #this is required in standardization with 3 index back
            else:
                pass
            #If the processes do not need reduce,then keep intact.
    
    # pattern M1        
    for i in range (len(listOfLists)):  
    # we use 2 for-loops to visit every element in list of lists 
        for j in range(len(listOfLists[i])-1,1,-1): 
        # in this loop we visit the elemens from the end to second element not to beginning, 
        # because the big of lists is not stable after reduce operation
        
            if  listOfLists[i][j-2] < listOfLists[i][j-1] \
            and listOfLists[i][j-1] < listOfLists[i][j]  :
                del listOfLists[i][j-1]
                j = j-3   #this is required in standardization with 3 index back
            else:
                pass
    
    # pattern M2  
    for i in range (len(listOfLists)):  
    # we use 2 for-loops to visit every element in list of lists 
        for j in range(len(listOfLists[i])-1,1,-1): 
        # in this loop we visit the elemens from the end to second element not to beginning, 
        # because the big of lists is not stable after reduce operation       
            if listOfLists[i][j-2] > listOfLists[i][j-1] \
            and listOfLists[i][j-1] > listOfLists[i][j] :
                del listOfLists[i][j-1]            
                j = j-3   #this is required in standardization with 3 index back
            else:
                pass
            #If the processes do not need reduce,then keep intact.  

    # pattern M3
    for i in range (len(listOfLists)):      
    # we use 2 for-loops to visit every element in list of lists
        for j in range(len(listOfLists[i])-1,2,-1): 
        # in this loop we visit the elemens from the end to third element not to beginning, 
        # because the big of lists is not stable after reduce operation           
            if listOfLists[i][j-3] > listOfLists[i][j-2] \
            and listOfLists[i][j-1] > listOfLists[i][j]  \
            and listOfLists[i][j-2] < listOfLists[i][j-1]\
            and listOfLists[i][j-3] >= listOfLists[i][j-1] \
            and listOfLists[i][j-2] >= listOfLists[i][j] :
                del listOfLists[i][j-1] 
                del listOfLists[i][j-2]
                j = j - 3  #this is required in standardization with 3 index back
            else:
                pass #If the processes do not need reduce,then keep intact.              
    # pattern M4 
    for i in range (len(listOfLists)):     
    # we use 2 for-loops to visit every element in list of lists
        for j in range(len(listOfLists[i])-1,2,-1): 
        # in this loop we visit the elemens from the end to third element not to beginning, 
        # because the big of lists is not stable after reduce operation   
            if listOfLists[i][j-3] < listOfLists[i][j-2] \
            and listOfLists[i][j-1] < listOfLists[i][j]  \
            and listOfLists[i][j-2] > listOfLists[i][j-1]\
            and listOfLists[i][j-3] <= listOfLists[i][j-1]\
            and listOfLists[i][j-2] <= listOfLists[i][j] :
                del listOfLists[i][j-1] 
                del listOfLists[i][j-2]
                j = j - 3  #this is required in standardization with 3 index back
            else :
                pass #If the processes do not need reduce,then keep intact.     
    return listOfLists
reduceList=list_Reduce(originalLists)
print("Reduced Lists:")
print(reduceList)

x=0
def list_Standard_1(lst,x):
    listOfLists1 = lst
    k_0 =x
    # we collect every first element of sub list and put them in a new list list1
    list1 = [item[0] for item in listOfLists1] 
    # now in list1, we have all first elements of sub lists of listOfLists1 
    # then we give sum function to calculate the summation.
    k_0 = sum(list1)

    #in this for-loop, we visit every element in whole list
    for x in range (len(listOfLists1)): 
        if len(listOfLists1[x]) < 2:
            listOfLists1[x] = listOfLists1[x]
        # we compare the first element with the sceond one,
        # in order to check that, if there is a start-peak in this sub list
        elif len(listOfLists1[x]) >= 2 and listOfLists1[x][0] > listOfLists1[x][1] :
        # if there is a start-peak, and if the length of the list 
        # is larger than 2 or same as 2, then we delete this start-peak.
            del listOfLists1[x][0]
        # In ohterweise, we just do not do any change.
        else:
            pass
    return (listOfLists1,k_0)

def list_Standard_2(lst,x):
    listOfLists1 = lst
    k_w =x
    listOfLists2 = listOfLists1 
    # we collect every last element of sub list and put them in a new list list2
    list2 = [item[-1] for item in listOfLists2]

    # now in list1, we have all last elements of sub lists of listOfLists1 
    # then we give sum function to calculate the summation.
    k_w = sum(list2)
    
    #in this for-loop, we visit every element in whole list
    for y in range (len(listOfLists2)):    
        if len(listOfLists2[y]) < 2:
            listOfLists2[y] = listOfLists2[y]   
        # we compare the last element with the last sceond one,
        # in order to check that, if there is an end-peak in this sub list
        elif len(listOfLists1[y]) >= 2 and listOfLists2[y][-1] > listOfLists2[y][-2] :
        # if there is an end-peak, and if the length of the list 
        # is larger than 1, then we delete this end-peak.
            del listOfLists2[y][-1]
        # In ohterweise, we just do not do any change.
        else:
            pass
    return (listOfLists2,k_w)
#this function is the fourth standardization step
def list_Standard_3(lst,x):
    listOfLists2 = lst
    k_a =x
    listOfLists3 = [] # we give an empty list
    list3 = []    # we give this empty list to add every one element of all one-element lists

    #in this for-loop, we visit every element in whole list
    for z in range (len(listOfLists2)):
        # this if sentence ensures that, if the sub list is one-element list
        if len(listOfLists2[z]) > 1:    
        # if it is not one-element list, we add it to listOfLists3
            listOfLists3.append(listOfLists2[z])
        else:
        # if it is an one-element list, we send its element to list3
            list3 +=listOfLists2[z]
        # now in list3, we have all elements of one-element sub lists of listOfLists1 
        # we give sum function to calculate the summation
        k_a = sum(list3)
    
    return (listOfLists3,k_a)
K_0 =list_Standard_1(reduceList,x)[1]
K_W =list_Standard_2(reduceList,x)[1]
K_A =list_Standard_3(reduceList,x)[1]
print("K_0:",K_0)
print("K_W:",K_W)
print("K_A:",K_A)
print("Standard Lists:")
print(list_Standard_3(reduceList,x)[0])

#  the function end_index is uesed to confirm the unique
#  and of the right most golobalvally index if there are many global valley.
#  At last, the program collects valley index for each sub process in a list.    
def end_index(orglist):
    lst = orglist # the input is the standard process

    lst2 =[] # lst2 is used to collect every global valley index for each sub process.
    for x in range(len(lst)):
        ends = 0
        for i in range(len(lst[x])-1):
            
            lst1 =[] # lst1 is uesed to collect all same gobal valleys for 1 sub process
            if lst[x][i] == min(lst[x]): # if the element is the minimal, 
                j = i                  # then j is one of the global valleys for the sub process.
                lst1.append(j) # the program put all global vallys for sub process in one list 
                ends=max(lst1)  # Then it uses max function to find the rightmost global valley.
        lst2.append(ends)
    return lst2          # the function return the list of the vally index for each sub process.      


# Import the heap functions from python library 
from heapq import heappush, heappop, heapify 

# heappop - pop and return the smallest element from heap 
# heappush - push the value item onto the heap, maintaining 
#			 heap invarient 
# heapify - transform list into heap, in place, in linear time 
# A class for Min Heap 
class MinHeap: 
		# Constructor to initialize a heap 
	def __init__(self): 
		self.heap = [] 

	def parent(self, i): 
		return (i-1)/2
	
	# Inserts a new key 'k' 
	def insertKey(self, k): 
		heappush(self.heap, k)		 

	# Decrease value of key at index 'i' to new_val 
	# It is assumed that new_val is smaller than heap[i] 
	def decreaseKey(self, i, new_val): 
		self.heap[i] = new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
			# Swap heap[i] with heap[parent(i)] 
			self.heap[i] , self.heap[self.parent(i)] = ( 
			self.heap[self.parent(i)], self.heap[i]) 
			
	# Method to remove minium element from min heap 
	def extractMin(self): 
		return heappop(self.heap) 
    
	# This functon deletes key at index i. It first reduces 
	# value to minus infinite and then calls extractMin() 
	def deleteKey(self, i): 
		self.decreaseKey(i, float("-inf")) 
		self.extractMin() 

	# Get the minimum element from the heap 
	def getMin(self): 
		return self.heap[0] 

listStandard = list_Standard_3(originalLists,x)[0]

# this is the function of lef_scan_algo algorithm
def left_scan_algo(orglist):
    s_0 = m_0 =0
    list1 = orglist
    # colect every first element of sub lists and put them in one list
    list3 = [item[0] for item in list1] 

    # the summation of all first elements for each sub list
    s_0 = m_0 =sum(list3)
    
    # the list collcets tuples
    list4 = []
    for i in range(len(list1)):
        list4.append((list1[i][1]-list1[i][0],i))
    
    # we set a minheap search tree     
    heapObj = MinHeap()
    # give the end_index function to the standard process, in order to find the index valley
    ends = end_index(orglist)   
    lst = list4
    lst1 =list1
    M_0 = m_0
    S_0 = s_0
    # we insert the tuple in the search tree
    for x in lst:
        heapObj.insertKey(tuple(x))
    # if the tree is empty, then return the M and terminate
    while (heapObj.heap != []):
        j = heapObj.getMin()[1]
        M_0 = max(M_0, S_0 + heapObj.getMin()[0])
        S_0 = S_0 + (lst1[j][2]-lst1[j][0])        
        i_I = 1
        i_ends = ends[j]
        heapObj.extractMin()
        # if the current index+2 smaller than the valley index, 
        # then insert the new tuple in search tree
        while (i_I + 2 < i_ends+1): 
            heapObj.insertKey(tuple([lst1[j][i_I+2]-lst1[j][i_I+1],j]))
            i_I = i_I + 2
            heapObj.extractMin()
        else:
            pass
    return M_0
M0 = left_scan_algo(listStandard)
print("M_0:",M0)

listReverse = list_Standard_3(originalLists,x)[0]
# Reeverse function to reverse the list
def list_Reverse(lst):
    lstReverse = lst
# we set a reverse for the whole list
    for x in lstReverse:
        # reverse function 
        x.reverse()
    lstReverse.reverse()
    return lstReverse
print("Reverse List:",list_Reverse(listReverse))

# this is the function of right_scan_algo algorithm
def right_scan_algo(orglist):
    s_0 = m_0 =0
    list1 = orglist
    # colect every first element of sub lists and put them in one list
    list3 = [item[0] for item in list1] 

    # the summation of all first elements for each sub list
    s_0 = m_0 =sum(list3)
    
    # the list collcets tuples
    list4 = []
    for i in range(len(list1)):
        list4.append((list1[i][1]-list1[i][0],i))

    # we set a minheap search tree     
    heapObj = MinHeap()
    # give the end_index function to the standard process, in order to find the index valley
    ends = end_index(orglist)
    
    lst = list4
    lst1 =list1
    M_0 = m_0
    S_0 = s_0
    # we insert the tuple in the search tree
    for x in lst:
        heapObj.insertKey(tuple(x))
    # if the tree is empty, then return the M and terminate    
    while (heapObj.heap != []):
        j = heapObj.getMin()[1]
        M_0 = max(M_0, S_0 + heapObj.getMin()[0])
        S_0 = S_0 + (lst1[j][2]-lst1[j][0])        
        i_I = 1
        i_ends = ends[j]       
        heapObj.extractMin()
        # if the current index+2 smaller than the valley index, 
        # then insert the new tuple in search tree
        while (i_I + 2 < i_ends+1):
            heapObj.insertKey(tuple([lst1[j][i_I+2]-lst1[j][i_I+1],j]))
            i_I = i_I + 2
            heapObj.extractMin()
        else:
            pass
    return M_0
M1=right_scan_algo(listReverse)
print("M_1:",M1)

# the max function gives the spmin of the whole process
space_usage = max(M0+K_A, M1+K_A, K_0, K_W)
print("Spmin:",space_usage)

    
    



    
