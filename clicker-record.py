"""
A simple mouse logger that logs mouse clicks to a file.

This script will log mouse clicks to a file named "mouse_log.txt" in the
current working directory. Each click is logged as "x,y" where x and y are
the coordinates of the click.

The script will exit when the escape key is pressed.

"""
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key
from colorama import Fore, Style, init
import time
# Initialize colorama
init(autoreset=True)

# Header
print(Fore.CYAN + "===============================")
print(Fore.RED + "        MOUSE CLICK LOGGER")
print(Fore.CYAN + "===============================")
print(Fore.YELLOW + "Press 'esc' to quit.")

# List to store the clicked positions
click_positions = []
exit = False
def on_click(x, y, button, pressed):
    """Log mouse clicks."""

    if exit:
        return False
    else:
        if pressed:
            print(Fore.GREEN + f"Click logged: ({x}, {y}, {button})")
            click_positions.append((x, y, str(button)))

def on_press(key):
    global exit
    """Exit the program when the escape key is pressed."""
    if key == Key.esc:
        # Save to file
        with open("mouse_log.txt", "w") as file:
            for pos in click_positions:
                file.write(f"{pos[0]},{pos[1]},{pos[2]}\n")
        print(Fore.YELLOW + "Click positions saved to 'mouse_log.txt' file.")
        time.sleep(0.5)
        print(Fore.RED + "You can close this program now.")
        exit = True
        return False

if __name__ == "__main__":
    # Start the mouse and keyboard listeners

    with Listener(on_click=on_click) as mouse_listener, \
    KeyboardListener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()
