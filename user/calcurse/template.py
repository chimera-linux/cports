pkgname = "calcurse"
pkgver = "4.8.1"
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
maintainer = "Caio Raposo <caioraposo@disroot.org>"
license = "BSD-2-Clause"
url = "https://calcurse.org"
source = f"https://calcurse.org/files/calcurse-{pkgver}.tar.gz"
sha256 = "d86bb37014fd69b8d83ccb904ac979c6b8ddf59ee3dbc80f5a274525e4d5830a"


def post_install(self):
    self.install_license("COPYING")
