pkgname = "ccache"
pkgver = "4.10"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF", "-DREDIS_STORAGE_BACKEND=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
]
makedepends = [
    "fmt-devel",
    "xxhash-devel",
    "zstd-devel",
    "zlib-devel",
]
checkdepends = ["bash"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.dev"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "83630b5e922b998ab2538823e0cad962c0f956fad1fcf443dd5288269a069660"
# cfi crashes in fmt template expansion
hardening = ["vis", "!cfi"]
# not properly set up
options = ["!check"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("usr/lib/ccache/bin/clang", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/clang++", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/cc", "../../../bin/ccache")
    self.install_link("usr/lib/ccache/bin/c++", "../../../bin/ccache")
