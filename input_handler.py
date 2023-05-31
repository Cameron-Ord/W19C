
def attack_input():
        #reads input from user
    print("ATTACKS:")
    try:
        print("1. PUNCH")

        print("2. KICK")
            #if the input is "1" or "2" returns it as an integer
        attack = input("CHOOSE ATTACK:")

        if(attack == "1" or attack == "2"):
            return (int(attack))
            
          #Exception handler. 
    
    
    except ValueError:
        print("please enter a number")
     
    except TypeError:
        print("invalid entry, try again")
   
    except:
        print("Something went wrong")





def defense_input():
            #reads input from user
    try:
        print("DEFENSE:")

        print("1. HIGH")

        print("2. LOW")

        defense = input("ENTER DEFENSE:")

            #if the input is "1" or "2" returns it as an integer

        if(defense == "1" or defense == "2"):
          return (int(defense))
        
           #Exception handler. 

    except TypeError:
        print("invalid entry, try again")
    
    except ValueError:
        print("invalid entry, try again")
      
    except:
        print("Something went wrong")