pkgname = "clatd"
pkgver = "2.1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["perl"]
makedepends = ["dinit-chimera"]
depends = [
    "cmd:ip!iproute2",
    "cmd:nft!nftables",
    "cmd:tayga!tayga",
    "perl-net-dns",
    "perl-net-ip",
]
pkgdesc = "464XLAT implementation"
license = "MIT"
url = "https://github.com/toreanderson/clatd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fd171a7820215c2eaa950b81815c04d032cdcab619e8b5093198e96cdaefb4b0"
# check: no tests
options = ["!check"]


def pre_install(self):
    self.install_dir("usr/share/man/man8")


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("LICENCE")
    self.install_service("^/clatd")
