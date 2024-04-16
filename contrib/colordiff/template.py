pkgname = "colordiff"
pkgver = "1.0.21"
pkgrel = 1
build_style = "makefile"
make_install_args = ["INSTALL_DIR=/usr/bin", "MAN_DIR=/usr/share/man/man1"]
hostmakedepends = ["xmlto", "lynx", "perl"]
depends = ["perl"]
pkgdesc = "Tool to colorize diff output"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://www.colordiff.org"
source = f"https://www.colordiff.org/colordiff-{pkgver}.tar.gz"
sha256 = "9b30f4257ef0f0806dea5a27c9ad8edc3f7999f05ddaff6f0627064dc927e615"
# no testsuite
options = ["!check"]


def post_install(self):
    self.install_file("colordiffrc-*", "etc", glob=True)
