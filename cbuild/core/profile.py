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
    "ssp": True, # this should really be compiler default
    "scp": False, # stack-clash-protection
}

def _get_harden(dharden, tharden):
    hdict = dict(hardening_fields)

    for fl in dharden + tharden:
        neg = fl.startswith("!")
        if neg:
            fl = fl[1:]

        if not fl in hdict:
            logger.get().out_red(f"Unknown hardening option {fl}")
            raise Exception()

        hdict[fl] = not neg

    return hdict

def _get_hcflags(dharden, tharden):
    hflags = []
    hard = _get_harden(dharden, tharden)

    if hard["fortify"]:
        hflags.append("-D_FORTIFY_SOURCE=2")

    if not hard["pie"]:
        hflags.append("-fno-PIE")

    if hard["ssp"]:
        hflags.append("-fstack-protector-strong")

    if hard["scp"]:
        hflags.append("-fstack-clash-protection")

    return hflags

def _get_hldflags(dharden, tharden):
    hflags = ["-Wl,--as-needed"]
    hard = _get_harden(dharden, tharden)

    if hard["pie"]:
        hflags.append("-Wl,-z,now")
        hflags.append("-Wl,-z,relro")
    else:
        hflags.append("-no-pie")

    return hflags

class Profile:
    def __init__(self, archn, pdata, gdata):
        # bootstrap is a simplfied case
        if archn == "bootstrap":
            # initialize with arch data of the host system
            self._arch = os.uname().machine
            self._triplet = None
            self._endian = sys.byteorder
            self._wordsize = int(platform.architecture()[0][:-3])
            self._hardening = []
            # we ignore user flags here to guarantee a good base
            pd = pdata["profile"]
            self._cflags = shlex.split(pd.get("cflags", fallback = ""))
            self._cxxflags = shlex.split(pd.get("cxxflags", fallback = ""))
            self._fflags = shlex.split(pd.get("fflags", fallback = ""))
            self._ldflags = shlex.split(pd.get("ldflags", fallback = ""))
            # account for arch specific bootstrap flags
            if self._arch in pdata:
                pd = pdata[self._arch]
                self._cflags += shlex.split(pd.get("cflags", fallback = ""))
                self._cxxflags += shlex.split(pd.get("cxxflags", fallback = ""))
                self._fflags += shlex.split(pd.get("fflags", fallback = ""))
                self._ldflags += shlex.split(pd.get("ldflags", fallback = ""))
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
            if f"build.{archn}" in gdata:
                ccat = gdata[f"build.{archn}"]
            elif "build" in gdata:
                ccat = gdata["build"]
            else:
                return []
            return shlex.split(ccat.get(fn, fallback = ""))

        # profile data comes first
        self._cflags = shlex.split(pdata.get("cflags", fallback = ""))
        self._cxxflags = shlex.split(pdata.get("cxxflags", fallback = ""))
        self._fflags = shlex.split(pdata.get("fflags", fallback = ""))
        self._ldflags = shlex.split(pdata.get("ldflags", fallback = ""))

        # user flags may override whatever is in profile
        # it also usually defines what optimization level we're using
        self._cflags += get_gflag("cflags")
        self._cxxflags += get_gflag("cxxflags")
        self._fflags += get_gflag("fflags")
        self._ldflags += get_gflag("ldflags")

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

    def get_cflags(
        self, extra_flags = [], debug = False, hardening = [], shell = False
    ):
        hflags = _get_hcflags(self._hardening, hardening)

        # bootstrap
        if not self._triplet:
            bflags = ["-isystem", paths.masterdir() / "usr/include"]
        elif self.cross:
            bflags = ["--sysroot", self.sysroot]
        else:
            bflags = []

        ret = hflags + self._cflags + bflags + extra_flags

        if debug:
            ret.append("-g")

        if shell:
            return shlex.join(ret)

        return ret

    def get_cxxflags(
        self, extra_flags = [], debug = False, hardening = [], shell = False
    ):
        hflags = _get_hcflags(self._hardening, hardening)

        # bootstrap
        if not self._triplet:
            bflags = ["-isystem", paths.masterdir() / "usr/include"]
        elif self.cross:
            bflags = ["--sysroot", self.sysroot]
        else:
            bflags = []

        ret = hflags + self._cxxflags + bflags + extra_flags

        if debug:
            ret.append("-g")

        if shell:
            return shlex.join(ret)

        return ret

    def get_fflags(
        self, extra_flags = [], debug = False, hardening = [], shell = False
    ):
        hflags = _get_hcflags(self._hardening, hardening)

        # bootstrap
        if not self._triplet:
            bflags = ["-isystem", paths.masterdir() / "usr/include"]
        elif self.cross:
            bflags = ["--sysroot", self.sysroot]
        else:
            bflags = []

        ret = hflags + self._fflags + bflags + extra_flags

        if debug:
            ret.append("-g")

        if shell:
            return shlex.join(ret)

        return ret

    def get_ldflags(self, extra_flags = [], hardening = [], shell = False):
        hflags = _get_hldflags(self._hardening, hardening)

        # bootstrap
        if not self._triplet:
            bflags = [
                "-L" + str(paths.masterdir() / "usr/lib"),
                "-Wl,-rpath-link=" + str(paths.masterdir() / "usr/lib")
            ]
        elif self.cross:
            bflags = ["--sysroot", self.sysroot]
        else:
            bflags = []

        ret = hflags + self._ldflags + bflags + extra_flags

        if shell:
            return shlex.join(ret)

        return ret

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

    profiles = paths.cbuild() / "build_profiles"

    for pf in profiles.glob("*.ini"):
        archn = pf.with_suffix("").name

        cp = configparser.ConfigParser(
            interpolation = configparser.ExtendedInterpolation()
        )
        with open(pf) as cf:
            cp.read_file(cf)

        if not "profile" in cp:
            logger.get().out_red(f"Malformed profile: {archn}")
            raise Exception()

        _all_profiles[archn] = Profile(archn, cp, cparser)

def get_profile(archn):
    return _all_profiles[archn]
