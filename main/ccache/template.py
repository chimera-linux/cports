pkgname = "ccache"
pkgver = "4.10.2"
pkgrel = 3
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
    "doctest",
    "xxhash-devel",
    "zstd-devel",
]
checkdepends = ["bash", "elfutils"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.dev"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/ccache-{pkgver}.tar.xz"
sha256 = "c0b85ddfc1a3e77b105ec9ada2d24aad617fa0b447c6a94d55890972810f0f5a"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("usr/lib/ccache/bin/clang", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/clang++", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/cc", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/c++", "../../../bin/ccache")
