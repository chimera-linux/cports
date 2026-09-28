pkgname = "intel-vaapi-driver"
pkgver = "2.4.1"
pkgrel = 0
# only usable here
archs = ["x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libva-devel", "libx11-devel"]
pkgdesc = "VA-API driver for Haswell and older Intel GPUs"
license = "MIT"
url = "https://github.com/intel/intel-vaapi-driver"
source = f"{url}/releases/download/{pkgver}/intel-vaapi-driver-{pkgver}.tar.bz2"
sha256 = "0081fce08eb3a83f7d99c3b853c8fdfa0af437b8f5b0fb7c66faeb83bcbe0c19"


def post_install(self):
    self.install_license("COPYING")
