pkgname = "snowball"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
# check_utf8 check_iso_8859_1 check_iso_8859_2 check_koi8r
# all have missing sub-targets
make_check_target = "check_stemtest"
hostmakedepends = ["gmake", "perl"]
pkgdesc = "Snowball rule-based stemming algorithms"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-3-Clause"
url = "https://snowballstem.org/index.html"
source = f"https://github.com/snowballstem/snowball/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "425cdb5fba13a01db59a1713780f0662e984204f402d3dae1525bda9e6d30f1a"
# needed for tests to find libstemmer
env = {"LD_LIBRARY_PATH": "./"}
# snowball is run during compilation giving error
# /bin/sh: ./snowball: Exec format error
options = ["!cross"]


def do_install(self):
    self.install_bin("snowball")
    self.install_bin("stemwords")
    self.install_lib(f"libstemmer.so.{pkgver}")
    self.install_link(
        f"libstemmer.so.{pkgver}", f"usr/lib/libstemmer.so.{pkgver[0]}"
    )
    self.install_link(f"libstemmer.so.{pkgver}", "usr/lib/libstemmer.so")
    self.install_file("include/libstemmer.h", "usr/include")
    self.install_license("COPYING")


@subpackage("snowball-devel")
def _devel(self):
    return self.default_devel()


@subpackage("snowball-progs")
def _subpkg(self):
    self.pkgdesc = f"{pkgdesc} (command line tools)"
    return self.default_progs()
