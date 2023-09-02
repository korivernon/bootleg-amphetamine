from pynput.mouse import Button, Controller
import time
import subprocess
import random
mouse = Controller()
import os
def zoom_running():
    process = subprocess.run(["ps", "-ef"], capture_output=True, shell=True)
    process_out = process.stdout.decode("utf-8")
    if "/Applications/zoom.us.app/Contents/Frameworks/CptHost.app/Contents/MacOS/CptHost" in process_out:
        return True

def run_mouse_move():
    while True:
        time.sleep(60)
        if zoom_running():
            continue
        #print('The current pointer position is {0}'.format(mouse.position))
        rand_x = random.randrange(-100,100)
        rand_y = random.randrange(-100,100)
        # Move pointer relative to current position
        mouse.move(rand_x,rand_y)
        #print('Now we have moved it to a new position {0}'.format(mouse.position))


run_mouse_move()
