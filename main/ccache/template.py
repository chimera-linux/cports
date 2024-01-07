pkgname = "ccache"
pkgver = "4.9"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF", "-DREDIS_STORAGE_BACKEND=OFF"]
hostmakedepends = ["cmake", "ninja", "perl"]
makedepends = ["zstd-devel", "zlib-devel"]
checkdepends = ["bash"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.samba.org"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1ebc72324e3ab52af0b562bf54189d108e85eef6478d6304a345a3c2dc4018e0"
hardening = ["vis", "cfi"]
# not properly set up
options = ["!check"]


def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang++")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/cc")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/c++")
