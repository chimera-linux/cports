pkgname = "bzip3"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
pkgdesc = "Better and stronger spiritual successor to BZip2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later AND Apache-2.0"
url = "https://github.com/kspalaiologos/bzip3"
source = f"{url}/releases/download/{pkgver}/bzip3-{pkgver}.tar.zst"
sha256 = "4535aac61d4ad33e5c6daadaac6e9b061318eadf53768dca8b4e6b689807e57d"
hardening = ["vis", "cfi"]


@subpackage("libbzip3")
def _(self):
    return self.default_libs()


@subpackage("libbzip3-devel")
def _(self):
    return self.default_devel()
