"""RockPaperScissors.py Play rock paper scissors against your computer!
   EyeCode4You - Do whatever you like with this file!"""
import sys
from random import randint

def usr_option(options):
	""" Display and get option index from user """
	print("RockPaperScissors.py\n---------------------\nOptions are: ", options)
	
	usr_choice = int(input("Choose an option: "))
	assert usr_choice >= 1 and usr_choice <= 4 #usr input between 1 & 4	
	usr_choice -= 1 #-1 for use with options tuple
	return usr_choice #return index to access
	
def results(cpu_choice_indx, usr_choice_indx, w, l, d):
	""" Calculate & Display Results"""
	res1, res2, res3 = "\nCPU WINS!", "\nYOU WIN!", "\nResult: DRAW"
	
	#0 = Scissors, 1 = Rock, 2 = Paper
	if(cpu_choice_indx == 0 and usr_choice_indx == 2):
		l += 1
		print(res1)
	elif(cpu_choice_indx == 1 and usr_choice_indx == 0):
		l += 1
		print(res1)
	elif(cpu_choice_indx == 2 and usr_choice_indx == 1):
		l += 1
		print(res1)
	elif(cpu_choice_indx == usr_choice_indx): #Draw
		d += 1
		print(res3)
	else:
		w += 1
		print(res2)
	return w, l, d

def main():
	""" Generate option for CPU, user, & display result """
	w, l, d = 0, 0, 0 #Vars for wins, losses, & draws
	while 1:
		options = ('1:Scissors', '2:Rock', '3:Paper', '4:Exit')
		cpu_choice_indx = randint(0, 2) #generate random index
		cpu_choice = options[cpu_choice_indx] #str based on generated index
		
		#Get user input and error check
		while 1:
			try:
				usr_choice_indx = usr_option(options)
				break #exit loop
			except:
				print("\n****Please enter a number between 1 and 4!****\n")
				
		usr_choice = options[usr_choice_indx] #str based on generated tuple index	
		if usr_choice == options[3]:
			sys.exit()
			
		#Display Results
		print("\nCPU chose", cpu_choice)
		print("You chose", usr_choice)	
		w, l, d = results(cpu_choice_indx, usr_choice_indx, w, l, d)
		print("Results -> Wins: {} Losses: {} Draws: {}".format(w, l, d))
		print("\n\n\n")
	
if __name__ == "__main__":
	main()
