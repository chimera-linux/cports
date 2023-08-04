pkgname = "libzip"
pkgver = "1.10.0"
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
sha256 = "52a60b46182587e083b71e2b82fcaaba64dd5eb01c5b1f1bc71069a3858e40fe"
hardening = ["vis", "int"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _progs(self):
    return self.default_progs()
