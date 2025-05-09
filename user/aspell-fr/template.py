pkgname = "aspell-fr"
pkgver = "0.50.3"
pkgrel = 0
_ver = "-".join(pkgver.rsplit(".", 1))
build_style = "configure"
hostmakedepends = [
    "aspell",
]
depends = ["aspell"]
pkgdesc = "French dictionary for aspell"
license = "custom:aspell-fr"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/dict/fr/aspell-fr-{_ver}.tar.bz2"
sha256 = "f9421047519d2af9a7a466e4336f6e6ea55206b356cd33c8bd18cb626bf2ce91"
# Makefile has no check target
options = ["!check"]


def post_install(self):
    self.install_license("Copyright")
