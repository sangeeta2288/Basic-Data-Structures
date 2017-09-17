
s_items = []

def stack_isEmpty():
	if len(s_items)== 0:
		print("Yes, Stack is empty")
	else:
		print("Stack has", len(s_items), "elements in it.")

def stack_view():
	for n in range(len(s_items)):
		print(s_items[n])
def stack_push():
	item = (input(print("Enter the element that you would like to push to the stack: ")))
	s_items.append(item)
def stack_pop():
	p_item=s_items.pop(-1)
	print("You just popped the element: ", p_item)


while True:
	print("***** Python Implementation of Stacks *****")
	print("1.Check stack is Empty? ")
	print("2.View stack elements ")
	print("3.Push on to the stack ")
	print("4.Pop from the stack ")
	print("5.Quit the application")

	choice=int(input("Enter your choice: "))
	print("")

	if (choice == 1):
		stack_isEmpty()
	elif (choice == 2):
		stack_view()
	elif (choice == 3):
		stack_push()
	elif (choice == 4):
		stack_pop()
	elif (choice == 5):
		quit()

	 
