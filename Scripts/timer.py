import time
import threading

class Timer:
    def __init__(self, exercise):
        self.sessions = 0
        self.skipped = False
        self.stopped = False
        self.display = None
        self.running = False
        self.exercise = exercise

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.display.tabs.index(self.display.tabs.select()) + 1

        # Productivity Timer
        if timer_id == 1:
            full_seconds = 60 * 25
            # For testing
            # full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.display.update_prod_timer_label(f"{minutes:02d}:{seconds:02d}")
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped:
                self.sessions += 1
                self.display.update_session_total(self.sessions)
                self.display.tabs.select(1)
                self.start_timer()

        # Exercise Timer
        elif timer_id == 2:
            full_seconds = 60 * 3
            # For testing
            # full_seconds = 5
            workout = self.exercise.assign_workout()  # Assign workout
            self.display.update_workout_label(workout)  # Update display with the assigned workout
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.display.update_exer_timer_label(f"{minutes:02d}:{seconds:02d}")
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped:
                self.display.root.after(0, self.collect_reps)

        # Break Timer
        elif timer_id == 3:
            full_seconds = 60 * 7
            # For testing
            # full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.display.update_brk_timer_label(f"{minutes:02d}:{seconds:02d}")
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped:
                self.display.tabs.select(0)
                self.start_timer()

    def collect_reps(self):
        reps = self.exercise.completed_reps()
        self.update_reps_after_collection(reps)

    def update_reps_after_collection(self, reps):
        if self.exercise.current_workout not in self.display.exercise_reps:
            self.display.exercise_reps[self.exercise.current_workout] = 0
        self.display.exercise_reps[self.exercise.current_workout] += reps
        self.display.update_workout_label_with_reps(self.display.exercise_reps)
        self.display.tabs.select(2)
        self.start_timer()

    def reset_timer(self):
        self.stopped = True
        self.skipped = False
        self.sessions = 0
        self.display.update_prod_timer_label(text="25:00")
        self.display.update_exer_timer_label(text="3:00")
        self.display.update_brk_timer_label(text="7:00")
        self.display.clear_workout_label()
        self.display.exercise_reps.clear()
        self.running = False

    def skip_session(self):
        self.stopped = True
        self.running = False
        current_tab = self.display.tabs.index(self.display.tabs.select())
        if current_tab == 0:
            self.display.update_prod_timer_label(text="25:00")
        elif current_tab == 1:
            self.display.update_exer_timer_label(text="3:00")
        elif current_tab == 2:
            self.display.update_brk_timer_label(text="7:00")

    def set_display(self, display):
        self.display = display
