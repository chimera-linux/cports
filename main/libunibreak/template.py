pkgname = "libunibreak"
pkgver = "6.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Library for the Unicode line breaking and word breaking algorithms"
maintainer = "psykose <alice@ayaya.dev>"
license = "Zlib"
url = "https://github.com/adah1972/libunibreak"
source = f"{url}/releases/download/libunibreak_{pkgver.replace('.', '_')}/libunibreak-{pkgver}.tar.gz"
sha256 = "f189daa18ead6312c5db6ed3d0c76799135910ed6c06637c7eea20a7e5e7cc7f"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")


@subpackage("libunibreak-devel")
def _devel(self):
    return self.default_devel()
