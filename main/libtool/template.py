pkgname = "libtool"
pkgver = "2.4.7"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "gm4",
    "perl",
    "automake",
    "help2man",
    "xz",
    "texinfo",
]
depends = ["gm4", "cmd:tar!bsdtar"]
pkgdesc = "Generic library support script"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://www.gnu.org/software/libtool"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "04e96c2404ea70c590c546eba4202a4e12722c640016c12b9b2f1ce3d481e9a8"
# FIXME: need to clear out sysroot from usr/bin/libtool for cross
# also keep libtool static compat intact
# tests interminable and endless
options = ["!cross", "!lto", "!check"]
# because this build system sucks
exec_wrappers = [("/usr/bin/gmake", "make")]


def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap", "--force", env={"MAKE": "gmake"})
    # prevent missing from re-running autotools
    for f in ["aclocal.m4", "Makefile.am", "Makefile.in"]:
        (self.cwd / f).touch()
        (self.cwd / "libltdl" / f).touch()


@subpackage("libltdl-devel")
def _devel(self):
    self.pkgdesc = "GNU libtool dlopen wrapper (development files)"
    # can't use default_devel, some aclocal stuff belongs in main package
    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/*.a",
        "usr/share/aclocal/ltdl.m4",
        "usr/share/libtool/libltdl",
    ]


@subpackage("libltdl")
def _ltdl(self):
    self.pkgdesc = "GNU libtool dlopen wrapper"
    return self.default_libs()


configure_gen = []
