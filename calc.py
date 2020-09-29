
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

expression = "" 
def press(num): 
	global expression 

	expression = expression + str(num) 

	equation.set(expression) 



def equalpress(): 
	try: 
		global expression 
		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 
	except: 

		equation.set(" error ") 
		expression = ""
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# background colour of GUI window 
	gui.configure(background="white") 

	# title of GUI window 
	gui.title("Simple Calculator") 

	#  configuration of GUI window 
	gui.geometry("270x150") 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70) 

	equation.set('enter your expression') 

