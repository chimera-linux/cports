pkgname = "libzip"
pkgver = "1.11"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_EXAMPLES=OFF",
    "-DENABLE_BZIP2=ON",
    "-DENABLE_LZMA=ON",
    "-DENABLE_OPENSSL=ON",
    "-DENABLE_ZSTD=ON",
]
hostmakedepends = [
    "cmake",
    "mandoc",
    "ninja",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["nihtest"]
pkgdesc = "C library for manipulating zip archives"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://libzip.org"
source = f"{url}/download/libzip-{pkgver}.tar.gz"
sha256 = "2afc48095d990d36fc10eb296d54f03913c7eb76e0296535d7071ad85139a319"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _(self):
    return self.default_progs()
