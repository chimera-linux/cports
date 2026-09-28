pkgname = "drm_info"
pkgver = "2.9.0"
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
sha256 = "6f0ef3e0e2625361665abcb7117cf8b6971e10e4cc7250b9194642e14f0b0811"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
