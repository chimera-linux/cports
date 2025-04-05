pkgname = "gtk-session-lock"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = ["gtk+3-devel", "vala", "wayland-devel"]
pkgdesc = "Library for Wayland screen lockers"
license = "GPL-3.0-only AND MIT"
url = "https://github.com/Cu3PO42/gtk-session-lock"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a4245c6930580c15ed263b9a7bb7e39f47693baec78be1026b4e0e28b233cb4e"
# left over from gtk-layer-shell
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE_MIT.txt")


@subpackage("gtk-session-lock-devel")
def _(self):
    return self.default_devel()
