import re


def _iscdigit(val):
    vn = ord(val)
    return vn >= 0x30 and vn <= 0x39


def _isclow(val):
    vn = ord(val)
    return vn >= 0x61 and vn <= 0x7A


def _isxdigit(val):
    vn = ord(val)
    return (vn >= 0x30 and vn <= 0x39) or (vn >= 0x61 and vn <= 0x66)


# version parser that mirrors apk's
# we have a custom one so we can do validation better etc.
class Token:
    # token types
    INITIAL_DIGIT = 0
    DIGIT = 1
    LETTER = 2
    SUFFIX = 3
    SUFFIX_NO = 4
    COMMIT_HASH = 5
    REVISION_NO = 6
    END = 7
    INVALID = 8

    # suffixes
    SUFFIX_INVALID = 0
    SUFFIX_ALPHA = 1
    SUFFIX_BETA = 2
    SUFFIX_PRE = 3
    SUFFIX_RC = 4
    SUFFIX_NONE = 5  # delimits the higher and lower matching suffixes
    SUFFIX_CVS = 6
    SUFFIX_SVN = 7
    SUFFIX_GIT = 8
    SUFFIX_HG = 9
    SUFFIX_P = 10

    def __init__(self, ver):
        self.token = self.INITIAL_DIGIT
        self.input = ver
        if not self.extract_span(_iscdigit):
            self.token = self.INVALID
        else:
            self.number = int(self.value)

    def extract_span(self, fun):
        spanlen = 0
        for i in range(len(self.input)):
            if not fun(self.input[i]):
                break
            spanlen += 1
        if spanlen == 0:
            return False
        self.value = self.input[0:spanlen]
        self.input = self.input[spanlen:]
        return True

    def compare(self, otok):
        match self.token:
            case self.DIGIT:
                if self.value[0] == "0" or otok.value[0] == "0":
                    # string comparison for 0-prefixed nums, see apk version.c
                    if self.value == otok.value:
                        return "="
                    elif self.value < otok.value:
                        return "<"
                    else:
                        return ">"
                else:
                    aval = self.number
                    bval = otok.number
            case self.INITIAL_DIGIT | self.SUFFIX_NO | self.REVISION_NO:
                aval = self.number
                bval = otok.number
            case self.SUFFIX:
                aval = self.suffix
                bval = otok.suffix
            case self.LETTER:
                aval = ord(self.value[0])
                bval = ord(otok.value[0])
            case _:
                if self.value == otok.value:
                    return "="
                elif self.value < otok.value:
                    return "<"
                else:
                    return ">"
        # numerical comparison
        if aval < bval:
            return "<"
        elif aval > bval:
            return ">"
        return "="

    def next(self):
        # end of stream
        if len(self.input) == 0:
            self.token = self.END
            return
        # input letter
        inp = self.input[0]
        # letter
        if _isclow(inp):
            if self.token > self.DIGIT:
                self.token = self.INVALID
                return
            self.value = inp
            self.token = self.LETTER
            self.input = self.input[1:]
            return
        # suffix
        if inp == "_":
            if self.token > self.SUFFIX_NO or len(self.input) <= 1:
                self.token = self.INVALID
                return
            self.input = self.input[1:]
            # extract the value
            if not self.extract_span(_isclow):
                self.token = self.INVALID
                return
            # map the suffix value
            sufmap = {
                "alpha": self.SUFFIX_ALPHA,
                "beta": self.SUFFIX_BETA,
                "pre": self.SUFFIX_PRE,
                "rc": self.SUFFIX_RC,
                "cvs": self.SUFFIX_CVS,
                "svn": self.SUFFIX_SVN,
                "git": self.SUFFIX_GIT,
                "hg": self.SUFFIX_HG,
                "p": self.SUFFIX_P,
            }
            self.suffix = sufmap.get(self.value, self.SUFFIX_INVALID)
            if self.suffix == self.SUFFIX_INVALID:
                self.token = self.INVALID
            else:
                self.token = self.SUFFIX
            return
        # hash
        if inp == "~":
            if self.token >= self.COMMIT_HASH or len(self.input) <= 1:
                self.token = self.INVALID
                return
            self.input = self.input[1:]
            self.token = self.COMMIT_HASH
            # parse it...
            if not self.extract_span(_isxdigit):
                self.token = self.INVALID
            return
        # revision
        if inp == "-":
            if self.token >= self.REVISION_NO or not self.input.startswith(
                "-r"
            ):
                self.token = self.INVALID
                return
            self.input = self.input[2:]
            self.token = self.REVISION_NO
            if not self.extract_span(_iscdigit):
                self.token = self.INVALID
                return
            self.number = int(self.value)
            return
        # .
        if inp == ".":
            if self.token > self.DIGIT:
                self.token = self.INVALID
                return
            # fall through...
            self.input = self.input[1:]
        elif not _iscdigit(inp):
            self.token = self.INVALID
            return
        # number
        match self.token:
            case self.INITIAL_DIGIT | self.DIGIT:
                self.token = self.DIGIT
            case self.SUFFIX:
                self.token = self.SUFFIX_NO
            case _:
                self.token = self.INVALID
                return
        if not self.extract_span(_iscdigit):
            self.token = self.INVALID
            return
        self.number = int(self.value)


def version_validate(ver):
    tok = Token(ver)
    while tok.token < tok.END:
        tok.next()
    return tok.token == tok.END


def version_compare(vera, verb):
    toka = Token(vera)
    tokb = Token(verb)

    while toka.token == tokb.token and toka.token < Token.END:
        ret = toka.compare(tokb)
        if ret != "=":
            return ret
        toka.next()
        tokb.next()

    if toka.token == tokb.token:
        return "="

    if toka.token == Token.SUFFIX and toka.suffix < Token.SUFFIX_NONE:
        return "<"
    if tokb.token == Token.SUFFIX and tokb.suffix < Token.SUFFIX_NONE:
        return ">"

    if toka.token > tokb.token:
        return "<"
    if tokb.token > toka.token:
        return ">"

    return "="


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
    from cbuild.apk import cli

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


# test for version parser; pass test/unit/version.data as input
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("no test data given")
        sys.exit(1)

    code = 0

    with open(sys.argv[1]) as tdata:
        for ln in tdata:
            ln = ln.strip()
            if len(ln) == 0:
                continue
            if "#" in ln:
                ln = ln[0 : ln.find("#")].strip()
            lns = ln.split()
            if len(lns) == 1:
                if lns[0].startswith("!"):
                    if version_validate(lns[0][1:]):
                        print(f"FAIL {ln}")
                        code = 1
                elif not version_validate(lns[0]):
                    print(f"FAIL {ln}")
                    code = 1
            elif len(lns) != 3:
                print(f"malformed line '{ln}'")
            else:
                if "~" in lns[1]:
                    # we don't support fuzzy match here
                    continue
                if version_compare(lns[0], lns[2]) != lns[1]:
                    print(f"FAIL {ln}")

    sys.exit(code)
