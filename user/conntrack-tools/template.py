pkgname = "conntrack-tools"
pkgver = "1.4.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "dinit-chimera",
    "libmnl-devel",
    "libnetfilter_conntrack-devel",
    "libnetfilter_cthelper-devel",
    "libnetfilter_cttimeout-devel",
    "libnetfilter_queue-devel",
    "libnfnetlink-devel",
    "libtirpc-devel",
    "linux-headers",
]
pkgdesc = "Connection tracking userspace tools"
license = "GPL-2.0-only"
url = "https://www.netfilter.org/projects/conntrack-tools"
source = f"{url}/files/conntrack-tools-{pkgver}.tar.xz"
sha256 = "c15afe488a8d408c9d6d61e97dbd19f3c591942f62c13df6453a961ca4231cae"


def post_install(self):
    self.install_service(self.files_path / "conntrackd")
