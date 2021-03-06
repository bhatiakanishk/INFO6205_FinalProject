# The Menace
Final Project for INFO 6205

## Team Members
Raj Mehta (NUID): 001094914

Kanishk Bhatia (NUID): 001580259

## System Requirements
```
 pip install python3
```
## Running the game
a) Clone the repo
```
git clone https://github.com/bhatiakanishk/INFO6205_FinalProject.git
```

b) Go to the cloned repository
```
cd INFO6205_FinalProject
```

c) Go to the main directory
```
cd main
```

d) Run the program
```
python3 main.py
```
## Running the tests

a) Go to the cloned repository
```
cd INFO6205_FinalProject
```

b) Run the unittest
```
python -m unittest
```
## Requirements for the Project
a) Implement "The Menace" by replacing the matchboxes with values in a dictionary.

b) Train the Menace by running games played against "human" strategy, which is based upon optimal strategy.

c) You will need to choose values for:

    • alpha (the number of "beads" to in each "matchbox" at the start of the game—may be different for each move)
    
    • beta (the number of "beads" to add to the "matchbox" in the event of a win)
    
    • gamma (the number of "beads" to take to the "matchbox" in the event of a loss)
    
    • delta (the number of "beads" to add to the "matchbox" in the event of a draw)
    
d) Implement logging with date/time, win/loss/draw, and p.

e) Run unit tests, showing the date/time.

