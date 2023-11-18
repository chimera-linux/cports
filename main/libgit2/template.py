pkgname = "libgit2"
pkgver = "1.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SSH=ON",
    "-DREGEX_BACKEND=pcre2",
    "-DUSE_BUNDLED_ZLIB=OFF",
    "-DUSE_HTTP_PARSER=system",
    "-DUSE_HTTPS=OpenSSL",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = [
    "heimdal-devel",
    "zlib-devel",
    "libssh2-devel",
    "openssl-devel",
    "http-parser-devel",
    "pcre2-devel",
]
pkgdesc = "Linkable library for using git"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-2.0-only WITH GCC-exception-2.0"
url = "https://libgit2.org"
source = f"https://github.com/libgit2/libgit2/archive/v{pkgver}.tar.gz"
sha256 = "17d2b292f21be3892b704dddff29327b3564f96099a1c53b00edc23160c71327"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libgit2-devel")
def _devel(self):
    return self.default_devel()
