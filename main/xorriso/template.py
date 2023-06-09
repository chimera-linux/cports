pkgname = "xorriso"
pkgver = "1.5.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-libedit",
    "--disable-libreadline",
    "MKDIR_P=mkdir -p",  # install-sh is buggy
]
# won't configure
configure_gen = []
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
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d4b6b66bd04c49c6b358ee66475d806d6f6d7486e801106a47d331df1f2f8feb"
# FIXME fails to generate live
hardening = ["vis", "!cfi"]
