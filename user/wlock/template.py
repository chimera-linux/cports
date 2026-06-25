pkgname = "wlock"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Itsy-bitsy sessionlocker for Wayland"
license = "GPL-3.0-only"
url = "https://codeberg.org/sewn/wlock"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "f9b3b540f4f3973c702ad1b0cf4bfc7ac436fac6cb7383abc73cc93d9de8f145"
file_modes = {
    "usr/bin/wlock": ("root", "root", 0o4755),
}
hardening = ["vis", "cfi"]
# no tests provided by upstream
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
