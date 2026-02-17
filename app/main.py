import threading
from gui import start_gui
from bot import run_bot

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()
    start_gui()
