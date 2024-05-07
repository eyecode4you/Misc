#num_process.py
""" 	Take a list of numbers from user input using the 
	input() function and calculate the sum.
	The input() function returns a string so we will separate the
	individual numbers before processing them. """

#The input function by itself returns a string!
line = input("Enter a line of numbers - separate them with spaces!: ")

#Create a list containing each character in input string
str_list = line.split()
print("\nList Contents: ", str_list, "\n\n") #display contents of list

total = 0 #Used for sum calculation (We're not using sum() function!)

try:
    for substr in str_list: #for each item in list
		
#Typecast (Data type conversion) list element to a float for processing
        total += float(substr)
        
    print("The sum is:", total) #Display sum
    
#If incorrect data type is entered, display error message
except ValueError: 
    print(substr, "is not a number.")
