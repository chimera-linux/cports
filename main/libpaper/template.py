pkgname = "libpaper"
pkgver = "2.2.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "gettext"]
pkgdesc = "Library for handling paper characteristics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND GPL-2.0-only AND GPL-3.0-or-later AND custom:none"
url = "https://github.com/rrthomas/libpaper"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "7be50974ce0df0c74e7587f10b04272cd53fd675cb6a1273ae1cc5c9cc9cab09"


def post_install(self):
    self.install_license("COPYING-MIT")
    self.install_dir("etc/libpaper.d", empty=True)


@subpackage("libpaper-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpaper-progs")
def _progs(self):
    return self.default_progs()
