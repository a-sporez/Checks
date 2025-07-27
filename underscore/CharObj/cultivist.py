from character import Character
from FSM import State

class CombatState(State):
    def attack(self, move):
        player = Character("Bob", "fire", "plant", temperament=1)
        return ()