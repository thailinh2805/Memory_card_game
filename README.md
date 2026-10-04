# Game Project

This project is a small game that I developed together with my teammates from Group 9 in the Engineering Mechanics Programming Techniques class in 2024. The game utilizes Pygame and features multiple screens: a start screen, settings, level selection, the main gameplay screen, and a game-over screen.

## Features
- Multiple game scenes and transitions
- Level-based gameplay flow
- Sound/music support
- Assets and scene management in separate modules

## Requirements
- Python 3.10+
- Pygame

## Setup
```bash
python -m pip install -r requirements.txt
```

## Run the game
```bash
python main.py
```

## Notes
- The main entry point is `main.py`.
- Game assets are stored in the `assets/` folder and scene logic is in the `scenes/` folder.
- If you want to make changes, start with the scene classes and the `SceneManager` in `main.py`.
