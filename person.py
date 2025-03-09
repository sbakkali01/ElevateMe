from __future__ import annotations

class Person:
    current_floor=None
    direction:int=None

    def __init__(self,current_floor,direction):
        self.current_floor=current_floor
        self.direction=direction

    def __str__(self):
        return f"The person is currently at the floor : {self.current_floor} and is going to floor : {self.direction}"

    def call_elevator(self,elevator:Elevator):
        elevator.current_floor=self.current_floor
