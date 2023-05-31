#importing

import input_handler
import random

#gameloop function, args are defined when function is called

def game_loop(p_hp, c_hp):
    #getting the input from the attack and defense functions by calling them and making a variable equal to the returned integer
    p_attack = input_handler.attack_input()
    p_defense = input_handler.defense_input()
    #using the random module to get a new randomized number on every function call
    c_attack = random.randint(0,100)
    c_defense = random.randint(0,100)

    
    try:
        #only executes if the integer is within range

        if(p_attack <= 2 and p_defense <= 2):
            print()
            print("PLAYER:", p_hp)
            print("OPPONENT:", c_hp)
            print()
                
                #The play and computer either block or receive damage based off the following conditions
                

                    #if the player choses punch and the cpu rolls a defense less than 50: the player will deal 10 damage

            if(p_attack == 1 and c_defense < 50):
                c_hp = c_hp -10
                print("PLAYER HITS FOR 10 DAMAGE")
                print("ENEMY HP REMAINING:",c_hp)
                print()

                    #if the player choses punch and the cpu rolls a defense equal to or greater than 50: the cpu will block the attack.

            elif(p_attack == 1 and c_defense >= 50):
                print("OPPONENT BLOCKS")
                    
                    #if the player chooses kick and the cpu rolls a defense equal to or greater than 50: the player will deal 10 damage.

            if(p_attack == 2 and c_defense >=50):
                c_hp = c_hp -10
                print("PLAYER HITS FOR 10 DAMAGE")
                print("ENEMY HP REMAINING:",c_hp)
                print()

                    #if the player chooses kick and the cpu rolls a defense equal to or greater than 50: cpu will block the attack.
            
            elif(p_attack == 2 and c_defense < 50):
                print("OPPONENT BLOCKS")
                print()

                    #if the cpu rolls less than 50 on attack, and player choses high defense: the player takes 10 damage.

            if(c_attack < 50 and p_defense == 1):
                p_hp = p_hp -10
                print("OPPONENT HITS FOR 10 DAMAGE")
                print("PLAYER HP REMAINING:",p_hp)
                print()

                    #if cpu rolls less than 50 on attack, and player chooses low defense: the player will block.
                
            elif(c_attack < 50 and p_defense == 2):
                print("YOU BLOCK THE ATTACK")
                print()
                    
                    #if cpu rolls greater than 50 on attack, and player chooses low defense: the player takes 10 damage.

            if(c_attack > 50 and p_defense == 2):
                p_hp = p_hp -10
                print("OPPONENT HITS FOR 10 DAMAGE")
                print("PLAYER HP REMAINING:",p_hp)
                print()
                
                    #if cpu rolls greater than 50 on attack, and player chooses high defense: the player will block 

            elif(c_attack > 50 and p_defense == 1):
                print("YOU BLOCK THE ATTACK")
                print()
                

        else:
            #if int value is not within range it will error
            print("invalid input, try again")

        if(c_hp > 0 and p_hp > 0):
            #calls game_loop with current arg values if no one is dead.
            game_loop(c_hp, p_hp)
        elif(c_hp <= 0):
            #prints victory if you defeat the cpu
            print("victory")
        elif(p_hp <= 0):
            #prints a loss message if you lose
            print("critical mission failure")

            #if there was an error with inputs, calls the game loop function again. 

    except TypeError:
        print("invalid entry, try again")
        game_loop(p_hp,c_hp)
    except ValueError:
        print("invalid entry, try again")
        game_loop(p_hp,c_hp)
    except:
        print("unknown error")
    
game_loop(100,100)
