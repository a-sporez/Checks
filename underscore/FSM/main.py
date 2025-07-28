from blessed import Terminal
from fsm import FSM
from states.intro import IntroState
from states.menu import MenuState
from states.running import RunningState

term = Terminal()

def main():
    # Register states and load intro.
    fsm = FSM()
    fsm.register('intro', IntroState())
    fsm.register('menu', MenuState())
    fsm.register('running', RunningState())
    fsm.change('menu')

    while True:
        fsm.render()
        user_input = term.inkey()
        result = fsm.handle_input(user_input.name or user_input)

        if isinstance(result, str):
            if result == 'quit':
                break
            fsm.change(result)
        fsm.update()

if __name__ == '__main__':
    main()