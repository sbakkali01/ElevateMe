from elevator import Elevator
from person import Person


if __name__ == '__main__':
    elevator=Elevator()
    print(elevator,"\n")
    person1=Person(1,2)
    print(person1,"\n")
    elevator.lift_person(person1)
    print(elevator,"\n")
    print(person1)

