pkgname = "man-pages-posix"
pkgver = "2017a"
pkgrel = 1
pkgdesc = "POSIX man pages"
license = "custom:posix"
url = "https://pubs.opengroup.org/onlinepubs/9699919799/nframe.html"
source = f"https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-{pkgver[:-1]}-{pkgver[-1]}.tar.xz"
sha256 = "ce67bb25b5048b20dad772e405a83f4bc70faf051afa289361c81f9660318bc3"
options = ["!autosplit"]


def install(self):
    self.install_license("POSIX-COPYRIGHT")
    for cat in ["0p", "1p", "3p"]:
        self.install_man(f"man{cat}/*.{cat}", cat=cat, glob=True)
