pkgname = "rkdeveloptool"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "scdoc",
]
makedepends = ["libusb-devel"]
pkgdesc = "Fastboot-like tool for Rockchip devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/pine64-org/quartz-bsp/rkdeveloptool"
source = f"{url}/-/archive/{pkgver}/rkdeveloptool-{pkgver}.tar.gz"
sha256 = "6622e51e2f3ec1e7f28c86693a36631948f269b02eb013e014ad83f0e407adda"


def post_install(self):
    self.install_dir("usr/share")
    self.rename("usr/man", "usr/share/man", relative=False)
