pkgname = "cwm"
pkgver = "7.4"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["byacc", "pkgconf"]
makedepends = [
    "libxft-devel",
    "libxrandr-devel",
]
pkgdesc = "Lightweight and efficient window manager for X11"
license = "ISC"
url = "https://github.com/leahneukirchen/cwm"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b4f275143c8c716d7df1cfbb230f888c72aa861708e144d1749858f1cc6fcac0"
# no tests
options = ["!check"]


def install(self):
    self.install_license("LICENSE")
    self.install_bin(pkgname)
