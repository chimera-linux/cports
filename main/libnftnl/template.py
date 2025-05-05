pkgname = "libnftnl"
pkgver = "1.2.9"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/libnftnl-{pkgver}.tar.xz"
sha256 = "e8c216255e129f26270639fee7775265665a31b11aa920253c3e5d5d62dfc4b8"
# CFI: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _(self):
    return self.default_devel()
