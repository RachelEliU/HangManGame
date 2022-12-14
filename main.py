# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YIV69mIrLsJsYVZtmS3qUtNLy_jfP4xr
"""

# In this Game we recive a text file with word and an index that repesnts the 
#secret word the player has to guess the word before the man gets "hung" 
def main():
  print("Welcome to the game the HandMan \n Please enter ")
  print("Please enter the file path ")
  filePath=input()
  num,secretWord=choose_word(filePath,index)
  oldLetters=[] #list of all the letters that have been used
  tree=""
  flage=True #a flage to check that the player still hasnt found the word 
  numberOfFailer=0
  while flage and numberOfFailer<7: #the player hasnt found the word and the man is not hung
   print("Please enter letter")
   letter=input()
   if validInput(letter,oldLetters): #checking the letter is valid and hasnt been pick yet
    word,old=showHiddenWord(secretWord,oldLetters,letter)
    oldLetters.append(letter)
    if old: #if the letter that the plaer picked this round was not in the secret word 
      numberOfFailer+=1
      print(printHanman(numberOfFailer))
      print(word)
    elif word==secretWord:#the player won 
      flage=False
      print("You Won good job the secret word is "+secretWord)
    else: #the player got the right letter but hasnt won yet
      print("Good job you got the letter right")
      print(word)
   else:
    print("You entered an unvalid char ")
  if numberOfFailer==7:
   print("You lost:( ")
  else:
    pass
  
if __name__ == "__main__":
    main()
    #---------------------------- Helping Project------------------------------------------------
    
#This function receives a file path to a file with diffrent words and an index wich repesnts the number of word that the player picked to be the secret word
# This function returns the number of words in the given file path with the secter word
def choose_word(filePath,index):
 wordFile=open(filePath,'r')
 word=wordFile.read()
 wordList=word.split(" ")
 wordFile.close()
 return len(wordList),wordList[index]

#Gets the number of failures tries the player did
#Returns a String that repesents the tree acording to the number of failures
def printHanman(numOfTries):
 handManTree=dict()
 handManTree[1]="    x-------x"
 handManTree[2]="    x-------x\n   |\n   |\n   |\n   |\n   |"
 handManTree[3]="    x-------x\n   |       |\n   |       0\n   |\n   |\n   |"
 handManTree[4]="    x-------x\n   |       |\n   |       0\n   |       |\n   |\n   |"
 handManTree[5]="    x-------x\n   |       |\n   |       0\n   |      /|\\\n   |\n   |"
 handManTree[6]="    x-------x\n   |       |\n   |       0\n   |      /|\\\n   |      /\n   |"
 handManTree[7]="    x-------x\n   |       |\n   |       0\n   |      /|\\\n   |      / \\\n   |"
 return handManTree[numOfTries]

#This function recives a secret word, old letters that the play already picked and the new letter that the player picked 
#This function will return word showing only the letters that the player guessed and return if this new letter was in the secret word
def showHiddenWord(secretWord,oldLetters,newletter):
  word=""
  old=True
  for letter in secretWord:
    if letter in oldLetters:
      word+=letter
    elif letter==newletter:
      word+=letter
      old=False
    else :
     word+=" _ " 
  return word,old

#This function receives a letter and checks if it is valid return an ansew accordingly
def valid(letter):
 if len(letter)==1 and letter>='A' and letter <='z' :
   return True 
 else :
    return False
#This function receives a letter and checks if it is valid and hasnt been used before return an ansew accordingly
def validInput(letter,oldLetters):
  if valid(letter) and letter not in oldLetters:
   return True
  else:
    return False
