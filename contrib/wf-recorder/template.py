pkgname = "wf-recorder"
pkgver = "0.4.0"
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
sha256 = "1d0cc9c4029adfeded29203dfcdd96532b49aba0d91b9e2dedb46796fcb11af7"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
