pkgname = "conntrack-tools"
pkgver = "1.4.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
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
sha256 = "067677f4c5f6564819e78ed3a9d4a8980935ea9273f3abb22a420ea30ab5ded6"


def post_install(self):
    self.install_service(self.files_path / "conntrackd")
