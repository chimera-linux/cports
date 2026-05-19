pkgname = "colordiff"
pkgver = "1.0.22"
pkgrel = 0
build_style = "makefile"
make_install_args = ["INSTALL_DIR=/usr/bin", "MAN_DIR=/usr/share/man/man1"]
hostmakedepends = ["xmlto", "lynx", "perl"]
depends = ["perl"]
pkgdesc = "Tool to colorize diff output"
license = "GPL-2.0-or-later"
url = "https://www.colordiff.org"
source = f"https://www.colordiff.org/colordiff-{pkgver}.tar.gz"
sha256 = "f96f73c54521c53f14dc164d5a3920c9ca21a0e5f8e9613f43812a98af3e22af"
# no testsuite
options = ["!check"]


def post_install(self):
    self.install_file("colordiffrc-*", "etc", glob=True)
