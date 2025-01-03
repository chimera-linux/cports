pkgname = "ignis"
pkgver = "0.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "git",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "libpulse-devel",
]
depends = [
    "gtk4-layer-shell",
    "python-click",
    "python-cairo",
    "python-gobject",
    "python-loguru",
    "python-requests",
]
pkgdesc = "GTK4 Python widget system for building desktop shells"
maintainer = "supermikea <mikewiegmanavila@keemail.me>"
license = "GPL-3.0-only"
url = "https://github.com/linkfrg/ignis"
source = f"{url}/releases/download/v{pkgver}/ignis-v{pkgver}.tar.gz"
sha256 = "dc8a8d76b80bea19497f6029b8ab816e5eceb2f2ff9697675bd1ac87ada70513"


def post_install(self):
    self.install_license("LICENSE")
