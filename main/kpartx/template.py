pkgname = "kpartx"
pkgver = "0.9.3"
pkgrel = 0
build_wrksrc = "kpartx"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "prefix=/usr", "libudevdir=/usr/lib/udev", "bindir=/usr/bin"
]
hostmakedepends = ["gmake"]
makedepends = ["device-mapper-devel"]
pkgdesc = "Create device maps from partition tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://christophe.varoqui.free.fr"
source = f"https://github.com/opensvc/multipath-tools/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7d5af5d86e43b757e253d1ba244aa8a9c09bfbb1677a72accb799b1bfcc0a9ac"
# no test suite
options = ["!check"]

# FIXME visibility
hardening = ["!vis"]
