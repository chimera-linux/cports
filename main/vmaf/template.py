pkgname = "vmaf"
pkgver = "3.0.0"
pkgrel = 0
build_style = "meson"
meson_dir = "libvmaf"
hostmakedepends = ["meson", "nasm", "pkgconf"]
checkdepends = ["xxd"]
pkgdesc = "Perceptual video quality assessment tool developed by Netflix"
maintainer = "LeFantome <fantome137@proton.me>"
license = "BSD-2-Clause-Patent"
url = "https://github.com/Netflix/vmaf"
source = f"{url}/archive/v{pkgver}/libvmaf-{pkgver}.tar.gz"
sha256 = "7178c4833639e6b989ecae73131d02f70735fdb3fc2c7d84bc36c9c3461d93b1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("vmaf-libs")
def _(self):
    return self.default_libs()


@subpackage("vmaf-devel")
def _(self):
    return self.default_devel()
