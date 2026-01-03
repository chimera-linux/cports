pkgname = "libnftnl"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/libnftnl-{pkgver}.tar.xz"
sha256 = "607da28dba66fbdeccf8ef1395dded9077e8d19f2995f9a4d45a9c2f0bcffba8"
# CFI: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _(self):
    return self.default_devel()
