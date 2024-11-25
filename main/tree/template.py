pkgname = "tree"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Recursive directory indented listing of files"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://gitlab.com/OldManProgrammer/unix-tree/-/archive/{pkgver}/unix-tree-{pkgver}.tar.gz"
sha256 = "bc6f954de0626babe80969746ded5440a7658f9a397e37304ddc1cc23fc08c2f"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def init_install(self):
    self.make_install_args = [
        f"DESTDIR={self.chroot_destdir / 'usr/bin'}",
        f"MANDIR={self.chroot_destdir / 'usr/share/man'}",
    ]
