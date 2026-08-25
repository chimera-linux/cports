from cbuild.apk import cli

import re

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


def pkg_match(pname, ver, pattern):
    for i, c in enumerate(pattern):
        if c == "<" or c == ">" or c == "~" or c == "=":
            # names don't match
            if pname != pattern[0:i]:
                return False
            # strip the name
            pattern = pattern[i:]
            break
    else:
        return False

    if pattern[0:1] == ">":
        # foo>x<y
        sidx = pattern.find("<")
        if sidx > 0:
            if pattern[sidx : sidx + 2] in _valid_ops:
                sep2 = pattern[sidx : sidx + 2]
            else:
                sep2 = pattern[sidx : sidx + 1]
            cmpv = cli.compare_version(ver, pattern[sidx + len(sep2) :])
            # if version is greater, always return
            # for less than, also return if version is equal
            if cmpv > 0 or (sep2 == "<" and cmpv == 0):
                return False
            # strip the part of the check we did already
            pattern = pattern[:sidx]

    # split the operator
    if pattern[0:2] in _valid_ops:
        sep1 = pattern[0:2]
    else:
        sep1 = pattern[0:1]

    # and drop it from the rest of the check
    pattern = pattern.removeprefix(sep1)

    # lower limit comparison
    cmpv = cli.compare_version(ver, pattern)

    # fuzzy compare
    if sep1 == "~":
        # first, the prefix has to be the same
        if not ver.startswith(pattern):
            return False
        ver = ver[len(pattern) :]
        # second, what follows must be a new token
        # both versions are already guaranteed to be
        # in valid format thanks to compare_version
        return (len(ver) == 0) or (ver[0] in "-._")

    if sep1 == "<=" and cmpv > 0:
        return False
    elif sep1 == "<" and cmpv >= 0:
        return False
    elif sep1 == ">=" and cmpv < 0:
        return False
    elif sep1 == ">" and cmpv <= 0:
        return False
    elif sep1 == "=" and cmpv != 0:
        return False

    return True


_comp = None


def set_compression(comp):
    global _comp
    _comp = comp


def get_compression():
    return _comp
