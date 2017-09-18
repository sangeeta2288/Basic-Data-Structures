# sort the given stack using only one more stack, no other data structure
# Recursive methos
# Time -  and Space - 

s1 =[1,6,5,3,2,9]
s1 = [6,5,4,1,2,3]
stack1 = []
#stack2 = []

def stack_sort():
	stack2= []	
	while (len(stack1)!= 0):
		temp = stack1.pop(-1)
		if(len(stack2)==0):
			stack2.append(temp)
			temp = stack1.pop(-1)
		stack2_len = len(stack2)
		i = 0
		while(i < stack2_len):
			temp2= stack2.pop(-1)
			if(temp<temp2):
				stack1.append(temp2)
			else:
				stack2.append(temp2)
				stack2.append(temp)
				break
			i = i + 1
			if(not len(stack2)):
				stack2.append(temp)
			print(stack2)
			#break
		

	if(len(stack1)==0):
		print(stack2)
				

for i in range (len(s1)):
	stack1.append(s1[i])
print(stack1)


choice=input(print("sort the stack? y/n: "))
#choice = choice.split[0].lowercase()
if (choice == 'y'):
	stack_sort()
else:
	quit()
