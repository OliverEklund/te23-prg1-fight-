from random import randint
print("Välkommen till Fantasy Duel! I detta spel kommer du och datorn mötas i en duel baserad på tärningskast.")

player_1_name = input(f"Spelare 1, skriv ditt namn: ")
#player_1_class = input(f"Välkommen {player_1_name}, välj din klass")
#print("Riddare, +4 för att träffa, 3 skada, 4+ för att undvika skada, 15 hälsa")
#print("tjuv, 3+ för att träffa, 1 skada, 3+ för att undvika skada, 8 hälsa")
#print("Suicide Bomber")

#Ide för nästa lektion: man har en variabel som är en 1d6. om resultatet är högre än fiendens attack slag så undiver man attacken.
# Man kan använda block för höja chansen att undvika!

player_1_damage = 3
player_1_health = 15
player_1_to_hit = 3

print(f"{player_1_name}'s förmågor är 3 skada, 3+ för att träffa och har 15 hälsa")
print(f"{player_1_name} kommer gå emot en slime med 10 hälsa och som gör 2 damage och träffar på 3 eller över")

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
        print(f"{player_1_name} använder sin sköld för att skydda från den nästa attacken.")
        player_1_dodge = randint(1,6)
    
    if player_one_action == "3":
        print(f"{player_1_name} aktiverar sin bomb vest och sprängs och dödar allting inom 20 meter")
        round_status = "N"
    
    print(f"Slimen attakerar {player_1_name} genom att skjuta spikar på dom.")
    player_two_roll = randint(1,6)
    
    if player_one_action == "2" and player_1_dodge >= 3:
        print(f"slimens attack är blokerad av {player_1_name}")
        
    elif player_two_roll >= 4:
        print(f"Slimens spik träffer {player_1_name} och gör {player_2_damage}")
        player_1_health -= player_2_damage
        print(f"{player_1_name} har {player_1_health} hälsa kvar")
    else:
        print("Slimen missar")


    if player_1_health <= 0:
        print(f"slimen vann genom att döda {player_1_name}")
        round_status = "N"
    
    if player_2_health <= 0:
        print(f"{player_1_name} van genom att döda slimen")
        round_status = "N"
    
    else:
         round_status = input("Redo för nästa runda? Skriv J: ")