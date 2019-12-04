from time import sleep
print("WELCOME TO HANGMAN,THE GAME THAT YOU CAN NEVER WIN")
print("You have 10 tries to guess any word that you can think of.Try your best")
print("GOOD LUCK")
sleep(4)
def hangman():
    words_list=["awkward","gazebo","inexorable","phlegm","kiosk","jinx","fervid","zigzag","humid","antimonopologeographicationalism","fervid","jukebox","memento","ostracize"]
    num_guess=10
    while num_guess!=0:
     guess=input("Guess any word you can think of: ")
     num_guess-=1
     for i in words_list:   
      if guess not in words_list and num_guess==9 and num_guess!=0:
        print("Incorrect,Keep trying, You still have 9 guessess left")
        break
      if guess not in words_list and num_guess==5 and num_guess!=0:
        print("Incorrect,Halfway, You have 5 guesses left")
        break
      if guess not in words_list and num_guess!=9 and num_guess!=5 and num_guess!=1 and num_guess!=0:
        print(f"Incorrect,You have {num_guess} guesses left")
        break
      if guess not in words_list and num_guess==1:
        print("You have 1 guess left, Make this last guess count")
        break
      if guess not in words_list and num_guess==0:
       print("Sorry,You are out of guesses")
       break
      elif guess in words_list:
          print("Nice one,You got it!")
          num_guess=0
          break

hangman()
answer=input("Would you like to play again? ").lower()
if answer=="yes":
   print(hangman())
else:
     print("Alright,pls feel free to play any other game in the GAME CENTER")
