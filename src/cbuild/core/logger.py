import sys
import os
import datetime


class Logger:
    def __init__(self, colors, timing, ostream, estream):
        self.use_colors = colors
        self.ostream = ostream
        self.estream = estream
        self.fileno = ostream.fileno()
        self.timing = timing
        self.time = datetime.datetime.now()

    def out_raw(self, msg):
        os.write(self.fileno, msg.encode())

    def _out_arrow(self, stream):
        if self.timing:
            ntime = datetime.datetime.now()
            stream.write(f"{ntime - self.time} ")
        stream.write("=> ")

    def out_plain(self, msg, end="\n"):
        self.ostream.write(msg)
        self.ostream.write(end)

    def out(self, msg, end="\n"):
        if self.use_colors:
            self.ostream.write("\033[1m")
        self._out_arrow(self.ostream)
        self.ostream.write(msg)
        if self.use_colors:
            self.ostream.write("\033[m")
        self.ostream.write(end)

    def out_orange(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[33m")
        self._out_arrow(self.estream)
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)

    def warn(self, msg, end="\n"):
        self.out_orange(f"WARNING: {msg}", end)

    def out_red(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[31m")
        self._out_arrow(self.estream)
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)

    def out_green(self, msg, end="\n"):
        if self.use_colors:
            self.estream.write("\033[1m\033[32m")
        self._out_arrow(self.estream)
        self.estream.write(msg)
        if self.use_colors:
            self.estream.write("\033[m")
        self.estream.write(end)


def init(colors, timing):
    global logger_inst
    logger_inst = Logger(colors, timing, sys.stdout, sys.stderr)


def get():
    global logger_inst
    return logger_inst
