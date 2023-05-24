pkgname = "inih"
pkgver = "56"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddistro_install=true",
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Simple ini parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/benhoyt/inih"
source = f"{url}/archive/r{pkgver}.tar.gz"
sha256 = "4f2ba6bd122d30281a8c7a4d5723b7af90b56aa828c0e88256d7fceda03a491a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _devel(self):
    return self.default_devel()
