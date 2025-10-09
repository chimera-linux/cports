pkgname = "calcurse"
pkgver = "4.8.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "asciidoc",
    "autoconf-archive",
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = ["ncurses-devel"]
depends = ["python-httplib2"]
pkgdesc = "Calendar and scheduling application for the command line"
license = "BSD-2-Clause"
url = "https://calcurse.org"
source = f"https://calcurse.org/files/calcurse-{pkgver}.tar.gz"
sha256 = "849ba852c7f37b6772365cb0c42a94cde0fe75efba91363e96a0e7ef797ba565"


def post_install(self):
    self.install_license("COPYING")
