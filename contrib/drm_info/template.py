pkgname = "drm_info"
pkgver = "2.6.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/drm_info"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "502fa66702d470a3e4107d85a9a2fcdc081bc1f027a341746e7267ee09a1117c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
