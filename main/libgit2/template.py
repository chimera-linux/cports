pkgname = "libgit2"
pkgver = "1.8.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SSH=ON",
    "-DREGEX_BACKEND=pcre2",
    "-DUSE_BUNDLED_ZLIB=OFF",
    "-DUSE_HTTP_PARSER=http-parser",
    "-DUSE_HTTPS=OpenSSL",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "heimdal-devel",
    "http-parser-devel",
    "libssh2-devel",
    "openssl-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Linkable library for using git"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-2.0-only WITH GCC-exception-2.0"
url = "https://libgit2.org"
source = f"https://github.com/libgit2/libgit2/archive/v{pkgver}.tar.gz"
sha256 = "8c1eaf0cf07cba0e9021920bfba9502140220786ed5d8a8ec6c7ad9174522f8e"


def post_extract(self):
    # zlib-ng deflate generates different data
    self.rm("tests/libgit2/pack/packbuilder.c")


def post_install(self):
    self.install_license("COPYING")


@subpackage("libgit2-devel")
def _(self):
    return self.default_devel()


@subpackage("libgit2-progs")
def _(self):
    return self.default_progs()
