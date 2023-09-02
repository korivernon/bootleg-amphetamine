from pynput.mouse import Button, Controller
import time
import subprocess
import random
mouse = Controller()
while True:
    time.sleep(5)
    # print('The current pointer position is {0}'.format(mouse.position))
    rand_x = random.randrange(-1000, 1000)
    rand_y = random.randrange(-1000, 1000)
    # Move pointer relative to current position
    mouse.move(rand_x, rand_y)