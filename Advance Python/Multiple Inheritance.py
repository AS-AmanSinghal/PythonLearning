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


class HybridBrog(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, arrows)
        Archer.__init__(self, name, power)


hb1 = HybridBrog("AMAN", 40, 20)
print(hb1.attck())
print(hb1.signIn())

wizard1 = Wizard("Paul", 23)
archers1 = Archer("Andrei", 100)

wizard1.attck()
archers1.attck()
