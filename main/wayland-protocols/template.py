pkgname = "wayland-protocols"
pkgver = "1.45"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "460dad72a6c84b2a7d80745bee43d96ba117f4e3dfc4d7c45f83f66469ea27df"
# check conditional
options = []

if self.profile().arch in ["armv7", "loongarch64", "riscv64"]:
    # several pedantic tests complain about symbol not found
    options += ["!check"]


def post_install(self):
    self.install_license("COPYING")
