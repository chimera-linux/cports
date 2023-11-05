pkgname = "keyutils"
pkgver = "1.6.3"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "NO_ARLIB=1",
    "LIBDIR=/usr/lib",
    "USRLIBDIR=/usr/lib",
    f"VERSION={pkgver}",
    f"RELEASE=-r{pkgrel}",
]
make_install_args = [
    "NO_ARLIB=1",
    "BINDIR=/usr/bin",
    "SBINDIR=/usr/bin",
    "LIBDIR=/usr/lib",
    "USRLIBDIR=/usr/lib",
]
hostmakedepends = ["gmake", "file", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Linux key management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://people.redhat.com/~dhowells/keyutils"
source = f"https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/{pkgname}.git/snapshot/{pkgname}-{pkgver}.tar.gz"
sha256 = "a61d5706136ae4c05bd48f86186bcfdbd88dd8bd5107e3e195c924cfc1b39bb4"
# needs rpm
options = ["!check", "linkundefver"]


@subpackage("keyutils-libs")
def _libs(self):
    return self.default_libs()


@subpackage("keyutils-devel")
def _devel(self):
    return self.default_devel()
