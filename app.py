#importing

import input_handler
import random
import webbrowser

#gameloop function, args are defined when function is called

def game_loop(p_hp, c_hp):

        while(p_hp > 0 and c_hp > 0):

            try:

                #getting the input from the attack and defense functions by calling them and making a variable equal to the returned integer

                p_attack = input_handler.attack_input()
                p_defense = input_handler.defense_input()

                #using the random module to get a new randomized number on every function call

                c_attack = random.randint(0,100)
                c_defense = random.randint(0,100)

                print()
                print("PLAYER HP:", p_hp)
                print("OPPONENT HP:", c_hp)

                #only executes if the integer is within range

                if(p_attack <= 2 and p_defense <= 2):

                    #if conditions are met for either attack, player deals 10 damage to cpu

                    if((p_attack == 1 and c_defense < 50) or (p_attack == 2 and c_defense >=50)) :
                        c_hp = c_hp -10

                        #if cpu hp is greater than 0 after being attacked, displays message with remaining health.
                        #otherwise, you win.

                        if(c_hp > 0):
                            print()
                            print("PLAYER HITS FOR 10 DAMAGE")
                            print("OPPONENT HP REMAINING:", c_hp)
                        else:
                            print("VICTORY!")
                            webbrowser.open("https://images.unsplash.com/photo-1578269174936-2709b6aeb913?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80")
                            return

                    #if conditions are not met for attack, cpu will block

                    elif((p_attack == 1 and c_defense >= 50) or (p_attack == 2 and c_defense < 50)):
                        print()
                        print("OPPONENT BLOCKS")



                    #if conditions are met for either attack cpu will deal 10 damage to player

                    if((c_attack < 50 and p_defense == 1) or (c_attack > 50 and p_defense == 2)):
                        p_hp = p_hp -10

                        #if player hp is greater than 0 after being attacked, displays message with remaining health.
                        #otherwise, you lose.

                        if(p_hp > 0):

                            print()
                            print("OPPONENT HITS FOR 10 DAMAGE")
                            print("PLAYER HP REMAINING:", p_hp)
                            print()
                        else:
                            print("CRITICAL MISSION FAILURE!")
                            return

                        
                    elif((c_attack < 50 and p_defense == 2) or (c_attack > 50 and p_defense == 1)):
                        print()
                        print("YOU BLOCK THE ATTACK")
                        print()
                else:
                    print("input error, try again")

               #exception handler
                    
            except TypeError:
                print()
                print("invalid entry, try again")
                print()

            except ValueError:
                print()
                print("invalid value entry, try again")
                print()

            except:
                print("unknown error")
    
game_loop(100,100)
