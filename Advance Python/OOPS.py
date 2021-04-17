class PlayerCharacter:
    # class object Attribute
    membership = True

    def __init__(self, name):  # just like constructor
        self.name = name  # attributes

    def run(self):  # custom functions
        print("Run")

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("AMAN")
print(player1.name)
player2 = PlayerCharacter("SINGHAL")
print(player2.name)
print(player2.run())  # it will give None because this function didn't return anything. If return then print that value
print(player2.shout())
