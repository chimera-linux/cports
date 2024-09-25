pkgname = "libnetfilter_conntrack"
pkgver = "1.1.0"
pkgrel = 1
build_style = "gnu_configure"
# reconf breaks ppc build
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libnfnetlink-devel", "libmnl-devel", "linux-headers"]
pkgdesc = "Library providing an API to the in-kernel connection tracking table"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnetfilter_conntrack"
source = f"{url}/files/libnetfilter_conntrack-{pkgver}.tar.xz"
sha256 = "67edcb4eb826c2f8dc98af08dabff68f3b3d0fe6fb7d9d0ac1ee7ecce0fe694e"


@subpackage("libnetfilter_conntrack-devel")
def _(self):
    return self.default_devel()
