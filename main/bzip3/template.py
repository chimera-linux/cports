pkgname = "bzip3"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Better and stronger spiritual successor to BZip2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later AND Apache-2.0"
url = "https://github.com/kspalaiologos/bzip3"
source = f"https://github.com/kspalaiologos/bzip3/releases/download/{pkgver}/bzip3-{pkgver}.tar.zst"
sha256 = "9ed00210290f594b886ca86d533a0e2fd6bd6699e4ea17bc54c4b83847979c38"
hardening = ["vis", "cfi"]


@subpackage("libbzip3")
def _(self):
    return self.default_libs()


@subpackage("libbzip3-devel")
def _(self):
    return self.default_devel()
