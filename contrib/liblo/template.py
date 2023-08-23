pkgname = "liblo"
pkgver = "0.31"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Open Sound Control protocol implementation for POSIX systems"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://liblo.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/liblo/{pkgver}/liblo-{pkgver}.tar.gz"
sha256 = "2b4f446e1220dcd624ecd8405248b08b7601e9a0d87a0b94730c2907dbccc750"
# vis breaks symbols
hardening = []
# fails in chroot networking
options = ["!check"]


@subpackage("liblo-devel")
def _devel(self):
    return self.default_devel()


@subpackage("liblo-progs")
def _progs(self):
    return self.default_progs()
