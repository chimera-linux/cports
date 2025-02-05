pkgname = "libzip"
pkgver = "1.11.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libzip.org"
source = f"{url}/download/libzip-{pkgver}.tar.gz"
sha256 = "76653f135dde3036036c500e11861648ffbf9e1fc5b233ff473c60897d9db0ea"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libzip-devel")
def _(self):
    return self.default_devel()


@subpackage("libzip-progs")
def _(self):
    return self.default_progs()
