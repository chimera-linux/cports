pkgname = "libmnl"
pkgver = "1.0.5"
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
sha256 = "274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525"
# FIXME cfi (e.g. libnftnl fails tests)
hardening = ["vis", "!cfi"]


@subpackage("libmnl-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
