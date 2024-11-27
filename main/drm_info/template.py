pkgname = "drm_info"
pkgver = "2.7.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/drm_info"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "6a810415d798235c61e69920de1fe923f493c4d3f3027102f4542bbdddf8f795"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
