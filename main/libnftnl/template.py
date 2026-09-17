pkgname = "libnftnl"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers", "libmnl-devel"]
pkgdesc = "Low-level netlink API to nf_tables"
license = "GPL-2.0-or-later"
url = "https://www.netfilter.org/projects/libnftnl"
source = f"{url}/files/libnftnl-{pkgver}.tar.xz"
sha256 = "c97abc3409f8fa396b4462b2bb7f147a3a47a4ddc97cfa0b2f18890c9cfde8b0"
# CFI: verify function pointers
hardening = ["vis", "!cfi"]


@subpackage("libnftnl-devel")
def _(self):
    return self.default_devel()
