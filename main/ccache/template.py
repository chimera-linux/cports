pkgname = "ccache"
pkgver = "4.10.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF", "-DREDIS_STORAGE_BACKEND=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
]
makedepends = [
    "blake3-devel",
    "fmt-devel",
    "xxhash-devel",
    "zstd-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
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
