pkgname = "libaio"
pkgver = "0.3.113"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "partcheck"  # full check needs root, e2fsprogs, mount, etc
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Linux-native asynchronous I/O facility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://pagure.io/libaio"
source = f"{url}/archive/libaio-{pkgver}/libaio-libaio-{pkgver}.tar.gz"
sha256 = "716c7059703247344eb066b54ecbc3ca2134f0103307192e6c2b7dab5f9528ab"
hardening = ["!ssp"]


@subpackage("libaio-devel")
def _devel(self):
    return self.default_devel()
