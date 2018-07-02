cars = []

class Car:

    def __init__(self, name, No_plate, seats):
        self._name = name
        self._No_plate = No_plate
        self._seats = seats
        self._available = True
        cars.append(self)

    def _Display(self):
        print("Car name: {}".format(self._name))
        print("Seats: {}".format(self._No_plate))
        print("Licence plate: {}".format(self._seats))

    def _hired(self):
        self._available = False
        print("car booked")

    def _returned(self):
        self._available = True
        print("car is returned")


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
            if c._available == True:
                print("----- Car: {}-----".format(counter))
                c._Display()
                counter += 1
            else:
                counter += 1
        while True:
            try:
                user_input = int(input())

                break
            except:
                print("please enter an interger corrisponding to a car")
        user_input -= 1
        cars[user_input]._Display()
        cars[user_input]._hired()
        main_menu()

    elif choice == 2:
        search()
    else:
        print("please enter an interger between 0 and 3")
        main_menu()


def search():
    while True:
        try:
            seats = int(input("how many seats would you like? "))
            break
        except:
            print("please enter an interger")
    counter = 1
    for x in cars:
        if x._seats == seats:
            print("------Car: {}-------".format(counter))
            x._Display()
            counter += 1
        else:
            counter += 1
    
    while True:
        try:
            seat_input = int(input("please enter a car: "))
            break
        except:
            print("please enter an interger")
    seat_input -= 1
    cars[seat_input]._Display()
    cars[seat_input]._hired()
    main_menu()

def Return():
    counter = 1
    for c in cars:
        if c._available == False:
            print("-------Car: {}--------".format(counter))
            c._Display
            counter += 1
        else:
            counter += 1
    while True:
        try:
            return_input = int(input("what car would you like return: "))
            break
        except:
            print("please enter an interger")
    return_input -= 1
    cars[return_input]._returned()
    main_menu()
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
    elif choice == 2:
        Return()
    else:
        print("please enter an interger between 0 and 3")
        main_menu()
Car("Ford", "233ybbh", 5)
Car("Ford", "233ybbh", 4)
Car("Ford", "233ybbh", 3)
Car("Ford", "233ybbh", 2)
main_menu()