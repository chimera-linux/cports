from cbuild.apk import cli

from enum import Enum

import re


def strip_tar_endhdr(data):
    tlen = len(data)
    # length of the initial archive without trailing headers
    dlen = 0
    dbeg = 0
    while True:
        # this should not happen though
        if (tlen - dlen) < 512:
            break
        # try if there's a name
        hname = data[dbeg : dbeg + 100]
        # trailing header
        if hname[0] == 0:
            break
        # header size
        dlen += 512
        # data size, if any
        szb = data[dbeg + 124 : dbeg + 136].rstrip(b"\x00")
        if len(szb) > 0:
            # align to 512
            dlen += (int(szb, 8) + 511) & ~511
        # new header start
        dbeg = dlen

    return data[0:dlen]


_valid_ops = {
    "<=": True,
    "<": True,
    ">=": True,
    ">": True,
    "=": True,
    "~": True,
}


def split_pkg_name(s):
    found = re.search(r"[><=~]", s)
    if not found:
        return None, None, None

    sn = s[: found.start()]
    sv = s[found.start() :]

    if len(sn) == 0:
        return None, None, None

    for i in range(len(sv)):
        if sv[i].isdigit():
            op = sv[0:i]
            if op not in _valid_ops:
                return None, None, None
            return sn, sv[i:], op

    return None, None, None


class Operator(Enum):
    LE = 0
    LT = 1
    GE = 2
    GT = 3
    EQ = 4
    EF = 5


_ops = {
    "<=": Operator.LE,
    "<": Operator.LT,
    ">=": Operator.GE,
    ">": Operator.GT,
    "=": Operator.EQ,
    "~": Operator.EF,
}


def _op_find(pat):
    opid = _ops.get(pat[0:2], None)
    if not opid:
        opid = _ops.get(pat[0], None)
        if not opid:
            return None, -1
        return opid, 1
    return opid, 2


def get_namever(pkgp):
    # maybe version dash
    fdash = pkgp.find("-")
    # invalid ver (ver should be FOO-VER-rREV)
    if fdash < 0:
        return None, None
    # maybe revision dash
    sdash = pkgp.find("-", fdash + 1)
    # invalid ver again
    if sdash < 0:
        return None, None
    # now get rid of any remaining dashes
    while True:
        ndash = pkgp.find("-", sdash + 1)
        if ndash < 0:
            break
        fdash = sdash
        sdash = ndash
    # and return name/ver
    return pkgp[0:fdash], pkgp[fdash + 1 :]


def pkg_match(ver, pattern):
    sepidx = -1

    for i, c in enumerate(pattern):
        if c == "<" or c == ">" or c == "~" or c == "=":
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
    ver = ver[sepidx + 1 :]

    sep1, sep1l = _op_find(pattern)

    if sep1 == Operator.GT or sep1 == Operator.GE:
        sidx = pattern.find("<")
        if sidx > 0:
            sep2, sep2l = _op_find(pattern[sidx:])
            if not sep2:
                return False
            cmpv = cli.compare_version(ver, pattern[sidx + sep2l :])
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
    cmpv = cli.compare_version(ver, pattern)

    # fuzzy compare
    if sep1 == Operator.EF:
        # first, the prefix has to be the same
        if not ver.startswith(pattern):
            return False
        ver = ver[len(pattern) :]
        # second, what follows must be a new token
        # both versions are already guaranteed to be
        # in valid format thanks to compare_version
        return (len(ver) == 0) or (ver[0] in "-._")

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


_comp = None


def set_compression(comp):
    global _comp
    _comp = comp


def get_compression():
    return _comp
