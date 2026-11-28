pkgname = "nvidia-egl-x11"
pkgver = "1.0.6"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "eglexternalplatform",
    "libdrm-devel",
    "libglvnd-devel",
    "libx11-devel",
    "libxcb-devel",
    "mesa-gbm-devel",
]
pkgdesc = "NVIDIA EGL X11 external platform"
license = "MIT"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/egl-x11/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "370870b0dea12dde0ddac0b77594ff94215cf2694ac0a5ded98f5d2f9864f6e0"


def post_install(self):
    self.install_license("LICENSE")
