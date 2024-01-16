pkgname = "chimera-install-scripts"
pkgver = "0.2"
pkgrel = 0
_commit = "92c05a86fe051eca961b8ed98151ee1d9cce3cb5"
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
sha256 = "c952e71cc081f504c943ae124f5ca83143a47d24558f4c356bd90d307694a32d"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
