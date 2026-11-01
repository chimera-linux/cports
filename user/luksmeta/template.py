pkgname = "luksmeta"
pkgver = "11"
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
sha256 = "a24eac0292b2f3f8f209a30dd7cd3da3be7814cb9b138575a77ef7bc8e7829df"
# vis breaks symbols
hardening = ["!vis", "!cfi"]


@subpackage("luksmeta-devel")
def _(self):
    return self.default_devel()
