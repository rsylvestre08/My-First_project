

trip_options = ['destinations', 'restaurants', 'transportation', 'entertainment']

import random
destinations = ['miami', 'green bay', 'new york', 'chicago']

restaurants = ['hibachi express', 'vortex', 'portellos', 'ruth chris']

transportation = ['car', 'train', 'plane', 'hovercraft']

entertainment = ['r&b festival', 'night club', 'football game', 'car show']

is_satisfied = False

while is_satisfied == False: 
     
    Trip_destinations = random.choice(destinations)
    print(Trip_destinations)

    food_options = random.choice(restaurants)
    print(food_options)

    means_of_transportation = random.choice(transportation)
    print(means_of_transportation)

    Festivites = random.choice(entertainment)
    print(Festivites)

    user_input = input("Are you satisfied? (y/n) ")
    if user_input == "y":
        print("Enjoy your trip!")
        is_satisfied = True
    elif user_input == "n":
        print("ok. lets try again.")
        
        trip_options = ['destinations', 'restaurants', 'transportation', 'entertainment']



    
    








