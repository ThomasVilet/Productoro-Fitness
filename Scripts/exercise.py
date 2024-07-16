# This file/script will handle all the logistics of the small break in between a pomodoro session.
# The file will contain a library of body / weighted workouts that can be completed at your
# own pace / setting. The timer will start and the user will have to record their repitions
# and begin the next session of the pomodoro timer - send a confirmation to the timer script. 

import random
import tkinter as tk
from tkinter import simpledialog

class Exercise:
    def __init__(self):
        self.workouts = ["Push-ups", "Elevated Split Squat", "Pull-ups", "Burpees"]
        self.current_workout = None

    def assign_workout(self):
        self.current_workout = random.choice(self.workouts)
        return self.current_workout
    
    def completed_reps(self):
        root = tk.Tk()
        root.withdraw()
        reps = simpledialog.askinteger("Workout Complete", f"How many repetitions of {self.current_workout} did you complete?")
        root.destroy()
        if reps is not None:
            return reps
        return 0
