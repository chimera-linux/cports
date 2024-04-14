pkgname = "aspell-en"
pkgver = "2020.12.07"
pkgrel = 0
build_style = "configure"
make_cmd = "gmake"
hostmakedepends = [
    "aspell",
    "gmake",
]
pkgdesc = "English dictionary for aspell"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "custom:aspell-en"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-{pkgver}-0.tar.bz2"
sha256 = "4c8f734a28a088b88bb6481fcf972d0b2c3dc8da944f7673283ce487eac49fb3"
# Makefile has no check target
options = ["!check"]


def post_install(self):
    self.install_license("Copyright")
