
class Queue():
	def __init__(self):
		self.queue = []
	def view(self):
		for i in range(len(self.queue)):
			print(self.queue[i])
	def enque(self):
		item=input(print("Enter item/elements into the queue: "))
		self.queue.append(item)
	def deque(self):
		item=self.queue.pop(0)
		print("dequed element is: ",item)

myQ=Queue()

while True:
	print("***** Queue Implementation using list *****")
	print("1. View	2.Enque 3. Deque 4. Quit ")
	choice = int(input(print("Enter ur choice: ")))
	if (choice==1):
		myQ.view()
	elif(choice == 2):
		myQ.enque()
	elif(choice == 3):
		myQ.deque()
	elif(choice == 4):
		quit()
