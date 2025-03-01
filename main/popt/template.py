pkgname = "popt"
pkgver = "1.19"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-devel"]
makedepends = ["gettext-devel"]
pkgdesc = "Command line option parsing library"
license = "MIT"
url = "https://rpm.org"
source = f"http://ftp.rpm.org/popt/releases/popt-1.x/popt-{pkgver}.tar.gz"
sha256 = "c25a4838fc8e4c1c8aacb8bd620edb3084a3d63bf8987fdad3ca2758c63240f9"
# ld: error: version script assignment of 'LIBPOPT_0' to symbol '_init' failed: symbol not defined
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("popt-devel")
def _(self):
    return self.default_devel()
