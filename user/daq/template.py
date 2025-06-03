pkgname = "daq"
pkgver = "3.0.19"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpcap-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Data Acquisition library for packet I/O"
license = "GPL-2.0-only"
url = "https://github.com/snort3/libdaq"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "28d026de46f8206b1a74dd6bf7de10ca19d7a7c95a463744b9f79e51958e5889"
# check requires wrapper on glibc function __vsnprintf_chk
options = ["!check"]


@subpackage("daq-devel")
def _(self):
    return self.default_devel()
