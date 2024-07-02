pkgname = "libsfdo"
pkgver = "0.1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "Libraries for Freedesktop specifications"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://gitlab.freedesktop.org/vyivel/libsfdo"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "50e6d97419b021d072c4388b5fbf492c7ae64ddc731304307f02992d05ab5a06"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsfdo-devel")
def _devel(self):
    return self.default_devel()
