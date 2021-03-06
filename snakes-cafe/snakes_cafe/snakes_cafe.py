
# Signboard

print('\n \n ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

# all menu items stored in nested dictionary
menu = {
    'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
    'Entrées': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
    'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
    'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

# printing the items inside the menu
for items in menu:
    print(items, '\n-------')
    for item_name in menu[items]:
        print(item_name)
    print(' ')

print(' *********************************** \n ** What would you like to order? ** \n *********************************** \n')
# making a function to take the clients input and render it

# initial input with capitaliztation for the first word of any amount of words.
order = input('> ').lower().title()

# declaring an empty dictionary to store order history and quantities while the code is running
order_dic = {}


# if user didn't run 'quit" command excute the while loop
while order != 'Quit':

    # check if we have the input item in our menu
    for key in menu.keys():

        if order in menu[key].keys():
            
            # if item exists increment its value
            menu[key][order] += 1

            #adding orders into a list
            order_dic[order]= menu[key][order]

            # logic for output for a single or multiple orders
            if menu[key][order] == 1:
                print( f'\n ** {order} has been added to your meal ** \n')
                break
            else:
                print( f'\n ** {menu[key][order]} orders of {order} have been added to your meal ** \n')
                break

    # print this output if item not exists in our menu
    else:
        #when the user input "finish "the code will show the ordered items.
         if order == 'Finish':
          print (f'Clients Order is :')
          for key in order_dic :
            print (key, " : " , order_dic[key])
            #print(*order_list, sep='\n') // this was a nice way to print a list but i choose dictionary instead so i t will show the amount with the order
         else:
          print('\n ** Sorry this item is unavailable, please order item from our menu ** \n')

    # ask user again
    order = input('> ').lower().title()
else:
 print(' *********************************** \n ** Thank you for using snakes cafe! ** \n *********************************** \n')
    
    
