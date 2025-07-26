pkgname = "libnetfilter_queue"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "libmnl-devel",
    "libnfnetlink-devel",
    "linux-headers",
]
pkgdesc = "Interface to the kernel packet filter queue"
license = "GPL-2.0-or-later"
url = "https://netfilter.org/projects/libnetfilter_queue"
source = f"{url}/files/libnetfilter_queue-{pkgver}.tar.bz2"
sha256 = "f9ff3c11305d6e03d81405957bdc11aea18e0d315c3e3f48da53a24ba251b9f5"


@subpackage("libnetfilter_queue-devel")
def _(self):
    return self.default_devel()
