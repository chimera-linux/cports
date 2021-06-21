# implements the version comparison algorithm for apk

from enum import Enum

suffixes = {
    "_alpha": -3,
    "_beta":  -2,
    "_pre":   -1,
    "_rc":    -1,
    "_cvs":   float("inf"),
    "_svn":   float("inf"),
    "_git":   float("inf"),
    "_hg":    float("inf"),
    "_p":     float("inf"),
}

class Version:
    def __init__(self, vers):
        self.components = []
        self.revision = 0

        # always need at least one version
        fdig, vers = self.parse_num(vers)
        if fdig == None:
            raise Exception("invalid version")
        self.components.append(fdig)

        # can be followed by any sequence of .<number>
        while len(vers) > 0 and vers[0] == ".":
            numv, vers = self.parse_num(vers[1:])
            if numv == None:
                raise Exception("invalid version")
            self.components.append(0)
            self.components.append(numv)

        # can be followed by a bunch of alphanumerics
        for i in range(len(vers)):
            if not vers[i].isalnum():
                vers = vers[i:]
                break
            # like an implied dot
            self.components.append(0)
            self.components.append(ord(vers[i].lower()) - 96)

        # can be followed by one or more known suffixes
        while len(vers) > 0 and vers[0] == "_":
            for sfx in suffixes:
                if vers.startswith(sfx):
                    self.components.append(suffixes[sfx])
                    vers = vers[len(sfx):]
                    break
            else:
                # bad suffix
                raise Exception("invalid version")

        # revision
        if vers[0:2] == "-r":
            revlen = 0
            for c in vers[2:]:
                if not c.isdigit():
                    break
                revlen += 1
            if revlen == 0:
                raise Exception("invalid version")
            self.revision = int(vers[2:revlen + 2])
            vers = vers[revlen + 2:]
        else:
            self.revision = 0

        # anything left is bad
        if len(vers) > 0:
            raise Exception("invalid version")

    def parse_num(self, s):
        if len(s) == 0:
            return None, s

        diglen = 0
        for c in s:
            if not c.isdigit():
                break
            diglen += 1

        if diglen == 0:
            return None, s

        return int(s[0:diglen]), s[diglen:]

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

_ops = {
    "<=": Operator.LE,
    "<":  Operator.LT,
    ">=": Operator.GE,
    ">":  Operator.GT,
    "=":  Operator.EQ
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
    sepidx = -1

    for i, c in enumerate(pattern):
        if c == "<" or c == ">" or c == "=":
            sepidx = i
            break
    else:
        return False

    # ver must be foo-VERSION where foo matches pattern before the operator
    if len(ver) <= sepidx or ver[sepidx] != "-":
        return False

    # names don't match
    if ver[0:sepidx] != pattern[0:sepidx]:
        return False

    pattern = pattern[sepidx:]
    ver = ver[sepidx + 1:]

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

    return True
