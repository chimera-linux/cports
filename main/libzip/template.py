pkgname = "libzip"
pkgver = "1.11.4"
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
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["nihtest"]
pkgdesc = "C library for manipulating zip archives"
license = "BSD-3-Clause"
url = "https://libzip.org"
source = f"{url}/download/libzip-{pkgver}.tar.gz"
sha256 = "82e9f2f2421f9d7c2466bbc3173cd09595a88ea37db0d559a9d0a2dc60dc722e"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _(self):
    return self.default_progs()
