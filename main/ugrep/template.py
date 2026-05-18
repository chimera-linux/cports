pkgname = "ugrep"
pkgver = "7.8.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
make_check_target = "test"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "brotli-devel",
    "bzip2-devel",
    "linux-headers",
    "lz4-devel",
    "pcre2-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Grep-compatible file searcher"
license = "BSD-3-Clause"
url = "https://ugrep.com"
source = f"https://github.com/Genivia/ugrep/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f991cc6c61dbc5af5a3b3939083e917df4113509549670fb400d121f639f69f6"


def post_install(self):
    self.install_license("LICENSE.txt")
