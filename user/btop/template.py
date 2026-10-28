pkgname = "btop"
pkgver = "1.4.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
checkdepends = ["gtest-devel"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "67e07c21b770a6d884c5e50ba1d2cfc90732ea57459367d8732ec7ecbeb3be5f"
hardening = ["cfi", "vis"]
