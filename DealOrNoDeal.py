# DealOrNoDeal.py
#
# Randomize all values into cases
# Choose a case for player - from 1 - 26 - mark inplay-False
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


Values = [ 0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750
1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

# 26 Cases total 
# randomize values into cases

Case[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
InPlay[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Taunts[]
prompts[]

Rounds = [ 6,5,4,3,2,1,1,1,1,1 ]

choose case
open 6 cases - 5, 25, 750, 10,000, 200,000, 400,000

offer - 30,000

open 5 cases

500,000, 5,000, 25,000, 400, 75

offer - 62,000

open 4 cases

300,000, 100, 10, 100,000

offer - 86,000

open 3 cases

500, 50,000, 300

offer - 141,000

open 2 cases

750,000, 1,000,000

offer - 9,000

open 1 case

.01

offer - 15,000

### offer calculation
1 in 5/1
1 in 5/50
1 in 5/200
1 in 5/1000
1 in 5/75000

20% of sum of all values = offer
round to nearest 1000.


open 1 case

200

offer - 21000

open 1 case

50

offer - 27000   (1 in 4 / 75000)

open 1 case

75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 
75000

offer - 500

2 cases left --- 
open player's case
$1000 















