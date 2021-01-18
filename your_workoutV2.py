from tkinter import *
import random
import reps
import moves

root = Tk()
root.geometry('300x300')
widget = Label(root)
widget.config(text = "Your Workout")
widget.pack()
root.title('Workout Project')
#Functions

def your_choice():
    player = input("What is your choice today?  mixed or other? :\n")
    if player == "beginner":
        print(beginner())
    elif player == "intermediate":
        print(intermediate())
    elif player == "advanced":
        print(advanced())
    else:
        quit

def beginner():
     print("This will include:\n {} rounds of {} reps"
            .format(reps.time_1, reps.schemeA))
     movements = random.choices(moves.begin, k=3)
     for  i in (movements):
         print(i)
     
def intermediate():
     print("This will include:\n {} rounds of {} reps"
           .format(reps.time_2, reps.schemeB))
     movements = random.choices(moves.inter, k=3)
     for i in (movements):
         print(i)
     
def advanced():
     print("This will include:\n {} rounds of {} reps"
           .format(reps.time_3, reps.schemeC))
     movements = random.choices(moves.advan, k=3)
     for i in (movements):
         print(i)
    
Button(root, text='beginner', font='ariel 15', command=beginner,
       bg='ghost white').place(x=60, y=120)
Button(root, text='Intermediate', font='ariel 15', command =intermediate, 
        bg='ghost white').place(x=60, y=180)
Button(root, text='Advanced', font='ariel 15', command=advanced, 
       bg= 'ghost white').place(x=60, y=240)

root.mainloop()


        

    



    
