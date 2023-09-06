pkgname = "wf-recorder"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "ffmpeg-devel",
    "libpulse-devel",
    "mesa-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Screen recorder for wlroots-based compositors"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ammen99/wf-recorder"
source = f"https://github.com/ammen99/wf-recorder/releases/download/v{pkgver}/wf-recorder-{pkgver}.tar.xz"
sha256 = "502ba54db8aaf5ebd280738f065c73409694a1440b9a660ef5c4e398714c51f7"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
