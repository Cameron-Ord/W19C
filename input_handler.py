
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
            
          #Exception handler. It does not call the function on failure as any exception inside the app.py will call the gameloop function
    
    
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
        
           #Exception handler. It does not call the function on failure as any exception inside the app.py will call the gameloop function

    except TypeError:
        print("invalid entry, try again")
    
    except ValueError:
        print("invalid entry, try again")
      
    except:
        print("Something went wrong")