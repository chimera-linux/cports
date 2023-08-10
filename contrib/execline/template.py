pkgname = "execline"
pkgver = "2.9.3.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--disable-allstatic",
    "--enable-multicall",
    "--enable-shared",
    "--libdir=/usr/lib",
]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["skalibs-devel"]
pkgdesc = "Small non-interactive scripting language"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://skarnet.org/software/execline"
source = f"https://skarnet.org/software/execline/execline-{pkgver}.tar.gz"
sha256 = "c8027fa70922d117cdee8cc20d277e38d03fd960e6d136d8cec32603d4ec238d"
# vis breaks symbols
hardening = []
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("execline-devel")
def _devel(self):
    return self.default_devel()
