pkgname = "libgit2"
pkgver = "1.9.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SSH=ON",
    "-DREGEX_BACKEND=pcre2",
    "-DUSE_BUNDLED_ZLIB=OFF",
    "-DUSE_HTTP_PARSER=llhttp",
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
    "libssh2-devel",
    "llhttp-devel",
    "openssl3-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Linkable library for using git"
license = "GPL-2.0-only WITH GCC-exception-2.0"
url = "https://libgit2.org"
source = f"https://github.com/libgit2/libgit2/archive/v{pkgver}.tar.gz"
sha256 = "a88a42a4ea9bdab7aa8686eead3bf7d9c6dd74529caca16ab22eaa92433d31d9"


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
