pkgname = "libnftnl"
pkgver = "1.2.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "ceeaea2cd92147da19f13a35a7f1a4bc2767ff897e838e4b479cf54b59c777f4"
# FIXME cfi: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _devel(self):
    return self.default_devel()
