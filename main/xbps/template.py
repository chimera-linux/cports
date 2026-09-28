pkgname = "xbps"
pkgver = "0.60.5"
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
sha256 = "fba39edfdcfeb6f7e3f348a091453fefb087089999cf5bea20ea65ac6cf009dc"
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
