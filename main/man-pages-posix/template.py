pkgname = "man-pages-posix"
_pver = "2017-a"
pkgver = f"{_pver.replace('-', '')}"
pkgrel = 1
pkgdesc = "POSIX man pages"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:posix"
url = "https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html"
source = f"https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-{_pver}.tar.xz"
sha256 = "ce67bb25b5048b20dad772e405a83f4bc70faf051afa289361c81f9660318bc3"
options = ["!autosplit"]


def install(self):
    self.install_license("POSIX-COPYRIGHT")
    for cat in ["0p", "1p", "3p"]:
        self.install_man(f"man{cat}/*.{cat}", cat=cat, glob=True)
