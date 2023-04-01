pkgname = "chimera-install-scripts"
pkgver = "0.1"
pkgrel = 0
_commit = "88a1c7d1dd981f8acb032173d0d2c10216361664"
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
sha256 = "bc019cade71a85d92e2568150d14a7cb1cd277b875cd50fb471d825c9c7ac49a"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("COPYING.md")
