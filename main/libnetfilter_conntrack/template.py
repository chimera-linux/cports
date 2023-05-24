pkgname = "libnetfilter_conntrack"
pkgver = "1.0.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libnfnetlink-devel", "libmnl-devel", "linux-headers"]
pkgdesc = "Library providing an API to the in-kernel connection tracking table"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnetfilter_conntrack"
source = f"{url}/files/{pkgname}-{pkgver}.tar.bz2"
sha256 = "67bd9df49fe34e8b82144f6dfb93b320f384a8ea59727e92ff8d18b5f4b579a8"


@subpackage("libnetfilter_conntrack-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
