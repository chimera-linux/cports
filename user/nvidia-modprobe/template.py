pkgname = "nvidia-modprobe"
pkgver = "620.70.06"
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
sha256 = "8c2346cafe23a9f85de82913dd4114e3b3728af2c696da088b1a801db487f7d5"
file_modes = {"usr/bin/nvidia-modprobe": ("root", "root", 0o4755)}
# no test suite
options = ["!check"]
