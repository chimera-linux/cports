pkgname = "wayland-protocols"
pkgver = "1.43"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "05fc0ff0c6b3081549d8f81c6b584076a20be18e8c2b9be65ae09ce05e5aea9e"
# check conditional
options = []

if self.profile().arch in ["armv7", "loongarch64", "riscv64"]:
    # several pedantic tests complain about symbol not found
    options += ["!check"]


def post_install(self):
    self.install_license("COPYING")
