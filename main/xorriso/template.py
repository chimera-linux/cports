pkgname = "xorriso"
pkgver = "1.5.4.2"
_xver = "1.5.4.pl02"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-libedit",
    "--disable-libreadline",
    "MKDIR_P=mkdir -p",  # install-sh is buggy
]
makedepends = [
    "zlib-devel",
    "libbz2-devel",
    "libedit-devel",
    "acl-devel",
    "linux-headers",
]
pkgdesc = "ISO 9660 Rock Ridge Filesystem Manipulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/xorriso"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{_xver}.tar.gz"
sha256 = "3ec7393d4a9dcbf5f74309c28a415f55227ec62770b95ae993ac8d7a3b152972"
# FIXME fails to generate live
hardening = ["vis", "!cfi"]

configure_gen = []
