pkgname = "libsfdo"
pkgver = "0.1.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "Libraries for Freedesktop specifications"
license = "BSD-2-Clause"
url = "https://gitlab.freedesktop.org/vyivel/libsfdo"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "3de485e2ea8bcb46f8673a8c3bc8dacb43c3d7e4e662233b11b877d9259f0921"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsfdo-devel")
def _(self):
    return self.default_devel()
