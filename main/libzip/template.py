pkgname = "libzip"
pkgver = "1.11.2"
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
sha256 = "6b2a43837005e1c23fdfee532b78f806863e412d2089b9c42b49ab08cbcd7665"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _(self):
    return self.default_progs()
