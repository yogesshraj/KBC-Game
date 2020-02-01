question_list = [
	"How many continents are there?",  			
	"What is the capital of India?",			
	"What do we learn in Navgurukul?"	
]

options_list = [
	["1.Four", "1.Chandigarh", "1.Software Engineering" ],
	
	["2.Nine", "2.Bhopal", "2.Counseling" ],
	
	["3.seven","3.chennai", "3.Tourism" ],

	["4.eight\n", "4.Delhi\n", "4.Agriculture\n"]
]

solution_list = [3, 4, 1]
a=0
b=0
for q in question_list:
	print (q)
	for o in options_list:
		print (o[a])
	a+=1
	l=int(input("ENTER THE ANSWER\n"))
	if l==solution_list[b]:
		print ("u r right\n ")
	else:
		print ("u r wrong\n")
		break
	b+=1
