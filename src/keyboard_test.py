from pynput.keyboard import Key, Listener, Controller
import os

def on_press(key):
    print("press one key")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    try:
        listener.wait()
    finally:
        listener.stop()

# os.system('clear')
Controller().press(Key.ctrl)
Controller().press('e')

Controller().release(Key.ctrl)
Controller().release('e')