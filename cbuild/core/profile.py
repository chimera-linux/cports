from cbuild.core import paths, logger
from cbuild import cpu

import configparser
import pathlib
import shlex

class Profile:
    def __init__(self, archn, pdata, gdata):
        # bootstrap is a simplfied case
        if archn == "bootstrap":
            self._triplet = None
            self._endian = cpu.host_endian()
            self._wordsize = cpu.host_wordsize()
            self._hardening = []
            # we ignore user flags here to guarantee a good base
            self._cflags = shlex.split(pdata.get("cflags", fallback = ""))
            self._cxxflags = shlex.split(pdata.get("cxxflags", fallback = ""))
            self._fflags = shlex.split(pdata.get("fflags", fallback = ""))
            self._ldflags = shlex.split(pdata.get("ldflags", fallback = ""))
            return

        if not "triplet" in pdata:
            logger.get().out_red(f"Unknown triplet for {archn}")
            raise Exception()

        if not "endian" in pdata:
            logger.get().out_red(f"Unknown endianness for {archn}")
            raise Exception()

        if not "wordsize" in pdata:
            logger.get().out_red(f"Unknown wordsize for {archn}")
            raise Exception()

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
    def triplet(self):
        return self._triplet

    def get_cflags(self, extra_flags = [], debug = False):
        ret = self._cflags + extra_flags
        if debug:
            ret.append("-g")
        return ret

    def get_cxxflags(self, extra_flags = [], debug = False):
        ret = self._cxxflags + extra_flags
        if debug:
            ret.append("-g")
        return ret

    def get_fflags(self, extra_flags = [], debug = False):
        ret = self._fflags + extra_flags
        if debug:
            ret.append("-g")
        return ret

    def get_ldflags(self, extra_flags = []):
        return self._ldflags + extra_flags

    @property
    def hardening(self):
        return self._hardening

    @property
    def wordsize(self):
        return self._wordsize

    @property
    def endian(self):
        return self._endian

_all_profiles = {}

def init(cparser):
    global _all_profiles

    profiles = paths.distdir() / "build_profiles"

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

        _all_profiles[archn] = Profile(archn, cp["profile"], cparser)

def get_profile(archn):
    return _all_profiles[archn]

def get_host():
    return _all_profiles[cpu.host()]

def get_target():
    return _all_profiles[cpu.target()]
