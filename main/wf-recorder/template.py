pkgname = "wf-recorder"
pkgver = "0.6.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "ffmpeg-devel",
    "mesa-devel",
    "pipewire-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Screen recorder for wlroots-based compositors"
license = "MIT"
url = "https://github.com/ammen99/wf-recorder"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "52d2c952506d63708f9a8f1aacd4d6ca176287caf3507c8ff2882fa0390cb391"


def post_install(self):
    self.install_license("LICENSE")
