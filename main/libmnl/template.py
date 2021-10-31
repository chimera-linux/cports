pkgname = "libmnl"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["musl-bsd-headers"]
pkgdesc = "Minimalistic user-space library oriented to Netlink developers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://www.netfilter.org/projects/libmnl"
source = f"{url}/files/{pkgname}-{pkgver}.tar.bz2"
sha256 = "171f89699f286a5854b72b91d06e8f8e3683064c5901fb09d954a9ab6f551f81"

@subpackage("libmnl-devel")
def _devel(self):
    return self.default_devel()
