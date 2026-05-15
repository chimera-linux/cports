pkgname = "wayland-protocols"
pkgver = "1.48"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "c563af8e2e784f9599fe23819a3fc5e7d946e76db9f90a2e3ba6c9a869a52911"
# check conditional
options = []

if self.profile().arch in ["armv7", "loongarch64", "riscv64"]:
    # several pedantic tests complain about symbol not found
    options += ["!check"]


def post_install(self):
    self.install_license("COPYING")
