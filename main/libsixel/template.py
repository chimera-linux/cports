pkgname = "libsixel"
pkgver = "1.10.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "gdk-pixbuf-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
]
pkgdesc = "SIXEL encoder/decoder"
maintainer = "natthias <natthias@proton.me>"
license = "MIT"
url = "https://github.com/libsixel/libsixel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b6654928bd423f92e6da39eb1f40f10000ae2cc6247247fc1882dcff6acbdfc8"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsixel-devel")
def _(self):
    return self.default_devel()


@subpackage("libsixel-progs")
def _(self):
    return self.default_progs()
