#Coffee-Crafter V2   -   By:  Dr.M-Dev
#note: this code is standalone and doesn't reqire importing packages outside the built-in packages in python


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


#______________________________________________________________________
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def logo():
    print('''  
    !P#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&G?:        
^G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#7         
@@@@@@@@@@GJ!^::^!JG@@@@@@@@@@GJ!^::^!JG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@@@5^   ^~~^   ^5@@@@@@5^   ^~~^   ^5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@@?  .5#@@@@#5.  ?@@@@?  .5#@@@@#5.  ?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@G   G@@@@@@@@G   G@@G   G@@@@@@@@G   G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@G   B@@@@@@@@B   G@@G   B@@@@@@@@B   G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@@7  :P&@@@@&P:  7@@@@7  :P&@@@@&P:  7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@@@Y:  :~77~:  :Y@@@@@@Y:  :~77~:  :Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!      
@@@@@@@@@&P?~:..:~?P&@@@@@@@@&P?~:..:~?P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@7      
@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^      
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?       
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&#GJ:        
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7^::::::^&@@?:::::::::::::::::::::::::^&@@?:::::^~!!!!!!~~:::^^^:.   
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&:        .&@@!                         .&@@!   :YB&&&&&&&&&@@@@@@@&G? 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.        .&@@!                         .&@@PYYY#@@@@@@@@@@@@@@@@@@@@@P
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.        .&@@!                         .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.         B@@P~^~~~~^^~~~~~~~~~~~~~~~^~J@@@~...J&@@@@@@@@@@@@@@@@@@@B!
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.         :P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@B!     :7JYYYYYYYYYYYYYYY?~. 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.           :~77777?@@@577777?@@@577777!^                             
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                   5#G:      5#G:                                                                                                                                       
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                  .&@@!     .&@@!                                    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                   YBP:      YBP:                                    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                                                                                   
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                                                                     
!!!!!!!!!!!!?&@@@@@@@@@@@@@@@&.    7PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPJ.                     
::::::::::::^#@@@@@@@@@@@@@@@&.   .&@@&###################################&@@@#G5?^                 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.    G@@5 ................................. !@@@B#@@@G^               
????????????Y&@@@@@@@@@@@@@@@&.    7@@&:                                  P@@P  :5@@#.              
            :B@@@@@@@@@@@@@@@&.     P@@G.                                J@@&:   5@@B               
&&&&&&&&&&&&@@@@@@@@@@@@@@@@@&.     .G@@G:                              Y@@#^  ~G@@#^               
555555555555G@@@@@@@@@@@@@@@@&.      .5@@&?.                          ~B@@@5?YB@@&Y.                
            .B@@@@@@@@@@@@@@@&.        !B@@#?:                     .!G@@@@@@@@#G?:                  
BBBBBBBBBBBB&@@@@@@@@@@@@@@@@@^          !G@@&P?^.              :75#@@B?^^^::.                      
GGGGGGGGGGGGB@@@@@@@@@@@@@@@@@&Y!~~~~~~~~~~JB@@@@#G5J7!!!!!7?YP#@@@@#Y!~~~~~~~~~~~~~~~~~^.          
            .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P~        
PPPPPPPPPPPPB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Y       
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~      
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^      
^G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#7       
  !P#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&G?:         
  ''')


#=======================================================================================================================
#=======================================================================================================================+CODE RUNS HERE+
MACHINE_SAFE = 0.0
#
#MACHINE_START-UP SUPPLIES ---------------------------------->(after being recently restocked)
#that's how we will get the numbers and manipulate them easily
water_SUPPLY = resources["water"]
milk_SUPPLY = resources["milk"]
coffee_SUPPLY = resources["coffee"]
#
#________________________________Orders_Required_Resources:
# print(MENU["espresso"]["ingredients"])
#     "water": 50,
#     "coffee": 18,

# print(MENU["latte"]["ingredients"])
#     "water": 200,
#     "milk": 150,
#     "coffee": 24,

# print(MENU["cappuccino"]["ingredients"])
#     "water": 250,
#     "milk": 100,
#     "coffee": 24,





#=======================================================================================================================
def simple_reboot():
    global IS_ON
    #_____________________Turning the logo-display on, it will revert back to being off as soon as you enter the orders-menu :)
    global ShowLogoStuff
    ShowLogoStuff = True

    #--------------
    IS_ON = False
    print("\n" * 50)
    IS_ON = True
    #--------------



##==================================================
def calculating_order_cost(order):

    all_coins_are_checked = False
    #-------#just mentioned the float values, to avoid any bugs
    pennies = 0.0       #0.01 $
    nickles = 0.0       #0.05 $
    dimes = 0.0         #0.10 $
    quarters = 0.0      #0.25 $
    #-------#Checking if coins were acquired
    coins_acquired = False
    #
    total_inserted_coins = 0.0
    extra_change = 0.0
    #-------
    order_cost = MENU[order]["cost"]

    while not all_coins_are_checked:
        coins_acquired = True
        #--------------------
        print("\n")
        print(f"your order will be: ${order_cost}")
        print("This machine is coin-operated, meaning it will accept only coins [US-Currency] for this model \n<!>insert the coins needed for your order:\n")
    #-----------------------------------------------
        try:
            pennies = float(input("How many pennies"))
        except ValueError:
            print("\n<!>ERROR<!>you have inserted a letter as currency, please type numbers only") #this is for testing, in a real machine it will use sensors
            print("++++++++ try again :) +++++++++")
            calculating_order_cost(order)  # note that, it will be the same order :)
    #-----------------------------------------------
        try:
            nickles = float(input("How many nickles"))
        except ValueError:
            print("\n<!>ERROR<!>you have inserted a letter as currency, please type numbers only") #this is for testing, in a real machine it will use sensors
            print("++++++++ try again :) +++++++++")
            calculating_order_cost(order)  # note that, it will be the same order :)
    #-----------------------------------------------
        try:
            dimes = float(input("How many dimes"))
        except ValueError:
            print("\n<!>ERROR<!>you have inserted a letter as currency, please type numbers only") #this is for testing, in a real machine it will use sensors
            print("++++++++ try again :) +++++++++")
            calculating_order_cost(order)  # note that, it will be the same order :)
    # -----------------------------------------------
        try:
            quarters = float(input("How many quarters"))
        except ValueError:
            print("\n<!>ERROR<!>you have inserted a letter as currency, please type numbers only")  # this is for testing, in a real machine it will use sensors
            print("++++++++ try again :) +++++++++")
            calculating_order_cost(order)  # note that, it will be the same order :)

    #_____________________________________________________
    #_____________________________________________________
        if pennies == str or nickles == str or dimes == str or quarters == str:
            print("\n<!>ERROR<!>you have inserted a letter as currency, please type numbers only") #this is for testing, in a real machine it will use sensors
            print("try again")
        else:
            coins_acquired = True         #start a new check
            all_coins_are_checked = True #stopping the loop

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # conversion from digits to currency:
    US_pennies = pennies * 0.01
    US_nickles = nickles * 0.05
    US_dimes   = dimes * 0.10
    US_quarters = quarters * 0.25

    #_____________________________Calculation profit and change
    global MACHINE_SAFE
    #-------
    total_inserted_coins = US_pennies + US_nickles + US_dimes + US_quarters
    extra_change = 0.0

    if coins_acquired:
        if total_inserted_coins >= order_cost:
            MACHINE_SAFE += order_cost
            extra_change = round(total_inserted_coins - order_cost, 2)
            #------------
            print("\n")
            print(f"Here's your order, a fresh {order}, enjoy! :)")
            #------------
            if extra_change > 0:
                print(f"it seems that you inserted more coins than needed, here's your change: ${extra_change}")
                input("press any key to order again! :D")
                simple_reboot()
        else:
            print("<!>Insufficient coins! you can't order this :( ") #returning coins if the cost wasn't met
            print(f"here's your coins: ${total_inserted_coins}")
            input("press any key to order again! :D")
            simple_reboot()
    else:
        print("<!>ERROR<!> The Machine Require Coins! ") #debug & if no coins were inserted (if the code passed the first loop-check)


##==================================================
def making_orders(order):
    #1 First check if you have enough resources
    #2 Then check if the customer gave enough MONS
    #3 FINALLY gave change back after calculating MONS
    #
    #______________________________________________________[1]
    #1 First check if you have enough resources
    global water_SUPPLY
    global milk_SUPPLY
    global coffee_SUPPLY
    #
    water_REQ = 0
    milk_REQ = 0
    coffee_REQ = 0
    #_______________requirements \\
    if order == "cappuccino" or order == "latte":
        water_REQ = (MENU[order]["ingredients"]["water"])
        milk_REQ = (MENU[order]["ingredients"]["milk"])
        coffee_REQ = (MENU[order]["ingredients"]["coffee"])
    elif order == "espresso":
        water_REQ = (MENU[order]["ingredients"]["water"])
        coffee_REQ = (MENU[order]["ingredients"]["coffee"])
    else:
        print("<!>ERROR - Supplies Register Error<!>")

    #________________ESPRESSO\\
    if order == "espresso":
        if water_SUPPLY >= water_REQ and coffee_SUPPLY >= coffee_REQ:
            #taxation
            water_SUPPLY -= water_REQ
            coffee_SUPPLY -= coffee_REQ
            #creation
            #print("DEBUG: *SPAWNING ESPRESSO*")
            calculating_order_cost(order)
        elif water_SUPPLY < water_REQ:
            print(
                f"Apologies, the machine doesn't have enough water to make your {order}, return later when it's restocked :)")
        elif coffee_SUPPLY < coffee_REQ:
            print(
                f"Apologies, the machine doesn't have enough coffee to make your {order}, return later when it's restocked :)")
        else:
            print(f"Apologies, the machine doesn't have enough ingredients to make your {order}, return later when it's restocked :)")

    #________________Latte\\
    if order == "latte":
        if water_SUPPLY >= water_REQ and coffee_SUPPLY >= coffee_REQ and milk_SUPPLY >= milk_REQ:
            #taxation
            water_SUPPLY -= water_REQ
            milk_SUPPLY -= milk_REQ
            coffee_SUPPLY -= coffee_REQ
            #creation
            #print("DEBUG: *SPAWNING Latte*")
            calculating_order_cost(order)
        elif water_SUPPLY < water_REQ:
            print(
                f"Apologies, the machine doesn't have enough water to make your {order}, return later when it's restocked :)")
        elif milk_SUPPLY < milk_REQ:
            print(
                f"Apologies, the machine doesn't have enough milk to make your {order}, return later when it's restocked :)")
        elif coffee_SUPPLY < coffee_REQ:
            print(
                f"Apologies, the machine doesn't have enough coffee to make your {order}, return later when it's restocked :)")
        else:
            print(
                f"Apologies, the machine doesn't have enough ingredients to make your {order}, return later when it's restocked :)")

    # ________________Cappuccino\\
    if order == "cappuccino":
        if water_SUPPLY >= water_REQ and coffee_SUPPLY >= coffee_REQ and milk_SUPPLY >= milk_REQ:
            # taxation
            water_SUPPLY -= water_REQ
            milk_SUPPLY -= milk_REQ
            coffee_SUPPLY -= coffee_REQ
            # creation
            #print("DEBUG: *SPAWNING cappuccino*")
            calculating_order_cost(order)
        elif water_SUPPLY < water_REQ:
            print(
                f"Apologies, the machine doesn't have enough water to make your {order}, return later when it's restocked :)")
        elif milk_SUPPLY < milk_REQ:
            print(
                f"Apologies, the machine doesn't have enough milk to make your {order}, return later when it's restocked :)")
        elif coffee_SUPPLY < coffee_REQ:
            print(
                f"Apologies, the machine doesn't have enough coffee to make your {order}, return later when it's restocked :)")
        else:
            print(
                f"Apologies, the machine doesn't have enough ingredients to make your {order}, return later when it's restocked :)")

##==================================================
def restock ():
    global water_SUPPLY
    global milk_SUPPLY
    global coffee_SUPPLY
    #------------------
    added_water = 0
    added_milk = 0
    added_coffee = 0
    #========================================================
    print("\n" * 5)
    print("<!>ALERT<!> resources stock lid have been opened")
    #========================================================
    lid_open = True #a sensor will give this line of code a value of 0 or 1 for False or True to sense the lid is closed or not
                     #fornow it's 0 [False] "closed"
                     #unless the command to "restock" is activated, then it becomes 1/True
    print("how much would you want to restock,\n<!>NOTE<!>(this is for testing, the machine would use sensors instead of a direct input from the terminal)\n")

    #__________________________________________
    added_water = 0
    added_milk = 0
    added_coffee = 0
    try:
        added_water = float(input(f"How much water to add? MAX:{water_SUPPLY} although it can be exceeded."))
        water_SUPPLY += added_water
    except ValueError:
        print(
            "\n<!>INPUT ERROR<!>")  # this is for testing, in a real machine it will use sensors
        print("++++++++ try again :) +++++++++")
        restock ()
    #XXXXXXXXXXXXX----------
    try:
        added_milk = float(input(f"How much water to add? MAX:{milk_SUPPLY} although it can be exceeded."))
        milk_SUPPLY += added_milk
    except ValueError:
        print(
            "\n<!>INPUT ERROR<!>")  # this is for testing, in a real machine it will use sensors
        print("++++++++ try again :) +++++++++")
        restock ()
    #XXXXXXXXXXXXX----------
    try:
        added_coffee = float(input(f"How much water to add? MAX:{coffee_SUPPLY} although it can be exceeded."))
        coffee_SUPPLY += added_coffee
    except ValueError:
        print(
            "\n<!>INPUT ERROR<!>")  # this is for testing, in a real machine it will use sensors
        print("++++++++ try again :) +++++++++")
        restock ()
    #XXXXXXXXXXXXX----------
    #========================================================
    while lid_open:
        print("<!>NOTE<!> Confirm when you finished restocking, by typing (y/yes), note that the machine will sense if the lid is shut well after conformation.")
        #__________________________________________
        lid_switch = input("your command:").lower()

        if lid_switch == "y" or lid_switch == "yes" or lid_switch == "":
            lid_open = False
            #===============
            #GIVES REPORT ON THE VALUES:
            print("<!> Here's a brief report of the resources currently available in storage <!>")
            print("\n")
            print(f" Water : {water_SUPPLY}")
            print(f" Milk : {milk_SUPPLY}")
            print(f" Coffee : {coffee_SUPPLY}")
            print("\n")
            print(f"Cash currently in the register : {MACHINE_SAFE}")
            #===============
            simple_reboot()
        else:
            print("<!>ALERT<!> the lid is open, please close it and proceed with the instructions under the lid, then confirm by typing (y/yes)")


##==================================================
def processing_order(order):
    #order types:
    #off => turn off the machine
    #report => gives a report of [resources] and [money at the machine's safe]
    #drink request => (making-orders) functions
    #--------------------------------------------
    #to check money in register:
    global MACHINE_SAFE
    #reporting global resources
    global water_SUPPLY
    global milk_SUPPLY
    global coffee_SUPPLY
    #---------------------
    #to turn the machine off:
    global IS_ON

    #--------------------------------------------
    if order == "off":
        print("<!> Turning the coffee machine off <!>")
        IS_ON = False

    elif order == "report":
        print("<!> Here's a brief report of the resources currently available in storage <!>")
        print("\n")
        print(f" Water : {water_SUPPLY}")
        print(f" Milk : {milk_SUPPLY}")
        print(f" Coffee : {coffee_SUPPLY}")
        print("\n")
        print(f"Cash currently in the register : {MACHINE_SAFE}")

    elif order == "espresso" or order == "latte" or order == "cappuccino":
        making_orders(order)

    elif order == "restock":
        restock()

    elif order == "help":
        print("Status: RUNNING \nMachine model: {NO DATA AT ASSEMBLY}\nMachine serial number: {NO DATA AT ASSEMBLY} \n<!>NOTE (if you have Admin-Access)<!> : \n1-you can ask for a \"Report\" to check the resources inside the machine \n2-to restock the machine supplies, type \"restock\" and follow the given instructions on the label under the lid.  \n3-to turn off the machine type \"off\" followed by conformation \"y/yes\". \n")


#____________________________
def start_coffee_machine ():
    #Spacer:
    print("\n")
    #_____________________Stopping logo display for now
    global ShowLogoStuff
    ShowLogoStuff = False
    #_____________________
    order = input("What would you like to order from our menu? - the menu [espresso] [latte] [cappuccino] \n <!>NOTE: type \"help\" for more info \nType here: ").lower()
    #
    processing_order(order)






#=======================================================================================================================
#===========================================================Loop Run:
MAIN_Code_Running = True #this should not be changed (ONLY to turn off the whole code)

while MAIN_Code_Running:
    #defult state
    IS_ON = True
    ShowLogoStuff = True
    SWITCH = ""

    #-----------------------------
    while IS_ON:
        SWITCH = ""
        # --------------------
        if ShowLogoStuff:
            logo()
            print(" +++++++++++ Welcome To The Coffee-Crafter! - By: Dr.M-Dev +++++++++++++ ")
        # ---------------------
        start_coffee_machine()

    #-----------------------------
    else:
        print("\n" * 2)
        SWITCH = input("Confirm turning off the Coffee-Crafter (y/n)").lower()
        if SWITCH == "n" or SWITCH == "no":
            IS_ON = True
        else:
            print("The machine will remain off, thanks for visiting, hope to see you soon :)")
            MAIN_Code_Running = False #to stop the MAIN_Code_Running loop
