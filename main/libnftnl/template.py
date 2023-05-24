pkgname = "libnftnl"
pkgver = "1.2.5"
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
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "966de0a8120c8a53db859889749368bfb2cba0c4f0b4c1a30d264eccc45f1226"
# FIXME cfi: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
