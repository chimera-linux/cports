pkgname = "libnfs"
pkgver = "5.0.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "NFS client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/sahlberg/libnfs"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "d945cb4f4c8f82ee1f3640893a168810f794a28e1010bb007ec5add345e9df3e"


@subpackage("libnfs-devel")
def _devel(self):
    return self.default_devel()
