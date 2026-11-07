pkgname = "nvidia-egl-wayland"
pkgver = "1.1.24"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "eglexternalplatform",
    "libdrm-devel",
    "libglvnd-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "NVIDIA EGL Wayland external platform"
license = "MIT"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = (
    f"https://github.com/NVIDIA/egl-wayland/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "4297ebcbe1476347519971c41be648e748aee0e2fdbff4a84bd3b52ef665dcab"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nvidia-egl-wayland-devel")
def _(self):
    return self.default_devel()
