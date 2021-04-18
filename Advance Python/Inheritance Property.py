class User():
    def signIn(self):
        print("Logged In")


class Archer(User):
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def attck(self):
        print(f"Attacking with the power of {self.attack}")


class Wizard(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attck(self):
        print(f"Having arrow {self.arrow}")


wizard1 = Wizard("Paul", 23)
archers1 = Archer("Andrei", 100)

wizard1.attck()
archers1.attck()
