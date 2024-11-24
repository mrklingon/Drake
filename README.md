# Drake
Calculate the Drake equation (https://en.wikipedia.org/wiki/Drake_equation) with a NeoTrinkey 

### Files
* drake.py - calculate the Drake equation- based on https://github.com/DeaconDesperado/pydrake
* sagan - Carl Sagan quotes
* wise.py - selects quotes to display
* prt.py - allows prt() to print to REPL or HID keyboard input

Copy the files to your NeoTrinkey running (renaming drake.py to "code.py").

Touch pad#1 for the NeoTrinkey to calculate and print out the estimate - since the factors are coded as ranges, you will get different answers every time. After presenting the calculations, the program will also give a random quote from Carl Sagan.

For fun, touching pad#2 will give a list of the names of the civilized planets - basically generating a random name for as many as the program calculated (plus Earth). Be aware that the number can be large and this will take a while.

Change REPL=False to REPL=True to have output go as if typed via the keyboard. 
