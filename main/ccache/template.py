pkgname = "ccache"
pkgver = "4.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF", "-DREDIS_STORAGE_BACKEND=OFF"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "perl", "asciidoc"]
makedepends = ["libzstd-devel", "zlib-devel"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.samba.org"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "51186ebe0326365f4e6131e1caa8911de7da4aa6718efc00680322d63a759517"
# test suite needs bash
options = ["!check", "lto"]

def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang++")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/cc")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/c++")
