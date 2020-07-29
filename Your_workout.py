'''
Second project is a workout type program, 
which i want it to consist of workouts and 
rep schemes at random, however, i want 
it to have certain conditions and those 
conditions will be based off your level of 
fitness
'''
import random

#rep scheme depending on level
rep_schemeA = random.randint(5,10) #Beginner rep scheme
rep_schemeB = random.randint(10,20) #Intermiate rep scheme
rep_schemeC = random.randint(20,30) #Advanced rep scheme

#rounds depending on level.
time_1 = 3
time_2 = 5
time_3 = 7

#For strength workout only.
heavy_reps = random.choice(["1-1-1-1-1", "5-3-1", "1 rep max"])

#Choice on different levels but also to focus on a certain area.
mixed = ['beginner',
               'intermediate',
               'advanced']

other = ['cardio only',
             'strength only',
             'other']

#Multiple lists, to give the user a feel for different workouts.
beginner_movements = ['lunges', 'skipping', 'jumping jacks', 'air squats',
                                      '100m run', 'situps', '30second plank', 'kettlebell swings',
                                      'tricep dips', 'shoulder press', 'push ups']

intermediate_movements = ['push ups', 'burpees', 'weighted squats', 'deadlifts',
                                             'push press', 'box jumps', '300m run', '50 cals Assault bike',
                                             'pull ups', 'medicine ball slams', '1min plank']

advanced_movements = ['power snatches', 'power cleans', 
                    'handstand push ups','muscle-ups', 'dips', '500m run', 'clean and jerks', 'heavy deadlift',
                                        'pull ups', 'burpees', 'box jumps']

cardio_movements = ['1 mile run', '2 mile run', '5km cycle', '10km cycle', 'swimming', 'rowing']

strength_movements = ['Heavy Deadlift', 'Heavy squat', 'heavy clean', 'heavy push press']

other_movements = ['yoga', 'mobility work', 'pilattes', 'meditation']



#CONTROL FLOW
player = input("What is your choice today?  mixed or other?")

#When the user chooses mixed choice
if player == 'mixed':
    player_1 = input("Please choose beginner, intermediate or advanced: ")
#beginner
    if player_1 == 'beginner':
        print("Beginner workout includes:\n {}\n".format(random.choices(beginner_movements, k=3)))
        print("This will include:\n {} rounds of {} reps".format(time_1, rep_schemeA))
#intermediate
    elif player_1 == 'intermediate':
        print("Intermediate workout includes:\n {}\n".format(random.choices(intermediate_movements, k=3)))
        print("This will include:\n {} rounds of {} reps".format(time_2, rep_schemeB))
#advanced
    elif player_1 == 'advanced':
         print("Advanced workout includes:\n {}\n".format(random.choices(advanced_movements, k=3)))
         print("This will include:\n {} rounds of {} reps".format(time_3, rep_schemeC))
    else:
        print("Sorry you have not chosen")
         
#When the user chooses other
elif player == 'other':
    player_2 = input("Choose from cardio only, strength only and other:  ")
#Cardio only choice
    if player_2 == "cardio only":
        print("Cardio workout: {}\n ".format(random.choice(cardio_movements)))
#Strength Only
    elif player_2 == "strength only":
        print("Strength Workout: {} reps of {}\n ".format(heavy_reps, random.choice(strength_movements)))
#Other
    elif player_2 == "other":
        print("If you are tired today, try some: {}\n ".format(random.choice(other_movements)))
    else:
        print("Sorry, that is not on the list")
        
#Choice to quit
else:
     if player == "quit":
         print("You have a quit working out")
        
