from replit import clear
import art
def add(n1,n2):
	return n1+n2

def subtract(n1,n2):
	return n1-n2

def multiply(n1,n2):
	return n1*n2

def divide(n1,n2):
	if n2 == 0:
		return "Zero Error!"
	return n1/n2

operations = {}
operations = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide
}
def calculator():
	print(art.logo)
	n1 = int(input("What's the first number. "))
	for operation in operations:
		print(operation)

	should_continue = True

	while should_continue:
		operator = input("Pick an operation from the line above. ")
		n2 = int(input("What's the next number. "))
		function = operations[operator] 
		answer = function(n1,n2)
		print(f"{n1} {operator} {n2} = {function(n1,n2)}")

		continue_or_no = input(f"Do you want to contiue with {answer}. Type 'y' or 'n' to exit. ").lower()
		if continue_or_no == 'y':
			n1 = answer
		elif continue_or_no == 'n':
			should_continue = False
			clear()
calculator()
		

	
	
		


