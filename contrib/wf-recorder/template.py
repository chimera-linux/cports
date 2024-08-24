pkgname = "wf-recorder"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
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
source = f"{url}/releases/download/v{pkgver}/wf-recorder-{pkgver}.tar.xz"
sha256 = "50b30569f9ecf4f6ba5ba76c422b7af652b4fbc7cae86c25e19ecbe669fca327"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
