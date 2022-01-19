pkgname = "libnftnl"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7508a5c414fab13e3cb3ce8262d0ce4f02c1590a8e4f8628ab497b5b4585937c"

@subpackage("libnftnl-devel")
def _devel(self):
    return self.default_devel()
