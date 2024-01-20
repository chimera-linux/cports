import sys
import os


class Logger:
    def __init__(self, colors, ostream, estream):
        self.use_colors = colors
        self.ostream = ostream
        self.estream = estream
        self.fileno = ostream.fileno()

    def out_raw(self, msg):
        os.write(self.fileno, msg.encode())

    def out_plain(self, msg, end="\n"):
        self.ostream.write(msg)
        self.ostream.write(end)

    def out(self, msg, end="\n"):
        if self.use_colors:
            self.ostream.write("\033[1m")
        self.ostream.write("=> ")
        self.ostream.write(msg)
        if self.use_colors:
            self.ostream.write("\033[m")
        self.ostream.write(end)

    def warn(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[33m")
        self.estream.write("=> WARNING: ")
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)

    def out_red(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[31m")
        self.estream.write("=> ")
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)

    def out_green(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[32m")
        self.estream.write("=> ")
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)


def init(colors):
    global logger_inst
    logger_inst = Logger(colors, sys.stdout, sys.stderr)


def get():
    global logger_inst
    return logger_inst
