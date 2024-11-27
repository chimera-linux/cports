pkgname = "liblo"
pkgver = "0.32"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Open Sound Control protocol implementation for POSIX systems"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://liblo.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/liblo/{pkgver}/liblo-{pkgver}.tar.gz"
sha256 = "5df05f2a0395fc5ac90f6b538b8c82bb21941406fd1a70a765c7336a47d70208"
# vis breaks symbols
hardening = []
# fails in chroot networking
options = ["!check"]


@subpackage("liblo-devel")
def _(self):
    return self.default_devel()


@subpackage("liblo-progs")
def _(self):
    return self.default_progs()
