pkgname = "zstd"
pkgver = "1.5.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dzlib=enabled", "-Dlzma=enabled", "-Dlz4=enabled", "-Dbin_contrib=true"
]
meson_dir = "build/meson"
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["zlib-devel", "liblzma-devel", "liblz4-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "Zstd compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.zstd.net"
source = f"https://github.com/facebook/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9c4396cc829cfae319a6e2615202e82aad41372073482fce286fac78646d3ee4"
hardening = ["!cfi"] # TODO
# checkdepends not available yet
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    for tool in [
        "zstdgrep", "zstdless"
    ]:
        self.rm(self.destdir / "usr/bin" / tool)
        self.rm(self.destdir / "usr/share/man/man1" / (tool + ".1"))

@subpackage("libzstd")
def _lib(self):
    self.pkgdesc = "Fast real-time compression algorithm"

    return self.default_libs()

@subpackage("libzstd-devel")
def _devel(self):
    self.pkgdesc = "Fast real-time compression algorithm (development files)"

    return self.default_devel()
