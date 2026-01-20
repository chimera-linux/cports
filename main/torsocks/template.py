pkgname = "torsocks"
pkgver = "2.5.0"
pkgrel = 0

build_style = "gnu_configure"

pkgdesc = "Transparent SOCKS proxying via LD_PRELOAD"
license = "GPL-2.0-or-later"
url = "https://gitlab.torproject.org/tpo/core/torsocks"

source = f"{url}/-/archive/v{pkgver}/torsocks-v{pkgver}.tar.gz"
sha256 = "0fc8e18f2dc2e12f1129054f6d5acc7ecc3f0345bb57ed653fc8c6674e6ecc7e"

hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]


makedepends = [
    "libcap-devel",
]

depends = [
    "tor",
]

configure_args = [
    "--disable-static",
]

options = ["!check"]
