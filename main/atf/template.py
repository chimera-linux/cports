pkgname = "atf"
pkgver = "0.22"
pkgrel = 0
build_style = "gnu_configure"
# XXX drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
pkgdesc = "Testing library"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://github.com/freebsd/atf"
source = f"{url}/archive/refs/tags/atf-{pkgver}.tar.gz"
sha256 = "a31fa9eb443ebce34540cb852c81f39346eb1875523e14399a6d4a636e4765a7"


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/tests")


@subpackage("atf-devel")
def _(self):
    return self.default_devel()
