pkgname = "nvidia-persistenced"
pkgver = "620.73.04"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "makefile"
make_install_args = ["DO_STRIP="]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libtirpc-devel"]
pkgdesc = "NVIDIA driver persistence daemon"
license = "MIT"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/nvidia-persistenced/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "74b4ae5a6aca61362d078fe2ebd37cd4a9121b85fc1937c4a6a2190dcac655b6"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
