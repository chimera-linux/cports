pkgname = "drm_info"
pkgver = "2.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "json-c-devel",
    "libdrm-devel",
    "pciutils-devel",
]
pkgdesc = "Utility to dump info about DRM devices"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/drm_info"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "e9709d10e93734bff13f29a44378cb2ee92fe02b32bef4271343b8e1975c7b7e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
