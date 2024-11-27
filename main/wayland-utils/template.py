pkgname = "wayland-utils"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "libdrm-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland-info utility to display supported protocols"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wayland/wayland-utils"
source = f"{url}/-/releases/{pkgver}/downloads/wayland-utils-{pkgver}.tar.xz"
sha256 = "d9278c22554586881802540751bcc42569262bf80cd9ac9b0fd12ff4bd09a9e4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
