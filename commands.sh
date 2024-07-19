function nosleep { # this will prevent your machine from sleeping and move the mouse
     sudo -S <<< "YOUR PASSWORD" pmset disablesleep 1 # this disables display sleep when closed
     python3 ~/PATH TO DIRECTORY/mouse_move/move_mouse.py $* & # this is the mouse jiggler
     caffeinate -d & # this disables your machine from sleeping
 }

function allowsleep { # this will allow your machine to sleep and move your mouse
     sudo -S <<< "YOUR PASSWORD" pmset disablesleep 0 # this re-allows sleep
     pkill -f "caffeinate -d" # THIS WILL KILL ALL OF THE caffeinate -d PROCESSES
     pkill -f "move_mouse.py" # THIS WILL KILL THE MOVE MOUSE SCRIPT
}
