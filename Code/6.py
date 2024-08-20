class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot is working")
