pkgname = "iotop"
pkgver = "1.30"
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
sha256 = "862e3d3d0263e4171aa9c5aaed2dd7d76ca746afa58ecbb6eca002717e9fa240"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
