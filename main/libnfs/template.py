pkgname = "libnfs"
pkgver = "5.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "NFS client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/sahlberg/libnfs"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "7ef445410b42f36b9bad426608b53ccb9ccca4101e545c383f564c11db672ca8"

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("libnfs-devel")
def _devel(self):
    return self.default_devel()
