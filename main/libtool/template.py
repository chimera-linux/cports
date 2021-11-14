pkgname = "libtool"
pkgver = "2.4.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "gm4", "perl", "automake", "help2man", "xz", "texinfo"
]
depends = ["gm4", "cmd:tar", "cmd:sed"]
depends_providers = {
    "cmd:tar": "bsdtar",
    "cmd:sed": "bsdsed",
}
pkgdesc = "Generic library support script"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://www.gnu.org/software/libtool"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e3bd4d5d3d025a36c21dd6af7ea818a2afcd4dfc1ea5a17b39d7854bcd0c06e3"
# FIXME: need to clear out sysroot from usr/bin/libtool for cross
options = ["!cross"]

def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap", ["--force"], env = {
        "MAKE": "gmake"
    })
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
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/share/aclocal/ltdl.m4",
        "usr/share/libtool/libltdl",
    ]

@subpackage("libltdl")
def _devel(self):
    self.pkgdesc = "GNU libtool dlopen wrapper"
    return self.default_libs()
