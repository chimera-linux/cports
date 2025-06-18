pkgname = "xbps"
pkgver = "0.60.3"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--enable-tests",
]
hostmakedepends = ["pkgconf"]
makedepends = ["libarchive-devel", "openssl3-devel", "zlib-ng-compat-devel"]
depends = ["ca-certificates"]
checkdepends = ["kyua", "atf-devel"]
pkgdesc = "XBPS package manager"
license = "BSD-2-Clause AND BSD-3-Clause AND MIT"
url = "https://github.com/void-linux/xbps"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "01ba4b7faad994560c6be5aeb50e39b6950e1d304e2d91c2668f0a9406d6af68"
# one bashcomp for all
options = ["!lintcomp"]


def init_check(self):
    self.make_check_env = {"NPROCS": str(self.make_jobs)}


def post_install(self):
    # lol kyua
    self.uninstall("usr/tests")
    # this xbps is only for xbps-src and bootstrapping
    self.uninstall("usr/share/xbps.d")
    self.uninstall("var/db/xbps")


@subpackage("xbps-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
