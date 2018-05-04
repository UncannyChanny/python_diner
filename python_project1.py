main_menu = ['King Crab', 'Ribs', 'Beef Wellington'] 

user = input('Please choose one Entree, we are offering King Crab, Ribs, and Beef Wellington tonight ')


total = 0


if user == "King Crab":
    print("MMM I love seafood, your total for the crab will be $5.25")
    total = total + 5.25

elif user == "Ribs":
    print("Our Ribs are the finest in town! Your total for the ribs will be $4.50")
    total = total + 4.50
elif user == "Beef Wellington":
    print("Chef Ramsey's favorite, that will be $3.75")
    total = total + 3.75
else:
    print("My apologies, I don't believe we carry that")


side_menu = ['Potatoes', 'Steak Fries', 'Cheese Curds']

user = input('Please choose a side with your meal! We have Potatoes, Steak Fries, and Cheese Curds. ')

if user == "Potatoes":
    print("Awesome, we take pride in our 'taters! ")
    total = total + 1.25
    print(f'Your current total is ${total}')

elif user == "Steak Fries":
    print("Yum! Nothing beats fries!")
    total = total + 1.75
    print(f'Your current total is ${total}')

elif user == "Cheese Curds":
    print("Gotta love them cheese curds, I tell ya what")
    total = total + 2.50
    print(f'Your current total is ${total}')

else:
    print('Sorry we don\'t have that tonight!')



