pkgname = "xcursorgen"
pkgver = "1.0.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = [
    "libpng-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxfixes-devel",
    "libxrender-devel",
]
pkgdesc = "X cursor generator"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xcursorgen-{pkgver}.tar.gz"
sha256 = "21082be975472e469dd79d46166cee3720fda80a54382dc8d03fa7a4cd39837a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
