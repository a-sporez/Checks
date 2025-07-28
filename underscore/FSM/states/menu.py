from fsm import State
from blessed import Terminal

term = Terminal()

class MenuState(State):
    def __init__(self):
        self.options = ["Start Game", "Options", "Quit"]
        self.index = 0

    def enter(self, **kwargs):
        print(term.clear)
        print(term.bold_underline("Main Menu"))

    def handle_input(self, user_input):
        if user_input in ['KEY_DOWN', 's']:
            self.index = (self.index + 1) % len(self.options)
        elif user_input in ['KEY_UP', 'w']:
            self.index = (self.index + 1) % len(self.options)
        elif user_input in ['\n', 'KEY_ENTER', 'enter']:
            selected = self.options[self.index]
            if selected == "Start Game":
                return 'running'
            elif selected == "Quit":
                return 'quit'
        
    def update(self):
        pass

    def render(self):
        print(term.clear)
        print(term.bold_underline("Main Menu"))
        for i, option in enumerate(self.options):
            if i == self.index:
                print(term.reverse(f'> {option}'))
            else:
                print(f' {option}')