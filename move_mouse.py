from pynput.mouse import Button, Controller
import time
import subprocess
import random
mouse = Controller()
import os
def zoom_running():
    # this will check to see if there is a zoom client already running
    # you can have a zoom window up, however, this criteria will not be met if you are in a zoom meeting
    process = subprocess.run(["ps", "-ef"], capture_output=True, shell=True)
    process_out = process.stdout.decode("utf-8")
    if "/Applications/zoom.us.app/Contents/Frameworks/CptHost.app/Contents/MacOS/CptHost" in process_out:
        return True

def run_mouse_move():
    while True:
        time.sleep(60)
        if zoom_running(): # you don't want your mouse to be moving on zoom !
            continue
        #print('The current pointer position is {0}'.format(mouse.position))
        rand_x = random.randrange(-100,100)
        rand_y = random.randrange(-100,100)
        # Move pointer relative to current position
        mouse.move(rand_x,rand_y)
        #print('Now we have moved it to a new position {0}'.format(mouse.position))


run_mouse_move()
