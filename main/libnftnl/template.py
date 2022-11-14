pkgname = "libnftnl"
pkgver = "1.2.4"
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
sha256 = "c0fe233be4cdfd703e7d5977ef8eb63fcbf1d0052b6044e1b23d47ca3562477f"

@subpackage("libnftnl-devel")
def _devel(self):
    return self.default_devel()
