pkgname = "nvidia-egl-gbm"
pkgver = "1.1.4"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "eglexternalplatform",
    "libdrm-devel",
    "libglvnd-devel",
    "mesa-gbm-devel",
]
pkgdesc = "NVIDIA EGL GBM external platform"
license = "MIT"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/egl-gbm/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9738d7961550a67f2fcca5923374d1869ac214e00e96da6393b7206e3ef293e0"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nvidia-egl-gbm-devel")
def _(self):
    return self.default_devel()
