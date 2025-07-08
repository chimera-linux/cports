pkgname = "daq"
pkgver = "3.0.20"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpcap-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Data Acquisition library for packet I/O"
license = "GPL-2.0-only"
url = "https://github.com/snort3/libdaq"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "42730cb427695d4049deaa667623036b3915eaa651bcb91493ca450f06bb36b3"
# check requires wrapper on glibc function __vsnprintf_chk
options = ["!check"]


@subpackage("daq-devel")
def _(self):
    return self.default_devel()
