pkgname = "iotop"
pkgver = "1.29"
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
sha256 = "8afcd3f2a91a5246c4b187e39cb87fafdb5c2dd27a0386fb8381361c271f8f60"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
