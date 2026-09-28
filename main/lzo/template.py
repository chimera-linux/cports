pkgname = "lzo"
pkgver = "2.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-shared"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Portable lossless data compression library"
license = "GPL-2.0-or-later"
url = "http://www.oberhumer.com/opensource/lzo"
source = f"{url}/download/lzo-{pkgver}.tar.gz"
sha256 = "c0f892943208266f9b6543b3ae308fab6284c5c90e627931446fb49b4221a072"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("lzo-devel")
def _(self):
    return self.default_devel()
