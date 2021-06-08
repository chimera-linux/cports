# implements the same version comparison algorithm as xbps

from enum import Enum

mods = {
    "alpha": -3,
    "beta": -2,
    "pre": -1,
    "rc": -1,
    "pl": 0,
    ".": 0
}

class Version:
    def __init__(self, vers):
        self.components = []
        self.revision = 0

        while vers != None:
            vers = self.make_component(vers)

    def make_component(self, s):
        if len(s) == 0:
            return None

        diglen = 0
        for c in s:
            if not c.isdigit():
                break
            diglen += 1

        # number component
        if diglen > 0:
            self.components.append(int(s[0:diglen]))
            return s[diglen:]

        # known modifier
        for k in mods:
            if s[0:len(k)] == k:
                self.components.append(mods[k])
                return s[len(k):]

        # revision
        if s[0] == "_":
            revlen = 0
            for c in s[1:]:
                if not c.isdigit():
                    break
                revlen += 1
            if revlen > 0:
                self.revision = int(s[1:revlen + 1])
            return s[revlen + 1:]

        # other alphabetics undergo regular comparison
        if s[0].isalpha():
            # like a dot
            self.components.append(0)
            self.components.append(ord(s[0].lower()) - 96)

        return s[1:]

def compare(ver1, ver2):
    ver1 = Version(ver1)
    ver2 = Version(ver2)

    for i in range(max(len(ver1.components), len(ver2.components))):
        if len(ver1.components) > i:
            d1 = ver1.components[i]
        else:
            d1 = 0

        if len(ver2.components) > i:
            d2 = ver2.components[i]
        else:
            d2 = 0

        if d1 != d2:
            return d1 - d2

    return ver1.revision - ver2.revision

class Operator(Enum):
    LE = 0
    LT = 1
    GE = 2
    GT = 3
    EQ = 4
    NQ = 5

_ops = {
    "<=": Operator.LE,
    "<":  Operator.LT,
    ">=": Operator.GE,
    ">":  Operator.GT,
    "==": Operator.EQ,
    "!=": Operator.NQ
}

def _op_find(pat):
    global _ops
    opid = _ops.get(pat[0:2], None)
    if not opid:
        opid = _ops.get(pat[0], None)
        if not opid:
            return None, -1
        return opid, 1
    return opid, 2

def match(ver, pattern):
    veridx = ver.rfind("-")

    if veridx < 0:
        return False

    sepidx = -1
    for i, c in enumerate(pattern):
        if c == "<" or c == ">":
            sepidx = i
            break
    else:
        return False

    # name lengths don't match
    if veridx != sepidx:
        return False

    # names don't match
    if ver[0:veridx] != pattern[0:sepidx]:
        return False

    pattern = pattern[sepidx:]
    ver = ver[veridx + 1:]

    sep1, sep1l = _op_find(pattern)

    if sep1 == Operator.GT or sep1 == Operator.GE:
        sidx = pattern.find("<")
        if sidx > 0:
            sep2, sep2l = _op_find(pattern[sidx:])
            if not sep2:
                return False
            cmpv = compare(ver, pattern[sidx + sep2l:])
            # if version is greater, always return
            if cmpv > 0:
                return False
            # for less-than, also return if version is equal
            if sep2 == Operator.LT and cmpv == 0:
                return False
            # substring the version for lower limit cmp
            pattern = pattern[sep1l:sidx]
    else:
        pattern = pattern[sep1l:]

    # lower limit comparison
    cmpv = compare(ver, pattern)

    if sep1 == Operator.LE and cmpv > 0:
        return False
    elif sep1 == Operator.LT and cmpv >= 0:
        return False
    elif sep1 == Operator.GE and cmpv < 0:
        return False
    elif sep1 == Operator.GT and cmpv <= 0:
        return False
    elif sep1 == Operator.EQ and cmpv != 0:
        return False
    elif sep1 == Operator.NQ and cmpv == 0:
        return False

    return True
