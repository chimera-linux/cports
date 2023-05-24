pkgname = "chimera-install-scripts"
pkgver = "0.1"
pkgrel = 0
_commit = "7ae4b3be8e46c34a2d398dfa87014a82ff261137"
build_style = "makefile"
depends = [
    "virtual:cmd:chroot!chimerautils",
    "virtual:cmd:id!chimerautils",
    "virtual:cmd:realpath!chimerautils",
    "virtual:cmd:findmnt!mount",
    "virtual:cmd:mount!mount",
    "virtual:cmd:mountpoint!mount",
    "virtual:cmd:tar!bsdtar",
    "virtual:cmd:apk!apk-tools",
]
pkgdesc = "Scripts to aid Chimera system installation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimera-install-scripts"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "736ab4a920e2d37863fd9c39bc54d129591aae836b92461e31f187f706d39ac0"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
