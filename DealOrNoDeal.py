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

Prizes = []


# 10 turns maximum


#Taunts[]
#prompts[]

Rounds = [ 6,5,4,3,2,1,1,1,1,1 ]

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




def PrintBoard():

	print("\n")
	print("|---------------------------|")
	print("|----  DEAL OR NO DEAL  ----|")
	print("|---------------------------|")

	for x in range(0,int(len(Prizes)/2)):
		print("| {} | {} |".format( 
		Prizes[x].TextValue, Prizes[x+13].TextValue ))

	print("|---------------------------|")
	print("\n")

	Remaining = []

	for x in range(0,len(Prizes)):
		if(Prizes[x].Active):
			Remaining.append(Prizes[x].Case)


	Remaining = sorted(Remaining)

	for s in Remaining:
		print("{} ".format(str(s)), end="")

	print("\n")

	print("Bank Offer: {:,}".format(BankOffer()))

	print("\n\n")



def OpenCase(Choice):

	# find Case in Prizes

	for x in range(0, len(Prizes)):
		if(Prizes[x].Case == int(Choice)):
			Prizes[x].Play()
			break

	#Prizes[6].Play()


def BankOffer():

	Total = 0
	Cnt = 0
	Offer = 0

	# add up all remaining prizes
	# and divide by how many cases remain

	for x in range(0, len(Prizes)):
		if(Prizes[x].Active):
			Total = Total + Prizes[x].Value
			Cnt = Cnt + 1

	if(Total > 0 and Cnt > 0):
		Offer = int(Total / Cnt)
	else:
		Offer = 0

	# round off the offer 

	if(Offer > 1000):
		Offer = int(Offer / 1000) * 1000
	elif(Offer > 500):
		Offer = int(Offer / 100) * 100
	elif(Offer > 100):
		Offer = int(Offer / 10) * 10

	return(Offer)



def main():
	# randomize cases
	# and crate list of cases

	shuffle(Cases)

	for x in range(0,len(Values)):
		Prizes.append(Prize(Values[x], Cases[x]))


	#### LOOP ####

	Choice = ""

	while(Choice != "q"):
		PrintBoard()

		print("Choose a case: ", end="")
		Choice = input()

		if(Choice.isdigit()):
			OpenCase(Choice)




###################################################################
main()
