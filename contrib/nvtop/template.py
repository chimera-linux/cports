pkgname = "nvtop"
pkgver = "3.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTING=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "gtest-devel",
    "libdrm-devel",
    "ncurses-devel",
    "udev-devel",
]
pkgdesc = "GPU process monitor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/Syllo/nvtop"
source = f"https://github.com/Syllo/nvtop/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "63fa45a2d675fe5320704850c216da6a6bb2edaf09821c26b3800fa7744bae00"
# FIXME: cfi
hardening = ["vis"]
