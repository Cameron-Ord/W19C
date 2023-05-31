import input_handler
import random



def game_loop(p_hp, c_hp):

    p_attack = input_handler.attack_input()
    p_defense = input_handler.defense_input()
    c_attack = random.randint(0,100)
    c_defense = random.randint(0,100)

    
    try:
        if(p_attack <= 2 and p_defense <= 2):
            print()
            print("PLAYER:", p_hp)
            print("OPPONENT:", c_hp)
            print()
            

            if(p_attack == 1 and c_defense < 50):
                c_hp = c_hp -10
                print("PLAYER HITS FOR 10 DAMAGE")
                print("ENEMY HP REMAINING:",c_hp)
                print()
                
            elif(p_attack == 1 and c_defense >= 50):
                print("OPPONENT BLOCKS")
                
            if(p_attack == 2 and c_defense >=50):
                c_hp = c_hp -10
                print("PLAYER HITS FOR 10 DAMAGE")
                print("ENEMY HP REMAINING:",c_hp)
                print()
            
            elif(p_attack == 2 and c_defense < 50):
                print("OPPONENT BLOCKS")
                print()

            if(c_attack < 50 and p_defense == 1):
                p_hp = p_hp -10
                print("OPPONENT HITS FOR 10 DAMAGE")
                print("PLAYER HP REMAINING:",p_hp)
                print()
                
            elif(c_attack < 50 and p_defense == 2):
                print("YOU BLOCK THE ATTACK")
                print()


            if(c_attack > 50 and p_defense == 2):
                p_hp = p_hp -10
                print("OPPONENT HITS FOR 10 DAMAGE")
                print("PLAYER HP REMAINING:",p_hp)
                print()
                
            elif(c_attack > 50 and p_defense == 1):
                print("YOU BLOCK THE ATTACK")
                print()
                

        else:
            print("invalid input, try again")

        if(c_hp > 0 and p_hp > 0):

            game_loop(c_hp, p_hp)
        elif(c_hp <= 0):
            print("victory")
        elif(p_hp <= 0):
            print("critical mission failure")
    
    except TypeError:
        print("invalid entry, try again")
        game_loop(p_hp,c_hp)
    except ValueError:
        print("invalid entry, try again")
        game_loop(p_hp,c_hp)
    except:
        print("unknown error")
    
game_loop(100,100)
