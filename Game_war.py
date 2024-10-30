import random
FIGHTER = {"health" :3,"attack" : 4,"dodge" : 3}
TANK = {"health" : 4, "attack" : 3, "dodge" : 1}
MAGE = {"health" : 1, "attack" : 5,"dodge" : 4}
TYPES = {"fighter" : FIGHTER, "tank" : TANK, "mage" : MAGE }

# Tambahkan class Character di bawah ini
class Character:
    def __init__(self, char_type):
        self.char_type = char_type
        self.health = 0
        self.attack = 0
        self.dodge = 0
        self.assign_attributes()
    
    def assign_attributes(self):
        type_dict =  TYPES[self.char_type]
        self.health = type_dict["health"]
        self.attack = type_dict["attack"]
        self.dodge = type_dict["dodge"]

    def __str__(self):
            return self.char_type
        
    def attack_enemy(self):
        return self.attack
    
    def take_damage(self, damage):
        if self.dodge_success():
            return "Missed"
        self.health -= damage
        return f"{self.char_type} took {damage} damage" 
    
    def dodge_success(self):
        dodge_change = self.dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_change:
            return True
        return False
    
    def is_dead(self):
        return self.health <= 0

def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)
    coin_toss = random.randint(0,1)
    if coin_toss == 0:
        first, second = [character_1, character_2]
    else:
        first, second = [character_2, character_1]
    
    while True:
        if attack_character(first, second):
            return str(first)   
        else:
            return str(second)

def attack_character(first, second):
    damage = first.attack_enemy()
    second.take_damage(damage)
    if second.is_dead():
        return True
    return False

game_turn = 1
char1_attack = 0
char1_score = 0
char2_attack = 0
char2_score = 0
roles = ["fighter", "tank", "mage"]

while game_turn == 1:
    player = None
    comp = None
    while player == None: 
        player = int(input("""Available Character\n1. Fighter\n2. Tank\n3. Mage\nYour Choice : """))
        if player>3 or player<1:
            print("Invalid input")
            player = None
    while comp == None: 
        comp = random.randint(0,2)
        if comp == player-1:
            comp = None
    char_1 = roles[player-1]
    char_2 = roles[comp]
    print("Player choice : " + char_1)
    print("Computer choice : " + char_2)
    input("Press Enter to continue...") 
    for _ in range(100):
        winner = character_fight(char_1, char_2)
        if winner == char_1:
            char1_attack += 1
        else:
            char2_attack += 1
    
    print("Result : ")
    print(f"{char_1} : {char1_attack}")
    print(f"{char_2} : {char2_attack}")
    if char1_attack == char2_attack:
        char1_score+=1
        char2_score+=1
    elif char1_attack > char2_attack:
        char1_score+=1
    else:
        char2_score+=1
    
    char1_attack = 0
    char2_attack = 0
    print("==== Score ===== ")
    print(f"PLAYER : {char1_score}")
    print(f"COMP : {char2_score}")
    game_turn = int(input("1 to continue the game -1 to stop the game : "))