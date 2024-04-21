pkgname = "chimera-install-scripts"
pkgver = "0.3"
pkgrel = 0
_commit = "d64bd12ee54a2abb00c587bd3e0b83a47b165be2"
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
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "0279525256ab9977282c9bca74c1f7345d5a1d01886e20fb7ff1d23660cc64e9"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
