pkgname = "cwm"
pkgver = "7.9"
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
sha256 = "ec75056a5f57980d9f57076c4ae7d25a1e6903ea4e793c0a04b98e25edb0fc90"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def pre_install(self):
    self.install_license("LICENSE")
