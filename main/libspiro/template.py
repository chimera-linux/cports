pkgname = "libspiro"
pkgver = "20240903"
pkgrel = 0
build_style = "gnu_configure"
# broken quoting
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Simplifies the drawing of beautiful curves"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/fontforge/libspiro"
source = f"{url}/releases/download/{pkgver}/libspiro-dist-{pkgver}.tar.gz"
sha256 = "1412a21b943c6e1db834ee2d74145aad20b3f62b12152d475613b8241d9cde10"


@subpackage("libspiro-devel")
def _(self):
    return self.default_devel()
