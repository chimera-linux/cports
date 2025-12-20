pkgname = "chimera-install-scripts"
pkgver = "0.6"
pkgrel = 0
_commit = "dc0984a59bd94e1f6cc3b31255bad4edafb69d6a"
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
sha256 = "d41919c919d347352b08257489d77531ab1cd214ea858628ae6f4e418c5616a4"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.md")
