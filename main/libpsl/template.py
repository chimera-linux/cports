pkgname = "libpsl"
pkgver = "0.23.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["icu-devel", "libidn2-devel", "libunistring-devel"]
pkgdesc = "Public Suffix List library"
license = "MIT"
url = "https://rockdaboot.github.io/libpsl"
source = f"https://github.com/rockdaboot/libpsl/releases/download/{pkgver}/libpsl-{pkgver}.tar.gz"
sha256 = "93941f85a1e7bd593fa94f299233cb5dfc91cd144fd9a78a6ceb75001c5b03be"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libpsl-devel")
def _(self):
    return self.default_devel()
