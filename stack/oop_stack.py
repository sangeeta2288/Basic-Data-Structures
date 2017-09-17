class Stack:
	def __init__(self):
		self.a_stack_items = []

	def stack_isEmpty(self):
		return self.a_stack_items== []

	def stack_view(self):
		for n in range(len(self.a_stack_items)):
			print(self.a_stack_items[n])

	def stack_push(self):
		item=int(input(print("Enter the item you want to add to the stack: ")))
		self.a_stack_items.append(item)

	def stack_pop(self):
		item=self.a_stack_items.pop(-1)
		print("You just popped", item , "from the stack")

s = Stack()

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
                s.stack_isEmpty()
        elif (choice == 2):
                s.stack_view()
        elif (choice == 3):
                s.stack_push()
        elif (choice == 4):
                s.stack_pop()
        elif (choice == 5):
                quit()

