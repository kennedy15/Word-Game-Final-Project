# Word-Game-Final-Project

# CSC 280 Final Project

#>>PYTHON 2.7<<!!! <- Just incase you try to run it on your laptop Justin

# Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modifieed by Bei Xiao <bxiao>
#
# Name          : Nathan Kennedy
# Collaborators : solo
# Time spent    : collectively ~ 20-25 hours

import math
import random
import string

ALPHABET = 'aeioubcdfghjklmnpqrstvwxyz*'
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz*'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    wordsum = 0
    #we set the wordsum = 0 so we have a base to work from
    for letter in word:
        letter = letter.lower()
        wordsum = SCRABBLE_LETTER_VALUES[letter] + wordsum
        #here in this for loop we iterate through each letter and pull its value from the dict and add it to wordsum to get the sum of points of the word

    #print 'first part of wordsum:', int(wordsum)
    word_length = len(word)
    #here we just set word_length to the len of the word
    #print 'Word Length:', int(word_length)
    
    if (7 * word_length - 3 * ( n- word_length)) > 1:
        #here is the formula used to calculate the extra points
        #if word length is greater then 1 do what?
        wordsum = wordsum * (7 * word_length - 3 * ( n- word_length))
        #add the extra points to wordsum
        return wordsum

    else:
        wordsum = wordsum * 1
        #if the above formula is less than one then it drops down here
        return wordsum
    
    #print 'second part of the wordsum:', int(wordsum)
    
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    #pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter)#, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
hand = deal_hand(HAND_SIZE)
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    new_hand = hand.copy()
    #set a new dict as a copy of the hand dict so we can modify it safely
    for letter in word:
        #iterate through each letter in the word given
        letter = letter.lower()
        #make it lower case to make everything the same
        if letter in new_hand:
            #here we check to make sure it is in the new_hand dict
            new_hand[letter] = new_hand[letter] - 1
            #if it is we subtract one from the value (this is important because..)
            if new_hand[letter] == 0:
                #when the value of the letter in new_hand reaches 0 we remove it
                new_hand.pop(letter)
    return new_hand    
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    #how i validate the word is with two "keys" those being case1 and case2 if both conditions are met then both keys will unlock the return true function
    #the assumptation im going off of here is that player should input a correct word to the game, so the program starts off that way by making case1 = True
    #but it do check that it is a valid word
    case1 = True
    case2 = False
    test_hand = hand.copy()
    #make a copy of the hand dict so we can change it safely
    for letter in word:
        #iterate through each letter in the word
        letter = letter.lower()
        #make it lowercase
        if letter in test_hand and case1 == True:
            #if the letter is in the hand and case1 is still true then we remove 1 from the value, this helps when a hand has multiple of the same letters
            test_hand[letter] = test_hand[letter] - 1
            if test_hand[letter] == 0:
                test_hand.pop(letter)
            case1 = True

        else:
            #if the letter is no longer in the hand or was never in the hand we switch case1 to false so we dont run more then we need to
            case1 = False

        if word.lower() in word_list:
            #this is a simple check to make sure that the word is in word_list, we'll handle wildcards in the below code
            case2 = True

        else:
            case2 = False

#Wildcard code here
#the wildcard code starts off by setting stoprunning and wildcard to false, these are conditions that will be used to test for a wildcard
    stoprunning = False
    wildcard = False
#it is important that both of these conditions are set to false so that the while loop can run, if there is no wildcard in the code then stoprunning will become True ending the while loop
    #and if there is a wildcard in the word and it equals a word then wildcard will return true ending the while loop
    while wildcard == False and stoprunning == False:
        #here we have the two conditions set to false so the program will look for wildcards in each word by default
        count = 0
        x = 0
        #count is used so that when the program finds a wildcard among a word it knows what positions the wildcard is in
        #x is used so that when it equals the len of the word the program knows that there was no wildcards in the word is stops running
        for letter in word:
            #scans each letter in a word
            if letter == '*':
                #if that letter equals a wildcard then...
                word = list(word)
                #we make a list of the word so we can change it
                for letter in VOWELS:
                    #we then iterate though each of the vowels
                    word[count] = letter
                    #adding each letter to the spot where the wildcard was found
                    #print 'replaced word:', word
                    word1 = ''.join(word)
                    #then we rejoin the list of the word into a string
                    if word1 in word_list:
                        #and test the word to see if it is in word_list
                        #print 'word1:', word1
                        case2 = True
                        wildcard = True
                        
##                for letter in CONSONANTS:
##                    word[count] = letter
##                    #print 'replaced word:', word
##                    word1 = ''.join(word)
##                    if word1 in word_list:
##                        #print 'word1:', word1
##                        case2 = True
##                        wildcard = True
                        
            else:
                #it is because of this else statement that the program knows that the word has no wildcards and stop running
                x = x + 1
                word = ''.join(word)
                #print word
                if x == len(word):
                    stoprunning = True
                    

            count = count + 1

    if case1 == True and case2 == True:
        #and if the word passes both conditions then the function will return true!
        return True

    else:
        #if it doesnt it will return false
        return False
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    #this programs finds out the length of a hand with a similiar method used in problem 1 to count the points of a word
    hand_leng = 0
    #set word_leng to 0
    for letter in hand:
        #iterate through each letter in hand and call upon the value, this way if there is multiple of the same letter in a hand we count correctly
        hand_leng = hand[letter] + hand_leng
        
    n = hand_leng    
    return n
    #return the integer ofthe hand_length
n = calculate_handlen(hand)
""" 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
"""
    
   # pass  # TO DO... Remove this line when you implement this function
#created this function myself because I needed to print the sting version of a hand alot
def mini_hand_update(hand):
    hand1 = hand.copy()
    #start off by making a copy of hand so we dont modify hand directly
    hand_list = []
    #make an empty list to deposit the letters into
    count = 0
    #set count to 0 so it can iterate through correcly each time
    while count <= HAND_SIZE:
        #while count is less that or equal to HAND_SIZE we will...
        for letter in hand1:
            #iterates through each letter(key) in hand1, the copy of hand
            if hand1[letter] > 0:
                #if the value is greater then one then we...
                #this if statement helps to add letters that are in the hand multiple times
                hand_list.append(letter)
                #append the letter to the empty list
            hand1[letter] = hand1[letter] - 1
            #remove one from the value of the key(letter0
        count = count + 1
        #add one to count

    hand_list = ' '.join(hand_list)
    #join the list into a string
    print 'Current Hand:', hand_list
    #and print!

#this is the main function that runs each hand in the game
def play_hand(hand, word_list):
    #we start off by..
    total = 0
    #setting total to 0, this way each round the current total is reset, dont worry we will store the overall total in the end
    end_hand = False
    #we set this to false so the while loop runs
    while end_hand == False:
        word_input = raw_input("Enter a word, or '!!' to indicate that you are finished: ")
        #here we ask the user if they want to input a word or end the hand
        word = word_input
        #make word equal to the users input
        if is_valid_word(word, hand, word_list) == True:
            #if the user input a word and it passes the validation test then...
            total = int(get_word_score(word, n)) + total
            #we get the total score of the word
            hand = update_hand(hand, word)
            #update the hand to remove the letters
            print str(word), 'earned', str(get_word_score(word, n)), 'points. Total:', str(total), 'points'
            #print the points that the word got the player
            mini_hand_update(hand)
            #and print the players new hand

        elif word_input != '!!':
            print 'Word is not valid, Try again.'
            #this if statement is to catch any words that arent the quit word or dont make sense

        if word_input == '!!':
            print 'Current Score: ', str(total), 'points'
            return total
            #if the input equals '!!' then the program knows to quit, returning total and breaking the while loop

        if len(hand) == 0:
            print 'Current Score: ', str(total), 'points'
            return total
        #this if statement is used to end the hand if the player used up all of their letters



    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    ALPHABET = 'aeioubcdfghjklmnpqrstvwxyz*'
    #here we set ALPHABET to equal both constants and vowels to make substituting a littler easier
    lettertest = False
    #naturll we assume that every letter will fail until proven other wise
    while lettertest == False:
        #while lettertest is false
        if len(letter) > 1:
            #we test for the length of said letter, to make sure the user input only one
            print "Please input only one letter."
            #let them know they goofed
            letter = raw_input("What letter would you like to substitute? ")
            #ask for new letter

        else:
            #if the letter does pass the lettertest then...
            print_statement = True
            #we sent the print_statement to true - this is so we dont print the "please input a l=letter you have in your hand" mulitple times for each failed attempt
            for piece in hand:
                #we use a for loop to iterate through each piece in the hand
                if piece == letter:
                    #make sure that the letter the user put in matches one in the hand
                    lettertest = True
                    #set this test to true ending the while loop
                    print_statement = False
                    #set print_statement to false so no error message prints letting the user know they goofed
            if print_statement == True:
                #this is just used to let the user know they goofed
                print "Please input a letter you have in your hand."
                letter = raw_input("What letter would you like to substitute? ")
                
                
    if lettertest == True:
        #if the letter passes both tests then we can finally substitute for the player!
        hand_copy = hand.copy()
        #make a copy of the hand
        for piece in hand:
            #iterate through each piece in the original hand
            if piece == letter:
                #find the piece that the player wants to substitute
                random_letter = random.choice(ALPHABET)
                #assign a random letter to random_letter
                hand_copy.pop(piece)
                #pop the piece that the player does not want in the copy of hand
                hand_test = True
                while hand_test == True:
                    #while this test is true...
                    for piece2 in hand_copy:
                        #we no iterate through the copy of hand
                        if random_letter == piece2:
                            #this is to make sure that the new letter we pick does not match one in the hand already
                            random_letter = random.choice(ALPHABET)
                            #if it does we switch it out and run it over again
                        else:
                            hand_test = False
                            #if it doesnt match a letter then we stop the test
                            
                hand[random_letter] = hand.pop(piece)
                #and then we input it into the original hand where the original letter was!
                """
                if you are wondering why we useda copy of hand and why we need to iterate through the copy, that is because
                if we only had one copy of hand, when we popped the letter the player wanted to replace, there would be no way
                to insert the new letter at that place, making sure the value(how many of that letter there was) stayed the same
                so we use a copy of the hand to make sure we didnt pick a copy of a letter already in the hand, then pass the newly picked
                letter back into the original hand for the letter that the user wanted to subsitute
                """

                        
        return hand
    #return hand
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    #pass  # TO DO... Remove this line when you implement this function
       
#here is the last function that ties everything together
def play_game(word_list):
    number_of_hands = int(raw_input("How many hands would you like to play? "))
    #we start off by asking how many hands the user wants to play
    HAND_SIZE = int(raw_input("What would you like the hand size to be set to? "))
    #we then allow the user to set the hand for the rounds
    if HAND_SIZE == 0:
        number_of_hands = 0
    #this little if statement is used to end the game if the user inputs 0 for the hand size
    hand = deal_hand(HAND_SIZE)
    #here we set the variable hand so it can be used in functions
    total_total_score = 0
    #set the score for 0 so nothing is carried over from previous games
    sub_letter = True
    #set sub_letter to true because the player gets to use substitute once each game
    redo = True
    #set redo to true because the player gets one redo each game
    while number_of_hands > 0:
        #while the number_of_hands is greater then 0 we will run the game
        mini_hand_update(hand)
        #print out the hand for the player
        if sub_letter == True:
            #check to see if the user wants to use substitute or not
            U_answer = raw_input("Would you like to substitute a letter? Note: you only get this option once a game. Yes or No only. ")
            U_answer = U_answer.lower()
            if U_answer == 'yes':
                #if the player does want to substitute then we run the substitute function!
                sub_letter = False
                #and we set sub_letter to false so the player cant run it again
                letter = raw_input("What letter would you like to substitute? ")
                hand = substitute_hand(hand, letter)               
                mini_hand_update(hand)
                #we then print out the new hand for the player with the substitute letter
        
 #       hand_redo_copy = hand.copy
        total = play_hand(hand, word_list)
        #this is where we set the total score of a hand round to total, but we dont add it to the overall score till after the player decides if they want to redo or not
        if redo == True:
            #since redo is set to true by default the player is asked everytime they finish a hand if they would like to redo it, until theu use up their one redo though
            redo_choice = raw_input("Would you like to replay your last hand? Yes or No only ")
            redo_choice = redo_choice.lower()
            if redo_choice == 'yes':
                #if they decide yes we then set total to 0, wiping the score of the round they just completed
                #they also dont get the chance to substitute because that question has already passed
                total = 0
                end_hand_copy = False
                #set this to false so the while loop will run
                while end_hand_copy == False:
                    #this while loop is directly copied from play_hand with no changes to it except at the end
                    mini_hand_update(hand)
                    word_input = raw_input("Enter a word, or '!!' to indicate that you are finished: ")
                    word = word_input
                    if is_valid_word(word, hand, word_list) == True:
                        total = int(get_word_score(word, n)) + total
                        hand = update_hand(hand, word)
                        print str(word), 'earned', str(get_word_score(word, n)), 'points. Total:', str(total), 'points'

                    elif word_input != '!!':
                        print 'Word is not valid, Try again.'

                    if word_input == '!!':
                        #here are the minor changes
                        print 'Current Score: ', str(total), 'points'
                        total = total
                        #we dont return total, instead total = total so we get the points from the redo round
                        redo = False
                        #set redo to false so the player cant use it again during a game
                        end_hand_copy = True
                        #set this to true ending the redo round


                
        total_total_score = total + total_total_score
        #here we add up the total scrores to equal the overall score
        hand = deal_hand(HAND_SIZE)
        #here we call a new hand for the next round
        


        number_of_hands = number_of_hands - 1
        #subtract one from the number_of_hands that the player set
        if number_of_hands != 0:
            #this if loop is only here so these print statements dont print when the game is over
            if number_of_hands == 1:
                #when its the last turn this will print instead of 'Number of Hands Remaining = 1
                print '>-New Hand-<'
                print 'This is your last turn.'
                
            else:
                print '>-New Hand-<'
                print 'Number of Hands Remaining: ', str(number_of_hands)
     #print the end of the game with the overall score       
    print '>------------------------<'
    print 'The End'
    print 'Overall Score = ', str(total_total_score), 'points' 
    
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    #print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
