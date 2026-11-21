pkgname = "nvidia-persistenced"
pkgver = "620.70.06"
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
sha256 = "2e0f9532a5a2d6f02b4d8c26626a15c36714fdceaa0b22aa35a87874b3e4e558"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
