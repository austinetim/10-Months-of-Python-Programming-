# THIS IS AN EXAMPLE OF HOW CLASS INHERITANCE WORKS

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

molly = Animal()
molly.breathe()

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

buzga = Fish()
buzga.breathe()
buzga.swim()
