import ctypes
import getopt
import subprocess
import sys
import time
from sys import platform

import progressbar


def show_timer(amount_in_sec):
    widgets = [
        ' [', progressbar.Timer(), '] ',
        progressbar.Bar(),
        ' (', progressbar.ETA(), ') ',
    ]
    for i in progressbar.progressbar(range(amount_in_sec), widgets=widgets):
        time.sleep(1)


def show_popup():
    if platform == "linux" or platform == "linux2":
        subprocess.run(["notify-send", "-u", "normal", "-t", "5000", "Countdown", "The time is over!"], check=True)
    elif platform == "win32":
        ctypes.windll.user32.MessageBoxW(0, "The time is over!", "Countdown", 1)
    else:
        print("Unsupported OS")


def main(argv):
    amount_in_sec = 60

    try:
        opts, args = getopt.getopt(argv, "hs:", ["seconds="])
    except getopt.GetoptError:
        print('timer.py -s 120')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('timer.py -s 120')
            sys.exit()
        elif opt in ("-s", "--seconds"):
            amount_in_sec = int(arg)
        else:
            print('timer.py -s 120')
            sys.exit(2)

    show_timer(amount_in_sec)
    show_popup()


if __name__ == '__main__':
    main(sys.argv[1:])
