pkgname = "skalibs"
pkgver = "2.13.1.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--dynlibdir=/usr/lib",
    "--libdir=/usr/lib",
]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Set of general-purpose C programming libraries for skarnet software"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://skarnet.org/software/skalibs"
source = f"https://skarnet.org/software/skalibs/skalibs-{pkgver}.tar.gz"
sha256 = "b272a1ab799f7fac44b9b4fb5ace78a9616b2fe4882159754b8088c4d8199e33"
# vis breaks symbols
hardening = []
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("skalibs-devel")
def _devel(self):
    return self.default_devel()
