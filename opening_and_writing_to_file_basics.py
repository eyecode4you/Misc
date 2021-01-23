#opening_and_writing_to_file_basics.py - Introduction to opening & writing to files in Python
#EyeCode4You - Do what you like with this file

from random import randint #We will use this to get random integers

def main():
	##### SECTION 1 Writing to a file example #####
	""" Using: variable = open("filename", "mode") """
	""" Common Modes: r = reading, r+ = read & write, w = writing, a = appending """
	
	""" The next line will open a file called out_numbers.txt in write 
	mode (sending data). When using w, if the file doesn't exist it is created.
	If the file does exist it is OVERWRITTEN! Keep this in mind.
	"""
	#open() returns a FILE OBJECT. Here outFile is our FILE OBJECT, so we access attributes and methods by using: outFile.methodName() or outFile.attributeName
	outFile = open("out_numbers.txt", "w") #This file will be located in the SAME folder as the python program
	
	for i in range(10):#loop ten times
		x = randint(0, 10)#Assign x the value of a random integer between 0 - 10 inclusive, these numbers will change everytime the program is run
		outFile.write(str(x) + "\n")#send x to out_numbers.txt - Remember to convert integers to a string before writing to file.
	
	outFile.close()#When you finish working with the file close it. 
	
	##### SECTION 2 File Object Attributes ######
	""" File Object Attributes 
	fileObject.name - Returns the filename 
	fileObject.mode - Returns the access mode (r, w, etc...)
	fileObject.closed - Can be used to check whether file is open or closed. closed = True, open = False
	"""
	#These are printed to the console NOT the file
	print(outFile.closed) #True (See line 18)
	print(outFile.name) #out_numbers.txt
	print(outFile.mode) #w - Notice that it returns w even though file has been closed
	
	##### SECTION 3 Appending to the outFile.txt file created previously #####
	""" if we wanted to write to the file again at this point of the program, we have to reopen it """
	#outFile = open("out_numbers.txt", "w") #This will OVERWRITE the out_numbers.txt
	""" if we wanted to ADD data to our file without overwriting we can use the a mode """
	
	outFile = open("out_numbers.txt", "a") #Again, if out-numbers.txt didn't exist, it would be created
	
	outFile.write("SECTION 3 START ") #The write function doesn't automatically add a trailing \n to the end of input.
	outFile.write("THIS WRITE WILL APPEAR ON SAME LINE" + "\n") #Since we added + "\n" the next write() will start on a new line.
	outFile.write("THIS WILL APPEAR ON A NEWLINE\n") #You can also add \n inside string instead of concatenating it (+ "\n")
	
	#These will be written to the file
	outFile.write("Is file closed? " + str(outFile.closed) + "\n")
	outFile.write("Name of the file: " + str(outFile.name) + "\n")
	outFile.write("Mode operating in: " + str(outFile.mode) + "\n")
	
	outFile.close()# Close our file
	print("END OF SECTION 3: Is file closed? ", outFile.closed)
	
if __name__ == "__main__":
	main()
