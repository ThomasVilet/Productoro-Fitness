
from Scripts.timer import Timer
from Scripts.display import Generate
from Scripts.exercise import Exercise

if __name__ == "__main__":
    exercise = Exercise()
    timer = Timer(exercise)
    app = Generate(timer)