pkgname = "libssh"
pkgver = "0.11.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later WITH custom:openssl-exception AND BSD-2-Clause"
url = "https://www.libssh.org"
source = f"https://www.libssh.org/files/{pkgver[:pkgver.rfind('.')]}/libssh-{pkgver}.tar.xz"
sha256 = "860e814579e7606f3fc3db98c5807bef2ab60f793ec871d81bcd23acdcdd3e91"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("BSD")
    self.install_license("COPYING")


@subpackage("libssh-devel")
def _(self):
    return self.default_devel()
