pkgname = "xbps"
pkgver = "0.59.2"
pkgrel = 1
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--enable-tests",
]
hostmakedepends = ["pkgconf"]
makedepends = ["libarchive-devel", "openssl-devel", "zlib-ng-compat-devel"]
depends = ["ca-certificates"]
checkdepends = ["kyua", "atf-devel"]
pkgdesc = "XBPS package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause AND BSD-3-Clause AND MIT"
url = "https://github.com/void-linux/xbps"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a6607e83fcd654a0ae846d729e43fefd8da9a61323e91430f884caf895b4f59b"


def init_check(self):
    self.make_check_env = {"NPROCS": str(self.make_jobs)}


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.3RDPARTY")


@subpackage("xbps-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
