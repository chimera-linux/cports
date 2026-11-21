pkgname = "nvidia-xconfig"
pkgver = "620.70.06"
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
sha256 = "92150eec0cd52b94eb35b7ab4541c80d9700056ab210fb265916c3458879e03d"
# no test suite
options = ["!check"]
