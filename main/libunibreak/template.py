pkgname = "libunibreak"
pkgver = "6.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Library for the Unicode line breaking and word breaking algorithms"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Zlib"
url = "https://github.com/adah1972/libunibreak"
source = f"{url}/releases/download/libunibreak_{pkgver.replace('.', '_')}/libunibreak-{pkgver}.tar.gz"
sha256 = "cc4de0099cf7ff05005ceabff4afed4c582a736abc38033e70fdac86335ce93f"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")


@subpackage("libunibreak-devel")
def _(self):
    return self.default_devel()
