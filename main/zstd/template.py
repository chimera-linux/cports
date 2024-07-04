pkgname = "zstd"
pkgver = "1.5.6"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Db_ndebug=true",
    "-Dbin_contrib=true",
    "-Dbin_tests=true",
    "-Dlz4=enabled",
    "-Dlzma=enabled",
    "-Dzlib=enabled",
]
make_dir = "mbuild"
meson_dir = "build/meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["lz4-devel", "xz-devel", "zlib-ng-compat-devel"]
provides = [f"libzstd={pkgver}-r{pkgrel}"]
pkgdesc = "Zstd compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.zstd.net"
source = f"https://github.com/facebook/zstd/releases/download/v{pkgver}/zstd-{pkgver}.tar.gz"
sha256 = "8c29e06cf42aacc1eafc4077ae2ec6c6fcb96a626157e0593d5e82a34fd403c1"
compression = "deflate"
hardening = ["!cfi"]  # TODO


def post_install(self):
    self.install_license("LICENSE")
    for tool in ["zstdgrep", "zstdless"]:
        self.uninstall(f"usr/bin/{tool}")
        self.uninstall(f"usr/share/man/man1/{tool}.1")


@subpackage("zstd-progs")
def _progs(self):
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_progs()


@subpackage("zstd-devel")
def _devel(self):
    self.provides = [f"libzstd-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()
