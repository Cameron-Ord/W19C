
def attack_input():

    print("ATTACKS:")
    try:
        print("1. PUNCH")

        print("2. KICK")

        attack = input("CHOOSE ATTACK:")

        if(attack == "1" or attack == "2"):
            return (int(attack))
            
         
    
    except ValueError:
        print("please enter a number")
        attack_input()
    except TypeError:
        print("invalid entry, try again")
        attack_input()
    except:
        print("Something went wrong")





def defense_input():

    try:
        print("DEFENSE:")

        print("1. HIGH")

        print("2. LOW")

        defense = input("ENTER DEFENSE:")

        if(defense == "1" or defense == "2"):
          return (int(defense))
        
           
           
        
    except TypeError:
        print("invalid entry, try again")
        defense_input()
    except ValueError:
        print("please enter a number")
        attack_input()
    except:
        print("Something went wrong")