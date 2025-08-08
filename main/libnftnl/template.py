pkgname = "libnftnl"
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/libnftnl-{pkgver}.tar.xz"
sha256 = "0f4be47a8bb8b77a350ee58cbd4b5fae6260ad486a527706ab15cfe1dd55a3c4"
# CFI: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _(self):
    return self.default_devel()
