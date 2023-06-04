# MC-Reaction-Solver
## Designed for InsanityCraft
A simple Python program to automatically solve word challenges on various Minecraft servers. Practically undetectable, and especially, free.

## Supported Challenges
- `Type Word` Challenges
- `Solve Expression` Challenges
  - Variable delay for multiplication expressions
- `Unscramble Word` Challenges
  - Checks against file of words
  - Automatically adds unseen words to file

## Auto-Open Window
- Will automatically open the Minecraft window when the reactions happens.

## Configurable Delays
- `UNSCRAMBLE_MIN_DELAY` - **minimum** delay for unscramble challenges in seconds
- `UNSCRAMBLE_MAX_DELAY` - **maximum** delay for unscramble challenges in seconds
- `TYPE_MIN_DELAY` - **minimum** delay for type challenges in seconds
- `TYPE_MAX_DELAY` - **minimum** delay for type challenges in seconds
- `SOLVE_MIN_DELAY` - **minimum** delay for solve challenges in seconds
- `SOLVE_MAX_DELAY` - **minimum** delay for solve challenges in seconds
- `SOLVE_MULTIPLY_MULTIPLIER` - The `min` and `max` delay for solve expression challenges is multiplied by this number

# How to Install
- download the repository
- check you have the latest version of Python installed
- Opem cmd in that directory you installed
- run `py main.py`
- success
