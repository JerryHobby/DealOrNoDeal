#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
#
# DealOrNoDeal.py
#
#
# round 1: 6 turns - mark inplay false
# calculate offer/board
# deal or no deal
#
# round 2: 5 turns - mark inplay false
# calculate offer/show previous offers/board
# deal or no deal
#
# round 3: 4 turns - mark inplay false
# calculate offer/show previous offers/board
# deal or no deal
#
# round 4: 3 turns - mark inplay false
# calculate offer/show previous offers/board
# deal or no deal
#
# round 5: 2 turns - mark inplay false
# calculate offer/show previous offers/board
# deal or no deal
#
# round 6-10: 1 turns - mark inplay false
# calculate offer/show previous offers/board
# deal or no deal
#
# end game
# reveal case and board
# did you make a good deal?
# thank you for playing
# display high score 
# write score to file if new high score

######################################################################
######################################################################

from random import shuffle


Values = [ 0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,
1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 
400000, 500000, 750000, 1000000]

# 26 Cases total 
Cases = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

Rounds = [ 6,5,4,3,2,1,1,1,1,1 ]

Prizes = []

MyCase = 0

RecalcOffer = True

# Ten historical offers - formatted as strings
Offer = ['','','','','','','','','','','','','']





# 10 turns maximum

#Taunts[]
#prompts[]

class Prize:

	def __init__(self, NewValue, NewCase):
		self.Value = NewValue
		self.Active = True
		self.Case = NewCase 

		# converts Value to fixed-width space-padded string with commas
		self.TextValue = "{: >11s}".format("{:,}".format(self.Value))

		# print(self.Case, self.Value)

	def Play(self):
		self.Active = False
		self.TextValue = "***********"




def PrintBoard(ShowOffers):

	print("\n")
	print("|---------------------------|")
	print("|----  DEAL OR NO DEAL  ----|")
	print("|---------------------------|")

	for x in range(0,int(len(Prizes)/2)):
		print("| {} | {} |".format( 
		Prizes[x].TextValue, Prizes[x+13].TextValue), end="")

		if(len(Offer[x]) and ShowOffers):
			print(" Previous Offer:", Offer[x])
		else:
			print("")

	print("|---------------------------|", end="")
	if(ShowOffers):
		print(" Bank Offer: {:,}".format(BankOffer()))
	else:
		print("\n")

	Remaining = []

	for x in range(0,len(Prizes)):
		if(Prizes[x].Active):
			Remaining.append(Prizes[x].Case)


	Remaining = sorted(Remaining)

	print("Remaining cases")

	for s in Remaining:
		if(s != MyCase):
			print("{} ".format(str(s)), end="")


	print("\n")



def OpenCase(Choice):

	global RecalcOffer

	# find Case in Prizes

	for x in range(0, len(Prizes)):
		if(Prizes[x].Case == int(Choice) and int(Choice) != MyCase):
			RecalcOffer = True
			Prizes[x].Play()
			break





def ChooseCase():

	global MyCase

	print("""

Welcome to DEAL OR NO DEAL

There are 26 cases numbered 1 through 26.
Each case has a cash prize inside ranging 
from a penny to one million dollars.  They
are in random order. 

Which case do you believe is the case with
one million dollars?""")


	while(MyCase<1 or MyCase>26):
	
		print("Choose your lucky case number (1 - 26):", end="")
		s = input()
		if(not s.isdigit()):
			MyCase = 0
		MyCase = int(s)

	print("""
Wonderful! Your case is {}. Let's hope you 
have the one million dollars in your case.""".format(MyCase))
	
	return()


def BankOffer():

	Total = 0
	Cnt = 0
	NewOffer = 0
	global Offer
	global RecalcOffer

	# add up all remaining prizes
	# and divide by how many cases remain

	for x in range(0, len(Prizes)):
		if(Prizes[x].Active):
			Total = Total + Prizes[x].Value
			Cnt = Cnt + 1

	if(Total > 0 and Cnt > 0):
		NewOffer = int(Total / Cnt)
	else:
		NewOffer = 0

	# round off the offer 

	if(NewOffer > 1000):
		NewOffer = int(NewOffer / 1000) * 1000
	elif(NewOffer > 500):
		NewOffer = int(NewOffer / 100) * 100
	elif(NewOffer > 100):
		NewOffer = int(NewOffer / 10) * 10


	if(RecalcOffer):
		RecalcOffer = False
		print("New Offer", end="")

		for x in range(0,10):
			if(Offer[x]==''):
				Offer[x] = "${:,}".format(NewOffer)
				break;

	return(NewOffer)



def main():
	# randomize cases
	# and crate list of cases

	shuffle(Cases)

	for x in range(0,len(Values)):
		Prizes.append(Prize(Values[x], Cases[x]))


	ChooseCase()

	#### LOOP ####

	Choice = ""

	while(Choice != "q"):


		# outer loop - until the game is over
			# inner loop - choose 6,5,4,3,2,1 cases
			# - input/print board
		# print bank offer/deal or no deal


		PrintBoard(True)

		print("Choose a case to open: ", end="")
		Choice = input()

		if(Choice.isdigit()):
			OpenCase(Choice)




###################################################################
main()
