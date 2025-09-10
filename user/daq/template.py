pkgname = "daq"
pkgver = "3.0.21"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpcap-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Data Acquisition library for packet I/O"
license = "GPL-2.0-only"
url = "https://github.com/snort3/libdaq"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "60ad9405c1c6b75955e0784511b173570a601491ccdb6399da53ca811c446a96"
# check requires wrapper on glibc function __vsnprintf_chk
options = ["!check"]


@subpackage("daq-devel")
def _(self):
    return self.default_devel()
