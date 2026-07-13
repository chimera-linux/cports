pkgname = "aspell-en"
pkgver = "2026.02.25"
pkgrel = 0
build_style = "configure"
hostmakedepends = [
    "aspell",
]
depends = ["aspell"]
pkgdesc = "English dictionary for aspell"
license = "custom:aspell-en"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-{pkgver}-0.tar.bz2"
sha256 = "77a5cb437c45d1115f3b593802c20651d8c93803ed1073278dc1a1240016f10d"
# Makefile has no check target
options = ["!check"]


def post_install(self):
    self.install_license("Copyright")
