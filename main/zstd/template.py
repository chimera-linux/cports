pkgname = "zstd"
pkgver = "1.5.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dbin_contrib=true",
    "-Dlz4=enabled",
    "-Dlzma=enabled",
    "-Dzlib=enabled",
]
make_dir = "mbuild"
meson_dir = "build/meson"
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["zlib-devel", "xz-devel", "lz4-devel"]
checkdepends = ["gtest-devel"]
provides = [f"libzstd={pkgver}-r{pkgrel}"]
pkgdesc = "Zstd compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.zstd.net"
source = f"https://github.com/facebook/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "8c29e06cf42aacc1eafc4077ae2ec6c6fcb96a626157e0593d5e82a34fd403c1"
hardening = ["!cfi"]  # TODO
# checkdepends not available yet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    for tool in ["zstdgrep", "zstdless"]:
        self.rm(self.destdir / "usr/bin" / tool)
        self.rm(self.destdir / "usr/share/man/man1" / (tool + ".1"))


@subpackage("zstd-devel")
def _devel(self):
    self.provides = [f"libzstd-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()
