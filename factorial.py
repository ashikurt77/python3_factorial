show_info = False #Controls the display of multiplication

def hint(): #Shows hint and Detailed View Commands
	if show_info :
		print('Insert an integer number.\nTo turn off detailed view, input "no"')
	else:
		print('Insert an integer number.\nTo turn on detailed view, input "yes" ')

while True :
	
	hint() #displays hint
	inp = input() #takes input from user
	
	if inp == 'done': #terminal close statement
		print("\nHave a nice day!")
		break
		
	elif inp == "yes": #toggle on Detailed View
		show_info = True
		print("\nDetailed View turned on\n")
	
	elif inp == "no": #toggle off Detailed View
		show_info = False
		print("\nDetailed View turned off\n")
	elif inp == "creator":
		print("\nMade By : Ashiqur Rahman Tusher\nEmail : ashikurt77@gmail.com\nDate : 11 July, 2020\n")
	else:
		try: #converting input str to int
			ini_num = int(inp)
			num = abs(ini_num) #taking absolute value
		except:
			print("\nplease put a number!\n")
			continue
			
		def compensate_neg(): #adjusting negative factorial by determinig if the input is positive or negative
			if ini_num <0:
				return "-"
			else:
				return ""
			
		factorial =1 #setting initial value of factorial
		
		for i in range(num,1,-2): #computing factorial
		
			counter = i-1
			factorial = factorial * (counter*i)
			
			if show_info: #detailed view portion
				print(f"\n{i} * {counter}")
			
		print(f"\nFactorial of {ini_num} is {compensate_neg()}{factorial}\nTo close the terminal, input 'done'\n")		