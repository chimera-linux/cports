pkgname = "cwm"
pkgver = "7.4"
pkgrel = 1
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
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def pre_install(self):
    self.install_license("LICENSE")
