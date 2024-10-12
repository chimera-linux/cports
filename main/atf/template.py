pkgname = "atf"
pkgver = "0.21"
pkgrel = 1
build_style = "gnu_configure"
# XXX drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Testing library"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://github.com/freebsd/atf"
source = f"{url}/releases/download/atf-{pkgver}/atf-{pkgver}.tar.gz"
sha256 = "92bc64180135eea8fe84c91c9f894e678767764f6dbc8482021d4dde09857505"
tool_flags = {"CXXFLAGS": ["-std=gnu++11"]}


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/tests")


@subpackage("atf-devel")
def _(self):
    return self.default_devel()
