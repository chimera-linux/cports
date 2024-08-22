pkgname = "libnftnl"
pkgver = "1.2.7"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/libnftnl-{pkgver}.tar.xz"
sha256 = "9122774f968093d5c0bacddd67de480f31fa4073405a7fc058a34b0f387aecb3"
# CFI: verify function pointers
hardening = ["vis", "!cfi"]
options = ["linkundefver"]


@subpackage("libnftnl-devel")
def _(self):
    return self.default_devel()
