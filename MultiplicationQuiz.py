#Etienne Soltys
#1/9/25
#init
import random
random.randint
#Function
def game(): #Function for the whole game
    print("Hi, welcome to Multiplication quiz")
    questions = input("how many questions would you like to answer?")#Determines how many times the game will loop
    win = 0     #sets score to 0
    loss = 0    #sets score to 0
    for i in range(int(questions)):  #Loop that will run game the number of times the player said to
        var1 = (random.randint(1,10)) #setting variable 1 to be a random number from 1-10
        var2 = (random.randint(1,10)) #setting variable 2 to be a random number from 1-10
        ans = input("what is " + str(var1) +" times " + str(var2)) #the player's answer to the random numbers
        correct = int(var1 * var2) #New variable to represent the correct answer
        if ans == str(correct): #If player gets the answer correct
            print("you are correct")
            win = win +1  #Adds points to the player's score
        else: #If the player got it wrong
            print("you are wrong, the answer is " + str(correct)) #prints the correct answer
            loss = loss +1 #adds up the number of rounds the player lost
        print("right: " + str(win) + " wrong: " + str(loss)) # printing total score after the first round
    print("your final score is: " + str(win)) #prints the final score after the game is over

#Main
game() #the game function
