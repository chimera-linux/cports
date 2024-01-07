pkgname = "xbps"
pkgver = "0.59.2"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--disable-tests",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["libarchive-devel", "openssl-devel", "zlib-devel"]
depends = ["ca-certificates"]
checkdepends = ["kyua", "atf-devel"]
pkgdesc = "XBPS package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND BSD-3-Clause AND MIT"
url = "https://github.com/void-linux/xbps"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a6607e83fcd654a0ae846d729e43fefd8da9a61323e91430f884caf895b4f59b"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.3RDPARTY")


@subpackage("xbps-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()
