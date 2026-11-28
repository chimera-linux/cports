pkgname = "nvidia-modprobe"
pkgver = "620.73.04"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "makefile"
make_install_args = ["DO_STRIP="]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "NVIDIA modprobe helper"
license = "GPL-2.0-or-later"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/nvidia-modprobe/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "69e27df09567fef58b329b615a32da268902e7504b40747b6de3174168ac8cde"
file_modes = {"usr/bin/nvidia-modprobe": ("root", "root", 0o4755)}
# no test suite
options = ["!check"]
