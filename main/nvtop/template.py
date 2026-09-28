pkgname = "nvtop"
pkgver = "3.2.0"
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
license = "GPL-3.0-or-later"
url = "https://github.com/Syllo/nvtop"
source = f"https://github.com/Syllo/nvtop/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d26df685455023cedc4dda033862dcddb67402fbdb685da70da78492f73c41d0"
hardening = ["vis", "!cfi"]
