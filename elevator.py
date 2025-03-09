from __future__ import annotations


class Elevator:
    min_floor=0
    max_floor=4
    # capacity=1
    current_floor=None

    def __init__(self):
        self.current_floor=0

    def lift_person(self, person : Person):
        # assert self.current_floor==person.current_floor
        self.current_floor=person.direction
        person.current_floor=person.direction

    def __str__(self):
        return f"The elevator is currently at the floor : {self.current_floor}"
