# check given string is paliandrome or not?
#space - O(2n) ==> O(n) extra space
# Time- O(2n)
# recursive method
str2= ''
str1= 'manu'
s=[]
if (len(str1)>0):
	for i in range(len(str1)):
		s.append(str1[i])

while(len(s)>0):
	str2=str2+s.pop(-1)

if (str1 == str2):
	print("string-",str1, "is a paliandrome")
else:
	print("Given string is not a paliandrome-",str1, str2)	





# Leet Code Solution
#class Solution(object):
 #   def isPalindrome(self, x):
 #       return str(x) == str(x)[::-1]	
