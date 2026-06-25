pkgname = "libnetfilter_cttimeout"
pkgver = "1.0.1"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = [
    "libmnl-devel",
    "linux-headers",
]
pkgdesc = "Netlink interface for conntrack timeout"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnetfilter_cttimeout"
source = f"{url}/files/libnetfilter_cttimeout-{pkgver}.tar.bz2"
sha256 = "0b59da2f3204e1c80cb85d1f6d72285fc07b01a2f5678abf5dccfbbefd650325"


@subpackage("libnetfilter_cttimeout-devel")
def _(self):
    return self.default_devel()
