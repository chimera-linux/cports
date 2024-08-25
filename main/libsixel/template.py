pkgname = "libsixel"
pkgver = "1.10.3"
pkgrel = 1
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
sha256 = "028552eb8f2a37c6effda88ee5e8f6d87b5d9601182ddec784a9728865f821e0"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsixel-devel")
def _(self):
    return self.default_devel()


@subpackage("libsixel-progs")
def _(self):
    return self.default_progs()
