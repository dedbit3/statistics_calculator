#import numpy as np
import math
import numpy as np
import re
from package.ui import GUI

#input the data file into python 
inp = input("Input the data file name, enter the full path of the file: ");

#opening the file
x = open(file=inp, mode='r')
x = x.read()

#creating lists
col_a = []
col_b = []
int_a = []
int_b = []

#this is the regex pattern for matching numbers
pattern = r"\d+"
matches = re.findall(pattern, x)

#This splits matches into the 2 data collumns
for i, item in enumerate(matches):

    if i % 2 == 0:
        col_a.append(item)
    else:
        col_b.append(item)

#makes the collumns into intergers
for i in col_a:
    i = float(i)
    int_a.append(i)

for i in col_b:
    i = float(i)
    int_b.append(i)

#printing the results
print("This is col_a:")
print(int_a)

print("\nThis is col_b:")
print(int_b)

#this is gonna be the data inputted manually but like why? 
'''
x1 = float(input("\nInput the mean of the sample (X1): "))
x2 = float(input("Input the mean of the sample (X2): "))
s1 = float(input("Input the sample mean (S1): "))
s2 = float(input("Input the sample mean (S2): ")) 
n1 = float(input("Input the sample size (N1): "))
n2 = float(input("Input the sample size (N2): "))


#if the data is inputted these are the operations
pool_in = math.sqrt(((( (((n1 - 1) * (s1**2)) + (n2 - 1)) * (s2**2))) / n1 + n2 - 2) )                                                                                                      
t_in = (x1 - x2) / (pool_in * math.sqrt(1/n1 + 1/n2))
'''


#some calculations from the data
mean_a = np.mean(int_a)
std_a = np.std(int_a)
mean_b = np.mean(int_b)
std_b = np.std(int_b)

#this will calculate the T-value which needs to be compared with the table
#!!!!!!!!!THIS IS PROB THE PART THAT GOT MESSED UP AFTER I CHANGED THE VALUES TO LENGHT
#EITHER THE lenght values are messing it up or the int_a or the brackets on pool
#I feel like def the pool brackets tbh
pool = math.sqrt((( (((len(int_a) - 1) * (std_a**2)) + (len(int_b) - 1)) * (std_b**2))) / (len(int_a) + len(int_b) - 2) )
t = (mean_a - mean_b) / (pool * math.sqrt(1/len(int_a) + 1/len(int_b)))

print("\n T value: ")
print(t)

#this is a functionality for manual input but like why?
#print("\n T value (manual inputs): ")
#print(t_in)

#asks for the T value in the table so we can compare to significance level and determine if
#the hypothesis is null or not
table_val = float(input("\nInput the T-distribution table value: "))

if table_val < t:
    print("\nWe reject the null hypothesis")
else:
    print("\nWe FAILED to rejet the null hypothesis")

print("\nEND OF PROGRAM")
