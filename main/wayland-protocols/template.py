pkgname = "wayland-protocols"
pkgver = "1.44"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "a8670a81a92a7108deff767a7b725afaa819b6c5a8b857cba41eac6acba783eb"
# check conditional
options = []

if self.profile().arch in ["armv7", "loongarch64", "riscv64"]:
    # several pedantic tests complain about symbol not found
    options += ["!check"]


def post_install(self):
    self.install_license("COPYING")
