pkgname = "ccache"
version = "4.2.1"
revision = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF"]
hostmakedepends = ["cmake", "ninja", "perl"]
makedepends = ["libzstd-devel", "zlib-devel"]
short_desc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
homepage = "https://ccache.samba.org"
distfiles = [f"https://github.com/ccache/ccache/releases/download/v{version}/{pkgname}-{version}.tar.xz"]
checksum = ["9d6ba1cdefdc690401f404b747d81a9a1802b17af4235815866b7620d980477e"]

def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("../../../ccache", "usr/lib/ccache/bin/clang")
    self.install_link("../../../ccache", "usr/lib/ccache/bin/clang++")
    self.install_link("../../../ccache", "usr/lib/ccache/bin/cc")
    self.install_link("../../../ccache", "usr/lib/ccache/bin/c++")
