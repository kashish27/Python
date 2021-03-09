#Python program to return second most frequent character in the input string

string =input("Enter the string:")  #Input the string
ascii_array=[0]*256  #Create a list which maintain the count of each alphabet

for i in range(len(string)):
	m=ord(string[i])  #ord() gives the decimal(ascii value) corresponding to each character 
	ascii_array[m]=ascii_array[m]+1  #incrementing the count 

first=0   #Keep First max character                      
second=0  #Keep Second max character
for i in range(len(ascii_array)):
	if(ascii_array[i]>ascii_array[first]):   #If current element is smaller than first max we need to update both first max and second max 
		second=first
		first=i
	elif(ascii_array[i]>ascii_array[second] and ascii_array[i]<ascii_array[first]): #If current element is in between first max and second max then update second max
		second=i
second_max_char=chr(second)

if second_max_char!="\0":
	print ("Second most frequent character in the String:"+second_max_char)                 
else:
	print("No second most frequent character")
	
	
#Time Complexity: O(n)
#Space Complexity: O(1) —Using fixed space (Hash array) irrespective of input string size.

'''
NOTE-->
If more than one characters have the same count and then the first character
with maximum count in input string is to be considered maximum.
'''
