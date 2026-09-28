pkgname = "libnetfilter_conntrack"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
# reconf breaks ppc build
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libnfnetlink-devel", "libmnl-devel", "linux-headers"]
pkgdesc = "Library providing an API to the in-kernel connection tracking table"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnetfilter_conntrack"
source = f"{url}/files/libnetfilter_conntrack-{pkgver}.tar.xz"
sha256 = "769d3eaf57fa4fbdb05dd12873b6cb9a5be7844d8937e222b647381d44284820"


@subpackage("libnetfilter_conntrack-devel")
def _(self):
    return self.default_devel()
