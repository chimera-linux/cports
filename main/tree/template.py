pkgname = "tree"
pkgver = "2.3.2"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Recursive directory indented listing of files"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://gitlab.com/OldManProgrammer/unix-tree/-/archive/{pkgver}/unix-tree-{pkgver}.tar.gz"
sha256 = "513a53cbc42ca1f4ea06af2bab1f5283524a3848266b1d162416f8033afc4985"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def init_install(self):
    self.make_install_args = [
        f"DESTDIR={self.chroot_destdir / 'usr/bin'}",
        f"MANDIR={self.chroot_destdir / 'usr/share/man'}",
    ]
