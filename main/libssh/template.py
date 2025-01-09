pkgname = "libssh"
pkgver = "0.11.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUNIT_TESTING=ON",
    "-DWITH_GSSAPI=ON",
]
make_check_args = ["-E", "torture_config_match_localnetwork"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "heimdal-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for accessing ssh client services through C libraries"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later WITH custom:openssl-exception AND BSD-2-Clause"
url = "https://www.libssh.org"
source = f"https://www.libssh.org/files/{pkgver[: pkgver.rfind('.')]}/libssh-{pkgver}.tar.xz"
sha256 = "14b7dcc72e91e08151c58b981a7b570ab2663f630e7d2837645d5a9c612c1b79"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _(self):
    return self.default_devel()
