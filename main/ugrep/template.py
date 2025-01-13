pkgname = "ugrep"
pkgver = "7.1.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://ugrep.com"
source = f"https://github.com/Genivia/ugrep/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "99bbccd7a192fb11070fa75f4d8adaa1379d0a27dd3cbc1f78e1bace1c2d0e46"


def post_install(self):
    self.install_license("LICENSE.txt")
