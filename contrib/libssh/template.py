pkgname = "libssh"
pkgver = "0.10.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUNIT_TESTING=ON",
    "-DWITH_GSSAPI=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "heimdal-devel",
    "openssl-devel",
    "zlib-devel",
]
pkgdesc = "Library for accessing ssh client services through C libraries"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later WITH custom:openssl-exception AND BSD-2-Clause"
url = "https://www.libssh.org"
source = f"https://www.libssh.org/files/{pkgver[:pkgver.rfind('.')]}/libssh-{pkgver}.tar.xz"
sha256 = "b60e2ff7f367b9eee2b5634d3a63303ddfede0e6a18dfca88c44a8770e7e4234"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _devel(self):
    return self.default_devel()
