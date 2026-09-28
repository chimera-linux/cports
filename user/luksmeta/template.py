pkgname = "luksmeta"
pkgver = "10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "asciidoc",
    "automake",
    "libtool",
    "libxml2-progs",
    "pkgconf",
]
makedepends = ["cryptsetup-devel"]
checkdepends = [
    "bash",
    "cryptsetup",
]
pkgdesc = "Simple library for storing metadata in the LUKSv1 header"
license = "GPL-3.0-only"
url = "https://github.com/latchset/luksmeta"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6d688bc37cdae3b2d11d1ad6ba1882954d5588103b396c5f30962a417b59b3a2"
# vis breaks symbols
hardening = ["!vis", "!cfi"]


@subpackage("luksmeta-devel")
def _(self):
    return self.default_devel()
