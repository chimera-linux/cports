pkgname = "libssh"
pkgver = "0.11.2"
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
sha256 = "69529fc18f5b601f0baf0e5a4501a2bc26df5e2f116f5f8f07f19fafaa6d04e7"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _(self):
    return self.default_devel()
