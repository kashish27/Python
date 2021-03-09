#Python program to return the maximum occuring character in the input string


string =input("Enter the string:") #Input the string

ascii_array=[0]*256 #Create a list which maintain the count of each alphabet


for i in range(len(string)):
	m=ord(string[i]) #ord() gives the decimal(ascii value) corresponding to each character 
   
	ascii_array[m]=ascii_array[m]+1  #incrementing the count
 

max_char=chr(ascii_array.index(max(ascii_array)))
#max return the first max value of list and index() will given index number
#chr() gives corresponding character value to decimel(ascii value) 
print ("Maximum occuring character in the String:"+max_char)                 

#Time Complexity: O(n)
#Space Complexity: O(1) —Using fixed space (Hash array) irrespective of input string size.

'''
NOTE-->
If more than one characters have the same count and then the first character
with maximum count in input string is to be considered maximum.
'''
