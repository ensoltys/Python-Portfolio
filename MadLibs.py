#Etienne Soltys
#Initalization
print("Welcome to Mad Libs! Answer the questions, and read your story.")
#Function
def game():
    adjective1 = input("Write an adjective:")
    animal = input("Write an animal:")
    verb = input("write a verb ending in -ing:")
    noun = input("Write a noun:")
    adjective2 = input("Write annother adjective:")
    print("We went to the zoo and saw a " + (adjective1) + (animal) + ". It was " + (verb) + " with a " + (noun) + ". What a " + (adjective2) + " day.")
#Maion
game()
