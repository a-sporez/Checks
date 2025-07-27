# bootstrap application
import sys
import os

# Add game folder to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_DIR = os.path.join(BASE_DIR, 'underscore')
sys.path.insert(0, GAME_DIR)

# entry stub
from .FSM.main import main

if __name__ == '__main__':
    main()