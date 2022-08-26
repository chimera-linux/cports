pkgname = "libnftnl"
pkgver = "1.2.3"
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
sha256 = "e916ea9b79f9518560b9a187251a7c042442a9ecbce7f36be7908888605d0255"

@subpackage("libnftnl-devel")
def _devel(self):
    return self.default_devel()
