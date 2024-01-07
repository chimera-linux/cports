pkgname = "libnfs"
pkgver = "5.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "NFS client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/sahlberg/libnfs"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "637e56643b19da9fba98f06847788c4dad308b723156a64748041035dcdf9bd3"


@subpackage("libnfs-devel")
def _devel(self):
    return self.default_devel()
