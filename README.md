# bootleg-amphetamine
I made this because for some reason my handy-ole [Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12) stopped working and became a pain. 
I figured I could just make my own, so I present to you: `bootleg-amphetamine`!

# Preface
_@my boss - If you are reading this, I work, I promise <3._

_Special thanks to [Granit](https://github.com/GranitG) for the Zoom idea._

# Setup
First, you want to install `pip install pynput`. This will 
allow you to use the module that we use to move the mouse. 

Next, you want to add the location of where the `move_mouse.py` file is in the `commands.sh` file.

Following this, you need to add the `commands.sh` file to be referenced in your `.zshrc` file.

Once all of this is done, you should be able to run:

- `nosleep`: this will prevent your machine from sleeping. You will notice that if you close your screen, it will still be on. 
- `allowsleep`: this will allow your machine to sleep and act as if nothing even happened :). 

