pkgname = "libsfdo"
pkgver = "0.1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
pkgdesc = "Libraries for Freedesktop specifications"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gitlab.freedesktop.org/vyivel/libsfdo"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "a792ae8545d532703b7b61a65b4630936f50711f290fc59d57d13839c849bcec"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsfdo-devel")
def _(self):
    return self.default_devel()
