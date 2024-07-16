import os
import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter.scrolledtext import ScrolledText

class Generate:
    def __init__(self, timer):
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title("Productoro Fitness")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '../Assets/workout-image.png')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file=image_path))

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Calibri", 16))
        self.s.configure("TButton", font=("Calibri", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=2, expand=True)

        self.prod = ttk.Frame(self.tabs, width=600, height=10)
        self.exer = ttk.Frame(self.tabs, width=600, height=10)
        self.brk = ttk.Frame(self.tabs, width=600, height=10)

        self.prod_timer_label = ttk.Label(self.prod, text="25:00", font=("Calibri", 48))
        self.prod_timer_label.pack(pady=20)

        self.exer_timer_label = ttk.Label(self.exer, text="3:00", font=("Calibri", 48))
        self.exer_timer_label.pack(pady=20)

        self.brk_timer_label = ttk.Label(self.brk, text="7:00", font=("Calibri", 48))
        self.brk_timer_label.pack(pady=20)

        self.tabs.add(self.prod, text="Productivity")
        self.tabs.add(self.exer, text="Exercise")
        self.tabs.add(self.brk, text="Break")

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.timer = timer
        self.timer.set_display(self)
        
        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.timer.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.timer.skip_session)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.timer.reset_timer)
        self.reset_button.grid(row=0, column=2)

        self.session_total = ttk.Label(self.grid_layout, text="Total Sessions: 0", font=("Calibri", 16))
        self.session_total.grid(row=1, column=0, columnspan=3)

        self.completed_exercises_label = ttk.Label(self.grid_layout, text="Completed Exercises:", font=("Calibri", 16))
        self.completed_exercises_label.grid(row=2, column=0, columnspan=3)

        self.completed_exercises_text = ScrolledText(self.grid_layout, width=60, height=10, font=("Calibri", 12), state='disabled')
        self.completed_exercises_text.grid(row=3, column=0, columnspan=3, pady=5)

        self.exercise_reps = {}  # Dictionary to keep track of completed exercises and reps

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def on_closing(self):
        self.timer.stopped = True
        self.root.destroy()
        self.root = None

    def update_prod_timer_label(self, text):
        if self.root:
            self.prod_timer_label.configure(text=text)
            self.root.update()
    
    def update_exer_timer_label(self, text):
        if self.root:
            self.exer_timer_label.configure(text=text)
            self.root.update()

    def update_brk_timer_label(self, text):
        if self.root:
            self.brk_timer_label.configure(text=text)
            self.root.update()

    def update_session_total(self, text):
        if self.root:
            self.session_total.configure(text="Total Sessions: " + str(text))
            self.root.update()

    def update_workout_label(self, workout):
        if self.root:
            self.completed_exercises_text.configure(state='normal')
            self.completed_exercises_text.insert(tk.END, f"{workout}\n")
            self.completed_exercises_text.configure(state='disabled')
            self.completed_exercises_text.yview(tk.END)
            self.root.update()

    def update_workout_label_with_reps(self, exercise_reps):
        if self.root:
            self.completed_exercises_text.configure(state='normal')
            self.completed_exercises_text.delete(1.0, tk.END)
            for exercise, reps in exercise_reps.items():
                self.completed_exercises_text.insert(tk.END, f"{exercise}: {reps} reps\n")
            self.completed_exercises_text.configure(state='disabled')
            self.completed_exercises_text.yview(tk.END)
            self.root.update()

    def clear_workout_label(self):
        if self.root:
            self.completed_exercises_text.configure(state='normal')
            self.completed_exercises_text.delete(1.0, tk.END)
            self.completed_exercises_text.configure(state='disabled')
            self.root.update()
