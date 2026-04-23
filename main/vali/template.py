pkgname = "vali"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["aml-devel", "json-c-devel"]
pkgdesc = "C library and code generator for Varlink"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/vali"
source = f"{url}/-/releases/v{pkgver}/downloads/vali-{pkgver}.tar.gz"
sha256 = "791785eca66392f91f28ca371ba9cfa2dc11915df0bff9f590a33453f67e5756"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("vali-devel")
def _(self):
    return self.default_devel()
