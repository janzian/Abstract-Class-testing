from abstract import AbstractBaseClass as ab
from implement import ImplementsMethods as im

class ConcreteBaseClass(ab, im):

    def test(self):
        print("test1")
        self.method("This probably won't work")
        print("test2")
