pkgname = "libconfuse"
pkgver = "3.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "gettext-devel", "libtool"]
pkgdesc = "Configuration file parser library"
license = "ISC"
url = "https://github.com/martinh/libconfuse"
source = f"{url}/releases/download/v{pkgver}/confuse-{pkgver}.tar.gz"
sha256 = "d98a793f4cafc1b3c18e2509ba54f6cb9ac6291b181bcda152dc987cb78f43ec"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libconfuse-devel")
def _(self):
    return self.default_devel()
