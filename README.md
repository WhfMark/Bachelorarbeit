# Bachelorarbeit
A Python-implementation of an efficient optimization space of independent parallel processes

In the bachelorarbeit, there are two programs. The first is the function for the optimizing implemenation, and another one is the test programs.
Test program contains two test function, one is runTestTime, for computing time; another is runTestN, for the diagram with different input.

If we want to get the computing time for the optimizing implementation.
We need command all operation sentences in optimizing implementation.

First we should command the all print function in the program and some sentences. 
'''import random       #imput the random library 
.....
print(originalLists)'''
from line 8 to line 29

'''reduceList=list_Reduce(originalLists) From line114 to line118
print("Reduced Lists:")
print(reduceList)
x=0'''
from line 114 to line 118


'''K_0 =list_Standard_1(reduceList,x)[1]
K_W =list_Standard_2(reduceList,x)[1]
K_A =list_Standard_3(reduceList,x)[1]
print("K_0:",K_0)
print("K_W:",K_W)
print("K_A:",K_A)
print("Standard Lists:")
print(list_Standard_3(reduceList,x)[0])'''
from line 189 to line 196

#listStandard = list_Standard_3(originalLists,x)[0]
line 261

'''M0 = left_scan_algo(listStandard)
print("M_0:",M0)'''
fron line 306 to line 307

#print("Reverse List:",list_Reverse(listReverse))
line 319

'''M1=right_scan_algo(listReverse)
print("M_1:",M1)
the max function gives the spmin of the whole process
space_usage = max(M0+K_A, M1+K_A, K_0, K_W)
print("Spmin:",space_usage)'''
from line 365 to line 370

In test program, if we need just get the computing time for the implementation, we should command the whole runTestN function.
If we want to get the diagram, we should command the whole runTestTime function.
