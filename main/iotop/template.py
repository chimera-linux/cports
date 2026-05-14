pkgname = "iotop"
pkgver = "1.31"
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
sha256 = "658a615eb1def9dddcf0c325efebb4f78b101a040fff33ef7afaaa39c2471669"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
