pkgname = "inih"
pkgver = "60"
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
sha256 = "706aa05c888b53bd170e5d8aa8f8a9d9ccf5449dfed262d5103d1f292af26774"
# CFI: breaks xdg-desktop-portal-wlr when it loads an empty config
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _(self):
    return self.default_devel()
