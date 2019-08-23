# string of 5 cards
# split 5 cards into a list
# check the suit of each member of the list
# if all the suits (second positions) are the same, assign as a flush
# otherwise, assign as not flush

# next check the rank of each member of the list
# if it's all in consecutive order by converting ranks to numbers, assign as a straight
    # if "A, 2, 3, 4, 5", still assign as straight, treating A as 1
    # if "A, K, Q, J, T", assign normally, also a straight here
# if 4/5 members of the list are ==, assign as four of a kind
# if 3/5 of the list is == and 2/5 is also ==, assign as full house
# if only 3/5 of the list is ==, assign as three of a kind
# if 2/5 are ==, and a different 2/5 are equal, assign as two pairs
# if only 2/5 are ==, assign as one pair
# if none of the above, pick best card from order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

# if flush is true, and straight is true, check start of list:
    # if list starts with A, assign as royal flush or
    # if list starts with anything else, assign as straight flush
# if above isn't true, leave rest of assigns the same

# if player1 and player2 both have a royal flush, call a tie
# if player1 and player2 both have a straight flush, winner == player witht the highest max value
# if player1 and player2 both have from lines 11-15, check both players unused cards, and pick highest number value as winner
# sort by highest group pairs wins