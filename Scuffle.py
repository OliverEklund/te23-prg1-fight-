from random import randint
player_1_name = input("Player 1, write your name: ")
player_2_name = input("Player 2, write your name: ")

player_1_health = 40
player_2_health = 40

player_1_special_use = True
player_2_special_use = True

print(f"Now {player_1_name} and {player_2_name} will meet in battle. Both have {player_1_health} health. First to three rounds, wins.")
print("Both have a chance to do between 4 and 8 damage, which is subtracted by 1 to 3 dependent on enemy armor.")
print("Different attacks can change these throws.\n")

print("These are the special actions you can choose, they are strong but risky, and can only be used once per round!.")
print("Type 1 for M79 Grenade launcher, nothing like bringing a thumper to a fist fight! High damage")
print("Type 2 for Tungsten shield. Wait how is this one time use? BALANCE!")
print("Type 3 for psychic bolt, radiation has given you the ability to kill shit with your mind. Go Wizard, go!")
player_1_special = input("Player 1, choose you special: \n")

if player_1_special == "1":
    player_1_special_damage = 20
    player_1_special_armor = 0

if player_1_special == "2":
    player_1_special_damage = 0
    player_1_special_armor = 20

if player_1_special == "3":
    player_1_special_damage = 10
    player_1_special_armor = 0

print("These are the special actions you can choose, they are strong but risky, and can only be used once per round!.")
print("Type 1 for M79 Grenade launcher, nothing like bringing a thumper to a fist fight! High damage")
print("Type 2 for Tungsten shield. Wait how is this one time use? BALANCE!")
print("Type 3 for psychic bolt, radiation has given you the ability to kill shit with your mind. Go Wizard, go!")
player_2_special = input("Player 2, choose you special: \n")

if player_2_special == "1":
    player_2_special_damage = 20
    player_2_special_armor = 0

if player_2_special == "2":
    player_2_special_armor = 20
    player_2_special_damage = 0

if player_2_special == "3":
    player_2_special_damage = 10
    player_2_special_armor = 0

round_status = input("Are you ready to play? (J/N): ")
print("")
while round_status == "J":

    
    player_1_armor = randint(1,3)
    player_2_armor = randint(1,3)

    print(f"{player_2_name} stands in front of you, what are you going to do?")
    print("Type 1 to do a high attack, type 2 for a central attack, type 3 for a low attack, type 4 to counter , type 5 to special action")
    player_1_action = input("What are you going to do?: ")
    
    if player_1_action == "1":
        player_1_damage = randint(6,8) - player_2_armor + 4
        player_1_armor = randint(1,3) - 1
    
    if player_1_action == "2":
        player_1_damage = randint(4, 8) - player_2_armor
    
    if player_1_action == "3":
        player_1_damage = randint (1, 3)
    
    if player_1_action == "4":
        player_1_armor == randint(3,6) + 2
        player_1_damage = 0
    
    if player_1_action =="5" and player_1_special_use is False:
        print("you can only special once")
        player_1_armor = 0
        player_1_damage = 0
   
    
    
    
    print("")

    print(f"{player_1_name} stands infront of you, what are you going to do?")
    print("Type 1 to do a high attack, type 2 for a central attack, type 3 for a low attack, type 4 to #counter , type 5 to special action")
    player_2_action = input("What are you going to do?: ")
      
    if player_2_action == "1":
        player_2_damage = randint(6,8) - player_1_armor + 4
        player_2_armor = randint(1,3) - 2
    
    if player_2_action == "2":
        player_2_damage = randint(4, 8) - player_1_armor
    
    if player_2_action == "3":
        player_2_damage = randint (1, 3)
    
    if player_2_action == "4":
        player_2_armor == randint(3,6) + 2
        player_2_damage = 0
    
    if player_2_action =="5" and player_2_special_use is False:
        print("you can only special once")
        player_2_damage = 0
        player_2_armor = 0
    
    if player_1_action =="5" and player_1_special_use is True:
        player_1_armor = player_1_special_armor

    if player_2_action =="5" and player_2_special_use is True:
        player_2_armor = player_2_special_armor
    
    if player_1_action =="5" and player_1_special_use is True:
        player_1_damage = player_1_special_damage - player_2_armor
        player_1_special_use = False
    
    if player_2_action =="5" and player_2_special_use is True:
        player_2_damage = player_2_special_damage - player_1_armor
        player_2_special_use = False
    
    # Above is the important code
    print("Both players have now chosen their action, let the fight begin!\n")
    # Below is the fluff text

    if player_1_action == "1":
        print(f"{player_1_name} punches {player_2_name} in the face")
    
    if player_1_action == "2":
        print(f"{player_1_name} gutpunches {player_2_name}")
    
    if player_1_action == "3":
        print(f"{player_1_name} sweeps the leg on {player_2_name}")
    
    if player_1_action == "4":
        print(f"{player_1_name} holds his hands out to block {player_2_name} attack")
    
    if player_1_action == "5" and player_1_special == "1":
        print(f"{player_1_name} shoots {player_2_name} with his M79 Thumper, nice going")
    
    if player_1_action == "5" and player_1_special == "2":
        print(f"{player_1_name} holds up his shield made of solid tungsten to block {player_2_name} attack. To bad its one use only.")

    if player_1_action == "5" and player_1_special == "3":
        print(f"{player_1_name} shoots {player_2_name} with a psychic blast, somehow.")

    print("")
    
    if player_2_action == "1":
        print(f"{player_2_name} punches {player_1_name} in the face")
    
    if player_2_action == "2":
        print(f"{player_2_name} gutpunches {player_1_name}")
    
    if player_2_action == "3":
        print(f"{player_2_name} sweeps the leg on {player_1_name}")
    
    if player_2_action == "4":
        print(f"{player_2_name} holds his hands out to block {player_1_name} attack")
    
    if player_2_action == "5" and player_2_special == "1":
        print(f"{player_2_name} shoots {player_1_name} with his M79 Thumper, nice going")
    
    if player_2_action == "5" and player_2_special == "2":
        print(f"{player_2_name} holds up his shield made of solid tungsten to block {player_1_name} attack. To bad its one use only.")

    if player_2_action == "5" and player_2_special == "3":
        print(f"{player_2_name} shoots {player_1_name} with a psychic blast, somehow.")
    
    if player_1_action and player_2_action == "4":
        print("they are both just standing there, MENACINGLY!")
    
    print("")
    player_1_health = player_1_health - player_2_damage
    player_2_health = player_2_health - player_1_damage
    print(f"{player_1_name} has {player_1_health} left")
    print(f"{player_2_name} has {player_2_health} left")

    if player_1_health <= 0:
        round_status = "N"
        print(f"{player_2_name} has won this round by defeating {player_1_name}")
    if player_2_health <= 0:
        round_status = "N"
        print(f"{player_1_name} has won this round by defeating {player_2_name}")