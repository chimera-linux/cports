pkgname = "rlwrap"
pkgver = "0.46.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "autoconf",
    "automake",
    "gmake",
    "libtool",
]
makedepends = [
    "ncurses-devel",
    "readline-devel",
]
checkdepends = ["perl"]
pkgdesc = "Readline Wrapper"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/hanslub42/rlwrap"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c537e8a53df36f1f996601d776203478ad56fab1d67b3c1a63057badb0851cec"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
