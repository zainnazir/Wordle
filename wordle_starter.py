'''
Wordle Rules:
 Guess a five-letter word in six attempts.
 Each time you guess, you're told which of your chosen letters are in the target word, and whether they are in the right place
 Every time you make a guess you get feedback:
    Green - Correct letter in the correct spot
    Yellow - Correct letter in the incorrect spot
    Black - Incorrect letter

 There are no five-letter words that use the same letter four times. They can only be sets of two or three.

 If you try a word that shares duplicate letters with the answer, every instance of that letter will change color.
 For example, if you guess ”lever” and the answer is “eaten,” the first E in “lever” will turn yellow and the second one will turn green.
 The first one is in the word but in the wrong spot, and the second one is in the correct spot. The other letters will turn gray.

 Wordle tells you when a letter is not duplicated, too. If you use two of the same letter in a word, and only one of them turns yellow
   or green, then there is only one copy of that letter in the correct Wordle answer.

 AI mode
    -Rate AI's by average number of guesses for 1000 random games

 Extensions:
     -Keep track of wordle streaks
     -Wordle bot: https://www.tomsguide.com/news/wordlebot-is-a-new-tool-to-help-you-beat-wordle-and-its-brilliant

  Wordle Design Questions
    1) What are the rules for playing Wordle?
        -see above
    2) What functions will you use to break the big problem into smaller pieces?
        -see below
    3) How will you provide feedback without the use of color?
        -Incorrect letters
        -Correct letters, wrong spots
        -Correct letters, correct spots
    4) List some good test cases for Wordle
      -words with lengths that aren't 5 letters
      -winning outcome after n guesses
      -winning on 6th guess
      -duplicate guesses
      -guess with no correct letters
      -guess with correct letters, correct spot
      -guess with some correct letters in the correct spot, some correct letters in wrong spot
      -hidden word with duplicate letters ("MOTTO")
    5) What information is needed to compare AI approaches?
        -hidden word, list of guessed words
    6) What information is needed for an AI to make their next guess?
        -same feedback as for humans
'''

from  wordlist_helper import getWordList
def pickHiddenWord():
    '''
    Returns a single word from the list of allowable words
    '''
    #words = getWordList()
    return "MOTTO"

def getPlayerGuess():
    '''
    Prompts for and returns a player guess.
    Returns a string guess that is exactly 5 uppercase letters.
    '''
    return ""

def generateFeedback(guess, hiddenWord, feedback):
    '''
    Returns a list of feeback based on comparing guess with the hidden word
    '''

    return feedback

def displayFeedback(feedback):
    '''
    Displays ongoing feedback guesses in a understndable manner
    '''
    print(feedback)

def playWordle():
    '''
    Plays a complete game of wordle. Up to six guesses.
    Returns the hidden word an a list of all player guesses
    '''
    hiddenWord=pickHiddenWord()
    guesses=[None]
    #0) Initialize necessary variables, including picking the hidden word

    #1) Get a properly-formatted player guess

    #2) Determine and display feedback on the guess

    #3) Check to see if the game is over, if not, goto step #1

    return hiddenWord, guesses


if __name__ == "__main__":
    hiddenWord, guesses = playWordle() #steps 0 -3

    #4) When the game is over, display the hidden word
    print("The correct word was:"+hiddenWord)

    if hiddenWord!=guesses[len(guesses)-1]:
        print("You lost.")
    else:
        print("You won in "+str(len(guesses))+ " guesses!")

    print("Your guesses:", guesses)
