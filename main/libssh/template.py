pkgname = "libssh"
pkgver = "0.11.3"
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
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for accessing ssh client services through C libraries"
license = "LGPL-2.1-or-later WITH custom:openssl-exception AND BSD-2-Clause"
url = "https://www.libssh.org"
source = f"https://www.libssh.org/files/{pkgver[: pkgver.rfind('.')]}/libssh-{pkgver}.tar.xz"
sha256 = "7d8a1361bb094ec3f511964e78a5a4dba689b5986e112afabe4f4d0d6c6125c3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _(self):
    return self.default_devel()
