damage = [[1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0/5, 2, 1, 2, 0.5],
          [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
          [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
          [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
          [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
          [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
          [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
          [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
          [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
          [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
          [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
          [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
          [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
          [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
          [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
          [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]]

types = {"normal": 0, "fighting" : 1, "flying": 2, "poison": 3, "ground": 4, "rock": 5, "bug": 6, "ghost": 7, "steel": 8, "fire": 9, "water": 10, "grass": 11,
         "electric": 12, "psychic": 13, "ice": 14, "dragon": 15, "dark": 16, "fairy": 17}
    
print("Welcome to the Pokemon type strength/weakness program.")

dmg_q = input("Do you want to know the damage you'll do on someone else, or the damage that someone else will do on you? (Choose 1 or 2 to pick your option) ")

if dmg_q == "1": 
    
    my_type = input("What type is your pokemon? ").lower()
    enemy_type = input("What type of pokemon do you think you'll be up against? ").lower()

    row = types[my_type]
    col = types[enemy_type]

    damage = damage[row][col]

    if damage == 1:
        print("Your " + my_type + " type pokemon will do a normal amount of damage to a " + enemy_type + " pokemon.")

    elif damage == 0.5:
        print("Your " + my_type + " type pokemon will only do half damage to a " + enemy_type + " type pokemon.")

    elif damage == 2:
        print("Your " + my_type + " type pokemon will do double damage to a " + enemy_type + " type pokemon.")
    input()

if dmg_q == "2":
    
    my_type = input("What type is your pokemon? ").lower()
    enemy_type = input("What type of pokemon do you think you'll be up against? ").lower()

    row = types[enemy_type]
    col = types[my_type]
    
    damage = damage[row][col]
    
    if damage == 1:
        print("Your " + my_type + " type pokemon take a normal amount of damage from a " + enemy_type + " pokemon.")

    elif damage == 0.5:
        print("Your " + my_type + " type pokemon will only take half damage from a " + enemy_type + " type pokemon.")

    elif damage == 2:
        print("Your " + my_type + " type pokemon will take double damage from a " + enemy_type + " type pokemon.")
    input()

