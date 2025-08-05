pkgname = "inih"
pkgver = "61"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddistro_install=true",
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Simple ini parser library"
license = "BSD-3-Clause"
url = "https://github.com/benhoyt/inih"
source = f"{url}/archive/r{pkgver}.tar.gz"
sha256 = "7caf26a2202a4ca689df3fe4175dfa74e0faa18fcca07331bba934fd0ecb8f12"
# CFI: breaks xdg-desktop-portal-wlr when it loads an empty config
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _(self):
    return self.default_devel()
