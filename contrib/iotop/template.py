pkgname = "iotop"
pkgver = "1.26"
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
sha256 = "211e8719dd762edf71c769c1bc80bf8f47bb28c4475486cf71fcbaf34baa9fb9"
# FIXME cfi
hardening = ["vis"]
# no tests
options = ["!check"]
