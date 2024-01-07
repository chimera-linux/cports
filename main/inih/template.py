pkgname = "inih"
pkgver = "57"
pkgrel = 1
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
sha256 = "f03f98ca35c3adb56b2358573c8d3eda319ccd5287243d691e724b7eafa970b3"
# FIXME: cfi breaks xdg-desktop-portal-wlr when it loads an empty config
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _devel(self):
    return self.default_devel()
