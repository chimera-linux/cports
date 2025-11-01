pkgname = "inih"
pkgver = "62"
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
sha256 = "9c15fa751bb8093d042dae1b9f125eb45198c32c6704cd5481ccde460d4f8151"
# CFI: breaks xdg-desktop-portal-wlr when it loads an empty config
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("inih-devel")
def _(self):
    return self.default_devel()
