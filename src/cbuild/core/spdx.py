import json

_opprec = {
    "OR": 1,
    "AND": 2,
}

_license_inst = {
    "BSL-1.0": True,
    "ISC": True,
    "NCSA": True,
    "X11": True,
    "X11-distribute-modifications-variant": True,
}


# not exhaustive but should catch common cases
def _license_install(lic):
    if lic in _license_inst:
        return True
    if lic.startswith("AGPL-"):
        return True
    if lic.startswith("BSD-"):
        return True
    if lic.startswith("MIT"):
        return True
    if lic.startswith("OFL"):
        return True
    return False


class SPDXParser:
    def __init__(self, spath):
        self.ldict = {}
        self.edict = {}

        def _license_parse(v):
            # ignore deprecated names, they should never pass
            if v.get("isDeprecatedLicenseId"):
                return
            if "licenseId" in v:
                self.ldict[v["licenseId"]] = v

        def _exception_parse(v):
            # ditto
            if v.get("isDeprecatedLicenseId"):
                return
            if "licenseExceptionId" in v:
                self.edict[v["licenseExceptionId"]] = v

        with open(spath / "licenses.json") as f:
            json.load(f, object_hook=_license_parse)

        with open(spath / "exceptions.json") as f:
            json.load(f, object_hook=_exception_parse)

    def lex(self):
        while True:
            # skip whitespace before matching any token
            nsp = 0
            while self.stream[nsp : nsp + 1].isspace():
                nsp = nsp + 1
            if nsp:
                self.stream = self.stream[nsp:]
                continue
            # early exit
            if len(self.stream) == 0:
                return None
            # see if we match a known token
            if self.stream[0:1] == "(" or self.stream[0:1] == ")":
                tok = self.stream[0]
                self.stream = self.stream[1:]
                return tok
            elif self.stream[0:4] == "WITH":
                self.stream = self.stream[4:]
                return "WITH"
            elif self.stream[0:3] == "AND":
                self.stream = self.stream[3:]
                return "AND"
            elif self.stream[0:2] == "OR":
                self.stream = self.stream[2:]
                return "OR"
            # otherwise see if we match a license id, maybe with a +
            idlen = 0
            stlen = len(self.stream)
            while stlen > idlen:
                c = self.stream[idlen]
                if (c != "-") and (c != ".") and not c.isalnum():
                    break
                idlen = idlen + 1
            # didn't get any valid character
            if idlen == 0:
                raise RuntimeError("unknown token: " + self.stream[0])
            tok = self.stream[0:idlen]
            # custom license in an SPDX expression
            if tok == "custom" and self.stream[idlen : idlen + 1] == ":":
                idlen = idlen + 1
                ollen = idlen
                while stlen > idlen:
                    c = self.stream[idlen]
                    if (c != "-") and (c != ".") and not c.isalnum():
                        break
                    idlen = idlen + 1
                if idlen == ollen:
                    raise RuntimeError("unknown token: 'custom:'")
                tok = self.stream[0:idlen]
                self.stream = self.stream[idlen:]
                return tok
            if tok.startswith("LicenseRef-") or tok.startswith("AdditionRef-"):
                # licenseref, additionref stand on their own
                self.stream = self.stream[idlen:]
                return tok
            elif tok.startswith("DocumentRef-"):
                # parse with the :
                if self.stream[idlen : idlen + 1] != ":":
                    raise RuntimeError("DocumentRef must be followed by colon")
                # skip
                idlen = idlen + 1
                self.stream = self.stream[idlen:]
                return tok
            elif tok not in self.ldict and tok not in self.edict:
                # this must be a license id
                raise RuntimeError("unknown token: " + tok)
            # may be directly followed by a +
            if self.stream[idlen : idlen + 1] == "+":
                tok = tok + "+"
                idlen = idlen + 1
            # return the token
            self.stream = self.stream[idlen:]
            return tok

    def parse_simple(self):
        if not self.token:
            raise RuntimeError("token expected")
        tok = self.token
        # parenthesized expression
        if tok == "(":
            self.token = self.lex()
            self.parse_expr()
            if self.token != ")":
                raise RuntimeError("')' expected to close '('")
            self.token = self.lex()
            return
        # documentref
        if tok.startswith("DocumentRef-"):
            self.need_install = True
            tok = self.token = self.lex()
        # license id maybe with exception
        if tok.endswith("+"):
            tok = tok[0 : len(tok) - 1]
        # custom licenses do not allow exceptions etc.
        if tok.startswith("custom:") or tok.startswith("LicenseRef-"):
            if tok != "custom:none" and tok != "custom:meta":
                self.need_install = True
        else:
            # not a custom license
            if tok not in self.ldict:
                raise RuntimeError("license id expected, got: " + tok)
            if _license_install(tok):
                self.need_install = True
        # check for exception
        self.token = self.lex()
        if self.token == "WITH":
            tok = self.token = self.lex()
            if not tok:
                raise RuntimeError("token expected")
            # documentref
            if tok.startswith("DocumentRef-"):
                self.need_install = True
                tok = self.token = self.lex()
            # custom exceptions
            if tok.startswith("custom:") or tok.startswith("AdditionRef-"):
                self.token = self.lex()
                self.need_install = True
                return
            if tok not in self.edict:
                raise RuntimeError("exception id expected, got: " + tok)
            self.token = self.lex()

    def parse_expr(self, mprec=1):
        # parse lhs
        self.parse_simple()
        # parse the rest
        while True:
            # no operator follows
            if not self.token:
                break
            # we're expecting an operator to be here
            # if it's not one, let the parent call handle it
            if self.token not in _opprec:
                break
            # deal with precedence
            oprec = _opprec[self.token]
            if oprec < mprec:
                break
            # expecting an rhs
            self.token = self.lex()
            if not self.token:
                raise RuntimeError("token expected")
            # for right associative this would be just oprec
            # we don't have any right associative operators here
            nprec = oprec + 1
            # parse rhs, repeat
            self.parse_expr(nprec)

    def parse(self, str):
        self.stream = str
        self.token = self.lex()
        self.need_install = False
        self.parse_expr()
        if self.token:
            raise RuntimeError("invalid token: " + self.token)
        return self.need_install


_parser = None


def init():
    from cbuild.core import paths

    global _parser
    _parser = SPDXParser(paths.cbuild() / "spdx")


def validate(str):
    return _parser.parse(str)
