from random import randint
print("Välkommen till Fantasy Duel! I detta spel kommer du och datorn mötas i en duel baserad på tärningskast.")

player_1_name = input(f"Spelare 1, skriv ditt namn: ")
#player_1_class = input(f"Välkommen {player_1_name}, välj din klass")
#print("Riddare, +4 för att träffa, 3 skada, 4+ för att undvika skada, 15 hälsa")
#print("tjuv, 3+ för att träffa, 1 skada, 3+ för att undvika skada, 8 hälsa")
#print("Suicide Bomber")

player_1_damage = 3
player_1_health = 15
player_1_to_hit = 3

print(f"{player_1_name}'s förmågor är 3 skada, 3+ för att träffa och har 15 hälsa")
print(f"{player_1_name} kommer gå emot en slime med 10 hälsa och som gör 2 damage")

player_2_health = 10
player_2_damage = 2


round_status = input("Är du redo att köra? (J/N): ")

while round_status == "J":

    print("En grön slime står framför dig. Vad kommer du att göra?")
    print("skriv 1 för att slå med svärdet, skriv 2 för att blockera attack, skriv 3 för att sprängas")
    player_one_action = input("Vad gör du?: ")
    if player_one_action == "1":
        print(f"{player_1_name} slår mot slimen med sitt svärd")
        player_one_roll = randint(1,6)
        
        if player_one_roll >= 3:
            print(f"{player_1_name}'s svärd slår in i slimen och gör {player_1_damage} skada")
            player_2_health -= player_1_damage
            print(f"Slimen har {player_2_health} hälsa kvar")
        else:
            print(f"{player_1_name} missar")
    
    if player_one_action == "2":
        print(f"")
    
    round_status = input("skriv J för nästa runda: ")