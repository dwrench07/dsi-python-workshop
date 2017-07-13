class MyClass():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        print(f"{self.name} = {self.score}")

    def __repr__(self):
        return int()


my_instance = MyClass(name="Dave", score=10)

type(my_instance)
type(my_instance.__str__())
type(my_instance.__repr__())
my_instance.__str__()
my_instance.__repr__()
