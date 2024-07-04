pkgname = "libconfuse"
pkgver = "3.3"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "gettext-devel", "libtool"]
pkgdesc = "Configuration file parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://github.com/martinh/libconfuse"
source = f"{url}/releases/download/v{pkgver}/confuse-{pkgver}.tar.gz"
sha256 = "3a59ded20bc652eaa8e6261ab46f7e483bc13dad79263c15af42ecbb329707b8"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libconfuse-devel")
def _devel(self):
    return self.default_devel()
