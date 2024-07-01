pkgname = "ccache"
pkgver = "4.10.1"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTING=ON",
    "-DREDIS_STORAGE_BACKEND=OFF",
]
# these fail cause of running grep on .o and musl has no reg_startend so shit sucks
make_check_args = ["-E", "(test.direct|test.debug_prefix_map)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
]
makedepends = [
    "blake3-devel",
    "doctest",
    "xxhash-devel",
    "zstd-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash", "elfutils"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.dev"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3a43442ce3916ea48bb6ccf6f850891cbff01d1feddff7cd4bbd49c5cf1188f6"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("usr/lib/ccache/bin/clang", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/clang++", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/cc", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/c++", "../../../bin/ccache")
