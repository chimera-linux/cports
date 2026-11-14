pkgname = "aircrack-ng"
pkgver = "1.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-experimental",
    "--with-ext-scripts",
    "--without-opt",
]
hostmakedepends = [
    "automake",
    "ethtool",
    "libtool",
    "pkgconf",
    "python-setuptools",
    "util-linux-rfkill",
]
makedepends = [
    "hwloc-devel",
    "libnl-devel",
    "libpcap-devel",
    "linux-headers",
    "openssl3-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
checkdepends = [
    "cmocka-devel",
]
depends = [
    "graphviz",
    "python-requests",
]
pkgdesc = "WiFi security auditing tools suite"
license = "GPL-2.0-or-later AND OpenSSL"
url = "https://www.aircrack-ng.org"
source = f"https://download.aircrack-ng.org/aircrack-ng-{pkgver}.tar.gz"
sha256 = "05a704e3c8f7792a17315080a21214a4448fd2452c1b0dd5226a3a55f90b58c3"


def post_extract(self):
    with open(self.cwd / "AC_VERSION", "w") as f:
        f.write(pkgver)


@subpackage("aircrack-ng-devel")
def _(self):
    return self.default_devel()
