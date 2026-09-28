pkgname = "snowball"
pkgver = "3.1.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["perl"]
pkgdesc = "Snowball rule-based stemming algorithms"
license = "BSD-3-Clause"
url = "https://snowballstem.org/index.html"
_commit = "a0ec0d0a2839ec885878868de20fcb63209d92b0"
source = [
    f"https://github.com/snowballstem/snowball/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/snowballstem/snowball-data/archive/{_commit}.tar.gz",
]
source_paths = [".", "snowball-data"]
sha256 = [
    "d8714aa91ed4333654708472a7a98b529c867a8f99b05c5e66febf4ca72c44c7",
    "caab8da3999e121ee72b2eba6d45166f984deb1f3c3ca967bea726501c0ee943",
]
# needed for tests to find libstemmer
env = {"LD_LIBRARY_PATH": "./", "STEMMING_DATA": "snowball-data"}
# snowball is run during compilation giving error
# /bin/sh: ./snowball: Exec format error
options = ["!cross"]


def install(self):
    self.install_bin("snowball")
    self.install_bin("stemwords")
    self.install_lib(f"libstemmer.so.{pkgver}")
    self.install_link(
        f"usr/lib/libstemmer.so.{pkgver[0]}", f"libstemmer.so.{pkgver}"
    )
    self.install_link("usr/lib/libstemmer.so", f"libstemmer.so.{pkgver}")
    self.install_file("include/libstemmer.h", "usr/include")
    self.install_license("COPYING")


@subpackage("snowball-devel")
def _(self):
    return self.default_devel()


@subpackage("snowball-progs")
def _(self):
    self.subdesc = "command line tools"
    return self.default_progs()
