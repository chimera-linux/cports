pkgname = "libxdg-basedir"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Implementation of the XDG Base Directory specifications"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/devnev/libxdg-basedir"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "ff30c60161f7043df4dcc6e7cdea8e064e382aa06c73dcc3d1885c7d2c77451d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxdg-basedir-devel")
def _devel(self):
    return self.default_devel()
