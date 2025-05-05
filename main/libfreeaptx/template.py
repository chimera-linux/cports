pkgname = "libfreeaptx"
pkgver = "0.2.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Free implementation of aptX codec"
license = "LGPL-2.1-or-later"
url = "https://github.com/iamthehorker/libfreeaptx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5ab5ebddf3f2eb7ce47a505b87460b00fc1ede99c70010796d3575ab31ea80bf"
# no test suite
options = ["!check"]


@subpackage("libfreeaptx-devel")
def _(self):
    return self.default_devel()
