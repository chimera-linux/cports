from cbuild.core import paths, logger, chroot

import configparser
import platform
import pathlib
import shlex
import os
import sys

# recognized hardening options
hardening_fields = {
    "fortify": True,
    "pie": True,
    "relro": True,
    "ssp": True, # this should really be compiler default
    "scp": True, # stack-clash-protection
}

# some hardening options are universal while some must be
# declared by the target as supported, on other systems
# they become noop
supported_hardening = {
    "fortify": True,
    "pie": True,
    "relro": True,
    "ssp": True,
    "scp": False,
}

def _htodict(hlist, hdict):
    for fl in hlist:
        neg = fl.startswith("!")
        if neg:
            fl = fl[1:]

        if not fl in hdict:
            logger.get().out_red(f"Unknown hardening option {fl}")
            raise Exception()

        hdict[fl] = not neg

    return hdict

def _get_harden(sharden, tharden):
    # hardening that is declared
    hdict = dict(hardening_fields)
    # hardening that is supported
    shdict = dict(supported_hardening)

    hdict = _htodict(tharden, hdict)
    shdict = _htodict(sharden, shdict)

    return hdict

def _get_hcflags(sharden, tharden):
    hflags = []
    hard = _get_harden(sharden, tharden)

    if hard["fortify"]:
        hflags.append("-D_FORTIFY_SOURCE=2")

    if not hard["pie"]:
        hflags.append("-fno-PIE")

    if hard["ssp"]:
        hflags.append("-fstack-protector-strong")

    if hard["scp"]:
        hflags.append("-fstack-clash-protection")

    return hflags

def _get_hldflags(sharden, tharden):
    hflags = ["-Wl,--as-needed"]
    hard = _get_harden(sharden, tharden)

    if hard["relro"]:
        hflags.append("-Wl,-z,now")
        hflags.append("-Wl,-z,relro")

    if not hard["pie"]:
        hflags.append("-no-pie")

    return hflags

def _flags_ret(it, shell):
    if shell:
        return shlex.join(it)
    else:
        return list(it)

def _get_gencflags(self, name, extra_flags, debug, hardening, shell):
    hflags = _get_hcflags(self._hardening, hardening)

    # bootstrap
    if not self._triplet:
        bflags = ["-isystem", paths.bldroot() / "usr/include"]
    elif self.cross:
        bflags = ["--sysroot", self.sysroot]
    else:
        bflags = []

    ret = hflags + self._flags[name] + bflags + extra_flags

    if debug >= 0:
        ret.append(f"-g{debug}")

    return _flags_ret(map(lambda v: str(v), ret), shell)

def _get_ldflags(self, name, extra_flags, debug, hardening, shell):
    hflags = _get_hldflags(self._hardening, hardening)

    # bootstrap
    if not self._triplet:
        bflags = [
            "-L" + str(paths.bldroot() / "usr/lib"),
            "-Wl,-rpath-link=" + str(paths.bldroot() / "usr/lib")
        ]
    elif self.cross:
        bflags = ["--sysroot", self.sysroot]
    else:
        bflags = []

    ret = hflags + self._flags["LDFLAGS"] + bflags + extra_flags

    return _flags_ret(map(lambda v: str(v), ret), shell)

_flag_handlers = {
    "CFLAGS": _get_gencflags,
    "CXXFLAGS": _get_gencflags,
    "FFLAGS": _get_gencflags,
    "LDFLAGS": _get_ldflags,
}

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
            self._arch = os.uname().machine
            self._triplet = None
            self._endian = sys.byteorder
            self._wordsize = int(platform.architecture()[0][:-3])
            self._hardening = []
            # account for arch specific bootstrap flags
            if f"flags.{self._arch}" in pdata:
                pd = pdata[f"flags.{self._arch}"]
                for ft in _flag_types:
                    self._flags[ft] += shlex.split(pd.get(ft, fallback = ""))
            return

        pdata = pdata["profile"]

        if not "triplet" in pdata:
            logger.get().out_red(f"Unknown triplet for {archn}")
            raise Exception()

        if not "endian" in pdata:
            logger.get().out_red(f"Unknown endianness for {archn}")
            raise Exception()

        if not "wordsize" in pdata:
            logger.get().out_red(f"Unknown wordsize for {archn}")
            raise Exception()

        self._arch = archn
        self._triplet = pdata.get("triplet")
        self._endian = pdata.get("endian")
        self._wordsize = pdata.getint("wordsize")

        if self._wordsize != 32 and self._wordsize != 64:
            logger.get().out_red(
                f"Unknown wordsize for {archn}: {self._wordsize}"
            )
            raise Exception()

        if self._endian != "little" and self._endian != "big":
            logger.get().out_red(
                f"Unknown endianness for {archn}: {self._endian}"
            )
            raise Exception()

        if "hardening" in pdata:
            self._hardening = pdata.get("hardening").split()
        else:
            self._hardening = []

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
    def short_triplet(self):
        tpl = self.triplet
        if not tpl:
            return None
        return tpl.replace("-unknown-", "-")

    @property
    def sysroot(self):
        if not self.cross:
            return pathlib.Path("/")

        return pathlib.Path("/usr") / self.short_triplet

    def get_tool_flags(
        self, name, extra_flags = [], debug = -1, hardening = [], shell = False
    ):
        return _flag_handlers[name](
            self, name, extra_flags, debug, hardening, shell
        )

    def _get_supported_tool_flags(self):
        return _flag_types

    def has_hardening(self, hname, hardening = []):
        return _get_harden(self._hardening, hardening)[hname]

    @property
    def hardening(self):
        return self._hardening

    @property
    def wordsize(self):
        return self._wordsize

    @property
    def endian(self):
        return self._endian

    @property
    def cross(self):
        return self._arch != chroot.host_cpu()

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
            logger.get().out_red(f"Malformed profile: {archn}")
            raise Exception()

        _all_profiles[archn] = Profile(archn, cp, cparser)

def get_profile(archn):
    return _all_profiles[archn]
