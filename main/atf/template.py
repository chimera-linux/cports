pkgname = "atf"
pkgver = "0.23"
pkgrel = 0
build_style = "gnu_configure"
# XXX drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
pkgdesc = "Testing library"
license = "BSD-2-Clause"
url = "https://github.com/freebsd/atf"
source = f"{url}/archive/refs/tags/atf-{pkgver}.tar.gz"
sha256 = "37aa5341f2b51ffee245db3456d9bc25f718ca12beb7b990dc16d686890115e3"


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/tests")


@subpackage("atf-devel")
def _(self):
    return self.default_devel()
