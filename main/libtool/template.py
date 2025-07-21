pkgname = "libtool"
pkgver = "2.5.4"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = [
    "automake",
    "gm4",
    "help2man",
    "perl",
    "texinfo",
]
depends = ["gm4", "cmd:tar!base-files"]
pkgdesc = "Generic library support script"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://www.gnu.org/software/libtool"
source = f"$(GNU_SITE)/libtool/libtool-{pkgver}.tar.gz"
sha256 = "da8ebb2ce4dcf46b90098daf962cffa68f4b4f62ea60f798d0ef12929ede6adf"
# FIXME: need to clear out sysroot from usr/bin/libtool for cross
# also keep libtool static compat intact
# tests interminable and endless
options = ["!check", "!cross", "!lto"]


def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap", "--force")
    # prevent missing from re-running autotools
    for f in ["aclocal.m4", "Makefile.am", "Makefile.in"]:
        (self.cwd / f).touch()
        (self.cwd / "libltdl" / f).touch()


@subpackage("libtool-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libltdl-devel")]
    # can't use default_devel, some aclocal stuff belongs in main package
    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/*.a",
        "usr/share/aclocal/ltdl.m4",
        "usr/share/libtool/libltdl",
    ]


@subpackage("libtool-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libltdl")]

    return self.default_libs()
