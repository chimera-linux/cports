import sys
import os
import re
import datetime

_colorstr = {
    "bold": "1",
    "black": "30",
    "red": "31",
    "green": "32",
    "orange": "33",
    "blue": "34",
    "purple": "35",
    "cyan": "36",
    "white": "37",
}


def _replf(m):
    mstr = m.group(1)
    if len(mstr) == 0:
        cols = []
    else:
        cols = [*map(lambda v: _colorstr[v], mstr.split(","))]
    return f"\033[{';'.join(cols)}m"


# just strip the escape
def _replf_nocolor(m):
    return ""


def write_color(stream, use_colors, msg):
    stream.write(
        re.sub(
            r"\f\[([a-z,]*)\]", _replf if use_colors else _replf_nocolor, msg
        )
    )


class Logger:
    def __init__(self, colors, timing, ostream):
        self.use_colors = colors
        self.ostream = ostream
        self.fileno = ostream.fileno()
        self.timing = timing
        self.time = datetime.datetime.now()

    def out_raw(self, msg):
        os.write(self.fileno, msg.encode())

    def out_stream(self, msg):
        write_color(self.ostream, self.use_colors, msg)

    def _out_arrow(self, stream):
        self.out_stream("\f[purple]")
        if self.timing:
            ntime = datetime.datetime.now()
            tdiff = ntime - self.time
            msec = tdiff.microseconds
            ntdiff = datetime.timedelta(
                tdiff.days, tdiff.seconds, round(msec / 1000) * 1000
            )
            # we can't :-3 because the input may be variable length
            dstr = str(ntdiff)[0:11]
            # pad with zeroes to make up full timestamp...
            if len(dstr) < 11:
                dstr += "0" * (11 - len(dstr))
            # just in case lol
            self.out_stream(f"{dstr[0:7]}.{dstr[8:]} ")
        self.out_stream("\f[bold]=> \f[]\f[bold]")

    def out_plain(self, msg, end="\n"):
        self.out_stream(msg)
        self.out_stream(end)

    def out(self, msg, end="\n"):
        self._out_arrow(self.ostream)
        self.out_stream(msg)
        self.out_stream(f"\f[]{end}")


def init(colors, timing):
    global logger_inst
    logger_inst = Logger(colors, timing, sys.stdout)


def get():
    global logger_inst
    return logger_inst
