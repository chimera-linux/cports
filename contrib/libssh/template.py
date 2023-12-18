pkgname = "libssh"
pkgver = "0.10.6"
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
sha256 = "1861d498f5b6f1741b6abc73e608478491edcf9c9d4b6630eef6e74596de9dc1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _devel(self):
    return self.default_devel()
