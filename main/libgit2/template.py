pkgname = "libgit2"
pkgver = "1.6.4"
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
sha256 = "d25866a4ee275a64f65be2d9a663680a5cf1ed87b7ee4c534997562c828e500d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libgit2-devel")
def _devel(self):
    return self.default_devel()
