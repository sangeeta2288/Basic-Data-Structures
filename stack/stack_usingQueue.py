class stack :
	def __init__(self):
		self.queue = []
	def push(self, item):
		self.queue.append(item)
	def pop(self):
		temp_queue = []
		while (len(self.queue) > 1):
                        temp_queue.append(self.queue.pop(0))
		p_item= self.queue.pop(0)
		self.queue = temp_queue
		print("popped: ",p_item)
	def view(self):
		for i in range (len(self.queue)):
			print(self.queue[i])
	def peek(self):
		print(self.queue[len(self.queue)-1])
			 
		
s = stack()
while True:
	print(" **** Implementing Stack using Queue data structure **** ")
	print("1. Push")
	print("2. pop")
	print("3. View")
	print("4. Exit")
	print("5. Peek")
	choice = int(input(print("Enter ur choice: ")))

	if(choice == 1):
		x = int(input(print("Enter item you want to push")))
		s.push(x)
	elif(choice == 2):
		s.pop()
	elif(choice == 3):
		s.view()
	elif(choice == 4):
		quit()
	elif(choice == 5):
		s.peek()
