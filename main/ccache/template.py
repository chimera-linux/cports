pkgname = "ccache"
pkgver = "4.14.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTING=ON",
    "-DREDIS_STORAGE_BACKEND=OFF",
]
# these fail cause of running grep on .o and musl has no reg_startend so shit sucks
# test.debug_compilation_dir fails because llvm objdump has different options
# test.inode_cache needs gnu stat(1)
make_check_args = [
    "-E",
    "test.(direct|debug_prefix_map|debug_compilation_dir|inode_cache)",
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
sha256 = "e1999132cf7dbce48de7d946b767f3e26ea09adcb5daa4a7103a8fa09ee0637d"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]
# check may be disabled
options = []

if self.profile.arch in ["loongarch64"]:
    # some file permissions weirdness: Expected permissions for remote to be drwxr-x-wx, actual drwxr-s-wx
    options += ["!check"]
