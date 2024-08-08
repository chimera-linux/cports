pkgname = "ugrep"
pkgver = "6.4.0"
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
sha256 = "4d28168a8b6c2fa7f39ec524f25625c10f3a5a1a9b718f71aee8dd6bc51e6eb5"


def post_install(self):
    self.install_license("LICENSE.txt")
