pkgname = "libpaper"
pkgver = "2.2.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
pkgdesc = "Library for handling paper characteristics"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND GPL-2.0-only AND GPL-3.0-or-later AND custom:none"
url = "https://github.com/rrthomas/libpaper"
source = f"{url}/releases/download/v{pkgver}/libpaper-{pkgver}.tar.gz"
sha256 = "500d39dc58768ee09688738c8b5bfe07640ba2fd6c25a6dc78810eb69c719e93"


def post_install(self):
    self.install_license("COPYING-MIT")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("libpaper-devel")
def _(self):
    return self.default_devel()


@subpackage("libpaper-progs")
def _(self):
    return self.default_progs()
