"""
Repeat mouse clicks at specified intervals.

This script will repeat mouse clicks at specified intervals. You can specify the
number of times to repeat the clicks, the time between each click and the time
between each set of clicks.

Example:
    python clicker.py

    How many times do you want to repeat the clicks? 5
    How many seconds between each click? 1
    How many seconds between each set of clicks? 2

    The script will then repeat the mouse clicks 5 times with 1 second between
    each click and 2 seconds between each set of clicks.

"""

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener as KeyboardListener, Key
import time
from colorama import Fore, Style, init

init(autoreset=True)
exit_ = False

mouse = Controller()
def get_user_input():
    """Get user input for number of repeats, time between clicks and time between sets of clicks."""
    while True:
        try:
            repeat_count = int(input(Fore.YELLOW + "How many times do you want to repeat the clicks? "))
            time_out = int(input(Fore.YELLOW + "How many seconds between each click? "))
            repeat_frequency = int(input(Fore.YELLOW + "How many seconds between each set of clicks? "))
            return repeat_count, time_out, repeat_frequency
        except ValueError:
            print(Fore.RED + "Invalid input. Please try again.")
            continue


def load_mouse_positions():
    """Load mouse positions from file."""
    positions = []
    with open("mouse_log.txt", "r") as file:
        for line in file.readlines():
            x, y, button = line.strip().split(',')

            positions.append((int(x), int(y),str(button)))
    print(Fore.GREEN + f"Loaded {len(positions)} mouse positions from file.")
    return positions


def perform_clicks(positions, repeat_count, time_out, repeat_frequency):

    """Perform mouse clicks at specified intervals."""
    for i in range(repeat_count):
        print(Fore.MAGENTA + f"\n{i+1}. set of clicks starting...")
        print(positions)
        for pos in positions:
            mouse.position = (pos[0], pos[1])
            if 'left' in pos[2]:
                if exit_:
                    print(Fore.RED+ "\nexiting...")
                    time.sleep(2)
                    exit()
                mouse.click(Button.left, 1)  # Left clickqqq
                print(Fore.CYAN + f"Left click at ({pos[0]}, {pos[1]})")
                time.sleep(time_out)  # Wait between clicks
            elif 'right' in pos[2]:
                if exit_:
                    print(Fore.RED+ "\nexiting...")
                    time.sleep(2)
                    exit()
                mouse.click(Button.right, 1)  # Right click
                print(Fore.CYAN + f"Right click at ({pos[0]}, {pos[1]})")
                time.sleep(time_out)  # Wait between clicks
        if not exit_:
            print(Fore.CYAN + f"{i+1}. set of clicks completed.")
            time.sleep(repeat_frequency)  # Wait between sets of clicks

    print(Fore.GREEN + "\nAll clicks completed.")
    print(Fore.RED+ "\nexiting...")
    time.sleep(2)
    exit()

def on_press(key):
    global exit_
    """Stop script on 'esc' key press."""
    if key == Key.esc:
        print(Fore.YELLOW + "Stopping script.")
        exit_ = True
        return False  # Stop listener

if __name__ == "__main__":
    repeat_count, time_out, repeat_frequency = get_user_input()
    positions = load_mouse_positions()
    with KeyboardListener(on_press=on_press) as listener:
        perform_clicks(positions, repeat_count, time_out, repeat_frequency)
        listener.join()
