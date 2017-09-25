# Eg: Convert given string into an acronym
# input:Java Virtual Machine=> o/p:JVM
# Time: O(2n) bcoz of list entry + looping through words===> O(n) where n is no of words
# Space: O(n) extra space bcoz of the list
class StrFunction():
        def __init__(self):
                #print("Hello")

        def strOperation(self,str):
                str1=str.upper()
                print(str1)

                #str=>List
                list1=str1.split()
                for word in list1:
                        print(word[0],end="")

                #get 1st letter of the word and eleminate new line
s=StrFunction()

while True:
        choice = input("Want to access Acronym Generator? (y/n): ")
        choice=choice.lower()
        if(choice== "y"):
                str=input("Enter the long string")
                s.strOperation(str)
        else:
                quit()
