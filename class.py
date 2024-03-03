class Classno:
    def __init__(self):
        self.veselo = 0

    def sdelat_veselo(self):
        self.veselo += 1


class Man:
    def __init__(self):
        self.age = int(input("Type your age: "))

    def a(self):
        print("You are adult!" if self.age >= 18 else "You are not adult(")


Tom = Classno()
Tom.sdelat_veselo()
print("Tom veseliy" if Tom.veselo else "Tom grustniy")

Bob = Man()
Bob.a()
