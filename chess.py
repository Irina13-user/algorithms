from random import randint
outcome = ["win", "draw", "lose"]
class ChessPlayer:
    def __init__(self, name):#конструктор (как создавать экземпляр)
        self.name = name
        self.points = 0
        self.previous = None
        self.next = None

    def __repr__(self):#как выводить информацию
        return f"Имя: {self.name}, количество очков: {self.points}"

    def add_points(self, result):
        if result == "win":
            self.points += 1
        elif result == "draw":
            self.points += 0.5
def game(p1, p2):
    result = outcome[randint(0,2)]
    if result == "win":
        p1.add_points(result)
    elif result == "draw":
        p1.add_points(result)
        p2.add_points(result)
    else:
        p2.add_points(outcome[0])

def swap(p):
    current = p.previous
    while current and current.points <= p.points:
        current = current.previous
    if current:
        p1 = current.next
        p2 = p.next
        p3 = p.previous
        p.next = p1
        p.previous = current
        current.next = p
        p1.previous = p
        p2.previous = p3
        p3.next = p2
    else:
        p1 = leader
        p2 = p.next
        p3 = p.previous
        p.previous = None
        p.next = p1
        p1.previous = p
        p2.previous = p3
        p3.next = p2


p1 = ChessPlayer("Piter")
p2 = ChessPlayer("Mary")
p3 = ChessPlayer("Noah")
p4 = ChessPlayer("Oliver")

leader = p1
p1.next = p2
p2.previous = p1
p2.next = p3
p3.previous = p2
p3.next = p4
p4.previous = p3
