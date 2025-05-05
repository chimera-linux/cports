pkgname = "iotop"
pkgver = "1.28"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Top-like utility for IO"
license = "GPL-2.0-or-later"
url = "https://github.com/Tomas-M/iotop"
source = f"https://github.com/Tomas-M/iotop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b83e5c7d82da3bfb3e46b74e91b24a52fc65d44ff268ace95b613972e27fc678"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
