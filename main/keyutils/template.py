pkgname = "keyutils"
pkgver = "1.6.3"
pkgrel = 0
build_style = "makefile"
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
hostmakedepends = ["file", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Linux key management utilities"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://people.redhat.com/~dhowells/keyutils"
source = f"https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/keyutils-{pkgver}.tar.gz"
sha256 = "a61d5706136ae4c05bd48f86186bcfdbd88dd8bd5107e3e195c924cfc1b39bb4"
# needs rpm
options = ["!check", "linkundefver"]


@subpackage("keyutils-libs")
def _(self):
    return self.default_libs()


@subpackage("keyutils-devel")
def _(self):
    return self.default_devel()
