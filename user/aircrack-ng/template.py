pkgname = "aircrack-ng"
pkgver = "1.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-experimental"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "cmocka-devel",
    "ethtool",
    "hwloc-devel",
    "libnl-devel",
    "libpcap-devel",
    "linux-headers",
    "openssl3-devel",
    "sqlite-devel",
    "util-linux-rfkill",
    "zlib-ng-devel",
]
pkgdesc = "WiFi security auditing tools suite"
license = "GPL-2.0-or-later AND OpenSSL"
url = "https://www.aircrack-ng.org"
source = f"https://download.aircrack-ng.org/aircrack-ng-{pkgver}.tar.gz"
sha256 = "05a704e3c8f7792a17315080a21214a4448fd2452c1b0dd5226a3a55f90b58c3"


def post_patch(self):
    (self.cwd / "AC_VERSION").write_text(self.pkgver)


@subpackage("aircrack-ng-devel")
def _(self):
    return self.default_devel()
