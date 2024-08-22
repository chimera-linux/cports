pkgname = "tree"
pkgver = "2.1.3"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Recursive directory indented listing of files"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://gitlab.com/OldManProgrammer/unix-tree/-/archive/{pkgver}/unix-tree-{pkgver}.tar.gz"
sha256 = "f554a1b62233b96fa8eaa2d85e91bc62cad80ee441fd591380f16cdfbe3e8868"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def init_install(self):
    self.make_install_args = [
        f"DESTDIR={self.chroot_destdir / 'usr/bin'}",
        f"MANDIR={self.chroot_destdir / 'usr/share/man'}",
    ]
