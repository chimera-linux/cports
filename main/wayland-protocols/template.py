pkgname = "wayland-protocols"
pkgver = "1.41"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland compositor protocols"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/{pkgver}/wayland-protocols-{pkgver}.tar.gz"
sha256 = "f25b0d00f3c610158b00b57b1b7b6e59c4bfd4d91aed46f24d9eba7acf220788"


def post_install(self):
    self.install_license("COPYING")
