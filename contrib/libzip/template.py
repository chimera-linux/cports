pkgname = "libzip"
pkgver = "1.10.1"
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
    "ninja",
    "pkgconf",
]
makedepends = [
    "libbz2-devel",
    "liblzma-devel",
    "libzstd-devel",
    "zlib-devel",
]
checkdepends = ["nihtest"]
pkgdesc = "C library for manipulating zip archives"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://libzip.org"
source = f"{url}/download/libzip-{pkgver}.tar.gz"
sha256 = "9669ae5dfe3ac5b3897536dc8466a874c8cf2c0e3b1fdd08d75b273884299363"
hardening = ["vis", "int"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _progs(self):
    return self.default_progs()
