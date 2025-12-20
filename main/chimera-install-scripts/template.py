pkgname = "chimera-install-scripts"
pkgver = "0.6.1"
pkgrel = 0
_commit = "43b0a7d2c86fa51c85a3fdc532ac5ebf9ece83b1"
build_style = "makefile"
depends = [
    "cmd:apk!apk-tools",
    "cmd:chroot!chimerautils",
    "cmd:dialog!dialog",
    "cmd:findmnt!util-linux-mount",
    "cmd:id!chimerautils",
    "cmd:mount!util-linux-mount",
    "cmd:mountpoint!util-linux-mount",
    "cmd:realpath!chimerautils",
    "cmd:tar!libarchive-progs",
]
pkgdesc = "Scripts to aid Chimera system installation"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimera-install-scripts"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "a2f9ca5c91249c77e039574f174b1695bc6afe79ad09678310eb646989f42e10"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
