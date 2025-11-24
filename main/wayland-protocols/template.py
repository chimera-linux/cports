pkgname = "wayland-protocols"
pkgver = "1.46"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "83afedde1e63751578ba51b5f6c36052802f85634ed68be41ecfcc3a515ab03d"
# check conditional
options = []

if self.profile().arch in ["armv7", "loongarch64", "riscv64"]:
    # several pedantic tests complain about symbol not found
    options += ["!check"]


def post_install(self):
    self.install_license("COPYING")
