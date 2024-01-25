pkgname = "inih"
pkgver = "58"
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
sha256 = "e79216260d5dffe809bda840be48ab0eec7737b2bb9f02d2275c1b46344ea7b7"
# FIXME: cfi breaks xdg-desktop-portal-wlr when it loads an empty config
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _devel(self):
    return self.default_devel()
