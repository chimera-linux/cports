pkgname = "luksmeta"
pkgver = "9"
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
sha256 = "0eea7d50a0411e0c1e383fd47073806ed7d435b27410504e33bfbc792a1688fc"
# vis breaks symbols
hardening = ["!vis", "!cfi"]


@subpackage("luksmeta-devel")
def _(self):
    return self.default_devel()
