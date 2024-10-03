from random import randint
player_1_name = input("Player 1, write your name: ")
player_2_name = input("Player 2, write your name: ")

player_1_health = 40
player_2_health = 40

print(f"Now {player_1_name} and {player_2_name} will meet in battle. Both have {player_1_health} health. First to three rounds, wins.")
print("Both have a chance to do between 4 and 8 damage, which is subtracted by 1 to 3 dependent on enemy armor.")
print("Different attacks can change these throws.\n")

print("These are the special actions you can choose, they are strong but risky, and can only be used once per round!.")
print("Type 1 for nano-machines, will make your defense incredibly high, go for that RISK!")
print("Type 2 for M79 Grenade launcher, nothing like bringing a thumper to a fist fight! High damage but low armor penetration")
print("Type 3 for Tesla coil, shoot them with your soviet era tesla coil, decent enough damage but ignores armor")
player_1_special = input("Player 1, choose you special: \n")

print("These are the special actions you can choose, they are strong but risky, and can only be used once per round!.")
print("Type 1 for nano-machines, will make your defense incredibly high, go for that RISK!")
print("Type 2 for M79 Grenade launcher, nothing like bringing a thumper to a fist fight! High damage but low armor penetration")
print("Type 3 for Tesla coil, shoot them with your soviet era tesla coil, decent enough damage but ignores armor")
player_2_special = input("Player 2, choose you special: \n")

round_status = input("Are you ready to play? (J/N): ")
print("")
while round_status == "J":

    player_1_armor = randint(1,3)
    player_2_armor = randint(1,3)
    #player_1_damage = randint(4,8) - player_2_armor
    #player_2_damage = randint(4,8) - player_1_armor

    print(f"{player_2_name} stands in front of you, what are you going to do?")
    print("Type 1 to do a high attack, type 2 for a central attack, type 3 for a low attack, type 4 to counter , type 5 to special action")
    player_1_action = input("What are you going to do?: ")
    
    if player_1_action == "1":
        player_1_damage = randint(6,8) - player_2_armor + 4
        player_1_armor = randint(1,3) - 3
    
    if player_1_action == "2":
        player_1_damage = randint(4, 8) - player_2_armor
    
    if player_1_action == "3":
        player_1_armor = randint (3, 8)
    
    if player_1_action == "4":
        player_1_armor == randint(3,6) + 2
    

    #print(f"{player_1_name} stands infront of you, what are you going to do?")
    #print("Type 1 to do a high attack, type 2 for a central attack, type 3 for a low attack, type 4 to #counter , type 5 to special action")
    #player_2_action = input("What are you going to do?: ")