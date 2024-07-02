pkgname = "tree"
pkgver = "2.1.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Recursive directory indented listing of files"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://gitlab.com/OldManProgrammer/unix-tree/-/archive/{pkgver}/unix-tree-{pkgver}.tar.gz"
sha256 = "5b4c92fa770ba157056546b4e59343a28749cb42b4a3a671ef76c17319cfeb2e"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def init_install(self):
    self.make_install_args = [
        f"DESTDIR={self.chroot_destdir / 'usr/bin'}",
        f"MANDIR={self.chroot_destdir / 'usr/share/man'}",
    ]
