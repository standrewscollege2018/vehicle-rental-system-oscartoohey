cars = []

class Car:

    def __init__(self, name, No_plate, seats):
        self._name = name
        self._No_plate = No_plate
        self._seats = seats

        cars.append(self)

    def _Display(self):
        print("Car name: {}".format(self._name))
        print("Seats: {}".format(self._No_plate))
        print("Licence plate: {}".format(self._seats))


def Hire():
    print("1. Show all Vehicles \n2. search by seats")
    while True:
        try:
            choice = int(input())
            break
        except:
            print("please enter an integer")
    if choice == 1:
        counter = 1
        for c in cars:
            print()
            c._Display()
        input

    else:
        search()
    
    
def main_menu():
    print("1. Hire vehicle \n2. Return vehicle")
    while True:
        try:
            choice = int(input())
            break
        except:
            print("please enter an integer")
    if choice == 1:
        Hire()
    else:
        Return()
    
Car("Ford", "233ybbh", 5)
Car("Ford", "233ybbh", 4)
Car("Ford", "233ybbh", 3)
Car("Ford", "233ybbh", 2)
main_menu()