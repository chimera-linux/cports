pkgname = "xorriso"
pkgver = "1.5.6.2"
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
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver[:-2]}.pl0{pkgver[-1:]}.tar.gz"
sha256 = "786f9f5df9865cc5b0c1fecee3d2c0f5e04cab8c9a859bd1c9c7ccd4964fdae1"
# FIXME fails to generate live
hardening = ["vis", "!cfi"]
