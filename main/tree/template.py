pkgname = "tree"
pkgver = "2.3.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Recursive directory indented listing of files"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://gitlab.com/OldManProgrammer/unix-tree/-/archive/{pkgver}/unix-tree-{pkgver}.tar.gz"
sha256 = "ac3cda918492fc4dd7833745a9fd431fa976c35e682fd824656bfe21d8b51a69"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def init_install(self):
    self.make_install_args = [
        f"DESTDIR={self.chroot_destdir / 'usr/bin'}",
        f"MANDIR={self.chroot_destdir / 'usr/share/man'}",
    ]
