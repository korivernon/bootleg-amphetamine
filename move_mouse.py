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

def run_mouse_move(run_time=None, interval = 60):
    t = time.time()
    interval = int(interval)
    while True:
        if run_time == None:
            pass
        else:
            curr_time = time.time()
            time_running = curr_time - t
            # print(f"Running for {time_running}s!")
            if time_running > run_time:
                break
        time.sleep(interval)
        if zoom_running(): # you don't want your mouse to be moving on zoom !
            continue
        else:
            rand_x = random.randrange(-100,100)
            rand_y = random.randrange(-100,100)
            # Move pointer relative to current position
            mouse.move(rand_x,rand_y)
            # print("moving mouse!")
            # print('Now we have moved it to a new position {0}'.format(mouse.position))


def main():
    import argparse
    from termcolor import colored, cprint
    from pyfiglet import Figlet

    parser = argparse.ArgumentParser(description="My script description")

    # Define argument -r for runtime in seconds (optional)
    parser.add_argument("-r", "--runtime", type=int, help="Runtime of the script in seconds")
    parser.add_argument("-i", "--interval", type=int, default=60, help="Interval between actions in seconds")

    # Parse arguments
    args = parser.parse_args()

    # Check if runtime argument is provided
    if args.runtime:
        runtime = args.runtime
        runtime_seconds = args.runtime
        # print(f"\nRunning for {runtime_seconds} seconds.")
    else:
        runtime = 'Indefinite'
    # print(f"Interval set at {runtime_seconds} seconds.")
    print('\n')
    f = Figlet(font='colossal')
    print(colored(f.renderText(f'MoveMove'), 'green'))
    cprint(f"        - Move Mouse ~ Interval: {args.interval}s ~ Runtime: {runtime}s -        ", "green")

    run_mouse_move(args.runtime, args.interval)

if __name__ == '__main__':
    main()