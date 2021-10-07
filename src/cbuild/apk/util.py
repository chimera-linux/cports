from cbuild.core import version

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
        hname = data[dbeg:dbeg + 100]
        # trailing header
        if hname[0] == 0:
            break
        # header size
        dlen += 512
        # data size, if any
        szb = data[dbeg + 124:dbeg + 136].rstrip(b"\x00")
        if len(szb) > 0:
            # align to 512
            dlen += (int(szb, 8) + 511) & ~511
        # new header start
        dbeg = dlen

    return data[0:dlen]

_valid_ops = {
    "<=": True,
    "<":  True,
    ">=": True,
    ">":  True,
    "=":  True,
}

def split_pkg_name(s):
    found = re.search(r"[><=]", s)
    if not found:
        return None, None, None

    sn = s[:found.start()]
    sv = s[found.start():]

    if len(sn) == 0:
        return None, None, None

    for i in range(len(sv)):
        if sv[i].isdigit():
            op = sv[0:i]
            if not op in _valid_ops:
                return None, None, None
            return sn, sv[i:], op

    return None, None, None

def pkg_match(pkgv, pattern):
    return version.match(pkgv, pattern)
