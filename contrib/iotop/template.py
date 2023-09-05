pkgname = "iotop"
pkgver = "1.23"
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
sha256 = "a2a620841f0c49caba590a730a15a546464e4aa337bbaa018eb7b6c92bc7a738"
# FIXME cfi
hardening = ["vis"]
# no tests
options = ["!check"]
