pkgname = "ccache"
pkgver = "4.12.1"
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
sha256 = "42e6c4b260cffd92dfa755e26390f45f5842e8c1a5f64f2b2e68adfbe82d1542"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]
# check may be disabled
options = []

if self.profile().arch in ["loongarch64"]:
    # some file permissions weirdness: Expected permissions for remote to be drwxr-x-wx, actual drwxr-s-wx
    options += ["!check"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("usr/lib/ccache/bin/clang", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/clang++", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/cc", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/c++", "../../../bin/ccache")
