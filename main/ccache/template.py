pkgname = "ccache"
pkgver = "4.11.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTING=ON",
    "-DREDIS_STORAGE_BACKEND=OFF",
]
# these fail cause of running grep on .o and musl has no reg_startend so shit sucks
# test.debug_compilation_dir fails because llvm objdump has different options
make_check_args = [
    "-E",
    "(test.direct|test.debug_prefix_map|test.debug_compilation_dir)",
]
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
license = "GPL-3.0-or-later"
url = "https://ccache.dev"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/ccache-{pkgver}.tar.xz"
sha256 = "319390f276123968cfa565acc3da0b1e18414374b40ff25274230e6860352125"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("usr/lib/ccache/bin/clang", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/clang++", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/cc", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/c++", "../../../bin/ccache")
