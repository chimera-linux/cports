pkgname = "chimera-install-scripts"
pkgver = "0.4"
pkgrel = 0
_commit = "74ba5eff892c3817ddf2bc7bd774b6f5c890f322"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimera-install-scripts"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "61e3f5d6417b14e079e31f05c3caef7cf49322601860fa4b013c5e344aa2fa7e"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
