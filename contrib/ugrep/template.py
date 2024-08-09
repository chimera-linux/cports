pkgname = "ugrep"
pkgver = "6.4.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = [
    "automake",
    "gmake",
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://ugrep.com"
source = f"https://github.com/Genivia/ugrep/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a90929a36c3adfbfc493cd808b0ca1e6ca0b06932447a91eaa598ad8b377bbc4"


def post_install(self):
    self.install_license("LICENSE.txt")
