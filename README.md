# backgammon_app
* This repo will, eventually, have a mobile app that allows a user to:
    1. take a photo of a backgammon board
    1. process and transform that image into a standardized format representing the position
    1. evaluate the board position to determine win expectancy for both parties
    1. evaluate point expectancy (as this can be a distinct value when taking into account gammon and backgammon likelihood)
    1. offer doubling advice
    1. provide the top n moves for a given roll from that position
* I am building this project to learn how to use and incorporate several of the component parts, so I welcome any and all advice and criticism

## Backgammon Programs
- [GNU Backgammon](https://www.gnu.org/software/gnubg/)
- [Extreme Gammon](https://www.extremegammon.com/)
- [bgammon.org](https://bgammon.org/)

## Repos
- [List of Repos in Python](https://github.com/topics/backgammon?l=python)

## Notation
- [Backgammon Notation](http://www.backgammon-play.net/GameNotation.htm)
- [Another example of a full notated game](https://www.backgammon-rules.com/how-to-read-backgammon-notation-game-transcription/)
- oddly difficult to find what the standard online notation is for the current board position if you don't have the move history. May need to create my own

## Incremental steps to proceed
1. build a function to take as input as series of backgammon moves from the beginning of a game and generate the resulting board position
    1. perhaps develop your own notation for storing current board state
2. build a function to evaluate the win expectancy of a given position
3. build a function to propose the best moves given a roll
4. Take a segmentation model and train it on images of backgammon positions
    1. get it to identify the checkers, bar, pieces that have been moved off the board, the points, the dice and the doubling cube
    2. create some process to take that set of info and write it out as board state
5. Combine these into a process that takes a photo of a backgammon board and outputs:
    1. the current position
    2. the win expectancy
    3. the point expectancy (given cube value and gammon potential)
    4. the correct doubling strategy
    5. the best move given the roll (if relevant)
6. Put this into an android app