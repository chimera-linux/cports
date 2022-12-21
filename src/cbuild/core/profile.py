from cbuild.core import paths, logger, chroot, errors
from cbuild.apk import cli as acli

import configparser
import platform
import pathlib
import shlex
import os
import sys

# recognized hardening options
hardening_fields = {
    "lto": False, # do not use directly, filled in by template
    "pie": True,
    "ssp": True, # this should really be compiler default
    "scp": True, # stack-clash-protection
    "int": True, # ubsan integer hardening
    "cet": True, # intel CET on x86
    "pac": True, # PAC+BTI on aarch64
    "cfi": False, # control flow integrity
    "sst": False, # safestack, not for DSOs
}

# only some are arch-specific, those are here
supported_fields = {
    "scp": set(["x86_64", "ppc64le", "ppc64", "ppc"]),
    "sst": set(["x86_64", "aarch64"]),
    "cfi": set(["x86_64", "aarch64"]),
    "cet": set(["x86_64"]),
    "pac": set(["aarch64"]),
}

def _get_harden(hlist):
    hdict = dict(hardening_fields)

    for fl in hlist:
        neg = fl.startswith("!")
        if neg:
            fl = fl[1:]

        if not fl in hdict:
            raise errors.CbuildException(f"unknown hardening option {fl}")

        hdict[fl] = not neg

    return hdict

# stuff that should go in both regular and linker flags, as it
# involves linking an extra runtime component (from compiler-rt)
def _get_archflags(prof, hard):
    sflags = []
    ubsan = False

    if not hard["ssp"]:
        sflags.append("-fno-stack-protector")

    if hard["sst"]:
        sflags.append("-fsanitize=safe-stack")

    # we cannot deploy cross-dso cfi yet, as doing so properly would require
    # support in the musl ldso, and llvm upstream does not recommend using
    # the existing compiler-rt implementation (unstable abi and so on)
    #
    # that means we stick with local cfi for hidden symbols for now
    if hard["cfi"] and hard["lto"] and prof._arch in supported_fields["cfi"]:
        sflags.append("-fsanitize=cfi")

    if hard["int"]:
        sflags.append("-fsanitize=signed-integer-overflow,shift,integer-divide-by-zero")
        ubsan = True

    if ubsan:
        sflags.append("-fsanitize-minimal-runtime")
        sflags.append("-fno-sanitize-recover")

    return sflags

def _get_hcflags(prof, tharden):
    hflags = []
    hard = _get_harden(tharden)

    if not hard["pie"]:
        hflags.append("-fno-PIE")

    if hard["scp"] and prof._arch in supported_fields["scp"]:
        hflags.append("-fstack-clash-protection")

    if hard["cet"] and prof._arch in supported_fields["cet"]:
        sflags.append("-fcf-protection=full")

    if hard["pac"] and prof._arch in supported_fields["pac"]:
        sflags.append("-mbranch-protection=standard")

    hflags += _get_archflags(prof, hard)

    return hflags

def _get_hldflags(prof, tharden):
    hflags = []
    hard = _get_harden(tharden)

    if not hard["pie"]:
        hflags.append("-no-pie")

    hflags += _get_archflags(prof, hard)

    return hflags

# have a custom quote wrapper since at least gnu autotools
# configure does not understand '-DFOO="bar baz"' and results
# in the compiler thinking it's an input file
def _quote(s):
    sep = s.find("=")
    # no value set, quote as is
    if sep < 0:
        return shlex.quote(s)

    nm = s[0:sep]
    # name part itself needs quoting, quote entire thing
    if shlex.quote(nm) != nm:
        return shlex.quote(s)
    # otherwise quote just the value
    return nm + "=" + shlex.quote(s[sep + 1:])

def _flags_ret(it, shell):
    if shell:
        return " ".join(_quote(x) for x in it)
    else:
        return list(it)

def _get_gencflags(self, name, extra_flags, debug, hardening, shell):
    hflags = _get_hcflags(self, hardening)

    # bootstrap
    if not self._triplet:
        bflags = ["-isystem", paths.bldroot() / "usr/include"]
    else:
        bflags = []

    ret = hflags + self._flags[name] + bflags + extra_flags

    if debug >= 0:
        ret.append(f"-g{debug}")

    return _flags_ret(map(lambda v: str(v), ret), shell)

def _get_ldflags(self, name, extra_flags, debug, hardening, shell):
    hflags = _get_hldflags(self, hardening)

    # bootstrap
    if not self._triplet:
        bflags = [
            "-L" + str(paths.bldroot() / "usr/lib"),
            "-Wl,-rpath-link=" + str(paths.bldroot() / "usr/lib")
        ]
    else:
        bflags = []

    ret = hflags + self._flags["LDFLAGS"] + bflags + extra_flags

    return _flags_ret(map(lambda v: str(v), ret), shell)

def _get_rustflags(self, name, extra_flags, debug, hardening, shell):
    if self.cross:
        bflags = [
            "--sysroot", self.sysroot / "usr",
        ]
    else:
        bflags = []

    ret = self._flags["RUSTFLAGS"] + bflags + extra_flags

    return _flags_ret(map(lambda v: str(v), ret), shell)

_flag_handlers = {
    "CFLAGS": _get_gencflags,
    "CXXFLAGS": _get_gencflags,
    "FFLAGS": _get_gencflags,
    "LDFLAGS": _get_ldflags,
    "RUSTFLAGS": _get_rustflags,
}

def has_hardening(hname, hardening = []):
    return _get_harden(hardening)[hname]

_flag_types = list(_flag_handlers.keys())

class Profile:
    def __init__(self, archn, pdata, gdata):
        self._flags = {}

        # profile flags are always used
        if "flags" in pdata:
            pd = pdata["flags"]
            for ft in _flag_types:
                self._flags[ft] = shlex.split(pd.get(ft, fallback = ""))

        # bootstrap is a simplfied case
        if archn == "bootstrap":
            # initialize with arch data of the host system
            self._arch = acli.get_arch()
            self._triplet = None
            self._endian = sys.byteorder
            self._wordsize = int(platform.architecture()[0][:-3])
            self._repos = []
            self._goarch = None
            # account for arch specific bootstrap flags
            if f"flags.{self._arch}" in pdata:
                pd = pdata[f"flags.{self._arch}"]
                for ft in _flag_types:
                    self._flags[ft] += shlex.split(pd.get(ft, fallback = ""))
            return

        pdata = pdata["profile"]

        if not "triplet" in pdata:
            raise errors.CbuildException(f"unknown triplet for {archn}")

        if not "endian" in pdata:
            raise errors.CbuildException(f"unknown endianness for {archn}")

        if not "wordsize" in pdata:
            raise errors.CbuildException(f"unknown wordsize for {archn}")

        self._arch = archn
        self._triplet = pdata.get("triplet")
        self._endian = pdata.get("endian")
        self._wordsize = pdata.getint("wordsize")

        if self._wordsize != 32 and self._wordsize != 64:
            raise errors.CbuildException(
                f"unknown wordsize for {archn}: {self._wordsize}"
            )

        if self._endian != "little" and self._endian != "big":
            raise errors.CbuildException(
                f"unknown endianness for {archn}: {self._endian}"
            )

        if "goarch" in pdata:
            self._goarch = pdata.get("goarch")
        else:
            self._goarch = None

        if "repos" in pdata:
            ra = pdata.get("repos").split(" ")
            if len(ra) == 0 or len(ra[0]) == 0:
                self._repos = []
            else:
                self._repos = ra
        else:
            self._repos = []

        def get_gflag(fn):
            if f"flags.{archn}" in gdata:
                ccat = gdata[f"flags.{archn}"]
            elif "flags" in gdata:
                ccat = gdata["flags"]
            else:
                return []
            return shlex.split(ccat.get(fn, fallback = ""))

        # user flags may override whatever is in profile
        # it also usually defines what optimization level we're using
        for ft in _flag_types:
            self._flags[ft] += get_gflag(ft)

    @property
    def arch(self):
        return self._arch

    @property
    def triplet(self):
        return self._triplet

    @property
    def sysroot(self):
        if not self.cross:
            return pathlib.Path("/")

        return pathlib.Path("/usr") / self.triplet

    def get_tool_flags(
        self, name, extra_flags = [], debug = -1, hardening = [], shell = False
    ):
        return _flag_handlers[name](
            self, name, extra_flags, debug, hardening, shell
        )

    def _get_supported_tool_flags(self):
        return _flag_types

    @property
    def wordsize(self):
        return self._wordsize

    @property
    def endian(self):
        return self._endian

    @property
    def cross(self):
        return self._arch != chroot.host_cpu()

    @property
    def goarch(self):
        return self._goarch

    @property
    def repos(self):
        return self._repos

_all_profiles = {}

def init(cparser):
    global _all_profiles

    profiles = paths.distdir() / "etc/build_profiles"

    for pf in profiles.glob("*.ini"):
        archn = pf.with_suffix("").name

        cp = configparser.ConfigParser(
            interpolation = configparser.ExtendedInterpolation()
        )
        with open(pf) as cf:
            cp.read_file(cf)

        if archn != "bootstrap" and not "profile" in cp:
            raise errors.CbuildException(f"malformed profile: {archn}")

        _all_profiles[archn] = Profile(archn, cp, cparser)

def get_profile(archn):
    return _all_profiles[archn]
