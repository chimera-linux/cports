pkgname = "npth"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "New portable threads library"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gnupg.org/software/npth/index.html"
source = f"https://gnupg.org/ftp/gcrypt/npth/npth-{pkgver}.tar.bz2"
sha256 = "8bd24b4f23a3065d6e5b26e98aba9ce783ea4fd781069c1b35d149694e90ca3e"


@subpackage("npth-devel")
def _(self):
    return self.default_devel()
