pkgname = "libnfnetlink"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["linux-headers"]
pkgdesc = "Low-level library for netfilter kernel/userspace communication"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnfnetlink"
source = f"{url}/files/libnfnetlink-{pkgver}.tar.bz2"
sha256 = "b064c7c3d426efb4786e60a8e6859b82ee2f2c5e49ffeea640cfe4fe33cbc376"


@subpackage("libnfnetlink-devel")
def _(self):
    return self.default_devel()
