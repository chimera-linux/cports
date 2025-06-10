pkgname = "wev"
pkgver = "1.1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf", "scdoc", "wayland-progs"]
makedepends = [
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland event viewer"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/wev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "89b8d9bc756631795ee91c99a0d5b0877c9f5c3acfe81f77a2b69ecfc15daf16"
hardening = ["vis", "cfi"]
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
