pkgname = "chimera-install-scripts"
pkgver = "0.5"
pkgrel = 0
_commit = "437f08305db5b71926f90265fb0279ad143c5e27"
build_style = "makefile"
depends = [
    "cmd:apk!apk-tools",
    "cmd:chroot!chimerautils",
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
sha256 = "6479e7f3f567f1ff50de09fa214e03f7a402163e44668991115c7b8772d5a726"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
