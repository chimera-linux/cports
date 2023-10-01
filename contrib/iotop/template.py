pkgname = "iotop"
pkgver = "1.24"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Top-like utility for IO"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/Tomas-M/iotop"
source = f"https://github.com/Tomas-M/iotop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96921047354ea988349c730f88accd06bb10ced04038509952095f5654d2415a"
# FIXME cfi
hardening = ["vis"]
# no tests
options = ["!check"]
