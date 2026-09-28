pkgname = "libnetfilter_cthelper"
pkgver = "1.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "libmnl-devel",
    "linux-headers",
]
pkgdesc = "Netfilter netlink library for connection tracking helpers"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/libnetfilter_cthelper"
source = f"{url}/files/libnetfilter_cthelper-{pkgver}.tar.bz2"
sha256 = "14073d5487233897355d3ff04ddc1c8d03cc5ba8d2356236aa88161a9f2dc912"


@subpackage("libnetfilter_cthelper-devel")
def _(self):
    return self.default_devel()
