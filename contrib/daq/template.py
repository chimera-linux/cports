pkgname = "daq"
pkgver = "3.0.16"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["libpcap-devel"]
checkdepends = ["cmocka-devel"]
pkgdesc = "Data Acquisition library for packet I/O"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "GPL-2.0-only"
url = "https://github.com/snort3/libdaq"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "20c641c5a8a6c230c2753eb3e0b1b493810942dbd4b1828a4462bb18a4f43f82"
# check requires wrapper on glibc function __vsnprintf_chk
options = ["!check"]


@subpackage("daq-devel")
def _(self):
    return self.default_devel()
