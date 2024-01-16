pkgname = "check"
pkgver = "0.15.2"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Unit testing framework for C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libcheck.github.io/check"
source = f"https://github.com/libcheck/check/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a8de4e0bacfb4d76dd1c618ded263523b53b85d92a146d8835eb1a52932fa20a"
# oh the irony
# the tests actually pass but the test infra is broken
options = ["!check"]


@subpackage("check-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
