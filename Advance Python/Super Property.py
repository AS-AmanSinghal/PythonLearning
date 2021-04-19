class User():
    def __init__(self, email):
        self.email = email

    def signIn(self):
        print("Logged In")


class Archer(User):
    def __init__(self, name, attack, email):
        super().__init__(email)
        self.name = name
        self.attack = attack

    def attck(self):
        print(f"Attacking with the power of {self.attack}")


class Wizard(User):
    def __init__(self, name, arrow, email):
        super().__init__(email)
        self.name = name
        self.arrow = arrow

    def attck(self):
        print(f"Having arrow {self.arrow}")


wizard1 = Wizard("Paul", 23, "paul@gmail.com")
archers1 = Archer("Andrei", 100, "anderi@gmail.com")

wizard1.attck()
archers1.attck()
print(wizard1.email)
