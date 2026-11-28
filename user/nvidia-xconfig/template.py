pkgname = "nvidia-xconfig"
pkgver = "620.73.04"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "makefile"
make_install_args = ["DO_STRIP="]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libpciaccess-devel"]
pkgdesc = "NVIDIA xorg.conf configurator"
license = "GPL-2.0-or-later"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/nvidia-xconfig/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e90083d834ec1c9b35013ae433a975c32fcb93b6500d8c0613487436678cd283"
# no test suite
options = ["!check"]
