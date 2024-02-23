pkgname = "nvtop"
pkgver = "3.1.0"
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
sha256 = "9481c45c136163574f1f16d87789859430bc90a1dc62f181b269b5edd92f01f3"
# FIXME: cfi
hardening = ["vis"]
