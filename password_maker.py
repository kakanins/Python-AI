import random
import string
print("Welcome to Password Maker!")

adjectives_list = ["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]
nouns_list = ["Dinosaur", "Ball", "Dragon","Hammer", "Apple", "Duck", "Panda"]

                        #1
#---------------------------------------------------   
adjective = random.choice(adjectives_list)
noun = random.choice(nouns_list)    
number = random.randint(0, 100)    
char = random.choice(string.punctuation)
#---------------------------------------------------
                         #2
#---------------------------------------------------
password = adjective + noun + str(number) + char
print("Recommended password: " + password) 
#---------------------------------------------------