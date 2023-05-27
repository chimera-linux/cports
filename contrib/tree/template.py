pkgname = "tree"
pkgver = "2.1.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Utility to display a tree view of directories"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later"
url = "https://oldmanprogrammer.net/source.php?dir=projects/tree"
source = f"https://oldmanprogrammer.net/tar/tree/tree-{pkgver}.tgz"
sha256 = "0160c535bff2b0dc6a830b9944e981e3427380f63e748da96ced7071faebabf6"
# no check/test target
options = ["!check"]

def do_install(self):
    self.make.install([
        f"MANDIR={self.chroot_destdir}/usr/share/man",
        f"DESTDIR={self.chroot_destdir}/usr/bin"
    ])

def post_install(self):
    self.install_license("LICENSE")
