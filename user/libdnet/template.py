pkgname = "libdnet"
pkgver = "1.18.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "linux-headers", "pkgconf"]
makedepends = ["check-devel"]
pkgdesc = "Interface to several low-level networking routines"
license = "BSD-3-Clause"
url = "https://github.com/ofalk/libdnet"
source = f"{url}/archive/refs/tags/libdnet-{pkgver}.tar.gz"
sha256 = "a4a82275c7d83b85b1daac6ebac9461352731922161f1dcdcccd46c318f583c9"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdnet-devel")
def _(self):
    return self.default_devel()
