pkgname = "libfontenc"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-encodingsdir=/usr/share/fonts/encodings"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "zlib-devel"]
pkgdesc = "Fontenc Library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "2cfcce810ddd48f2e5dc658d28c1808e86dcf303eaff16728b9aa3dbc0092079"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libfontenc-static")
def _static(self):
    return self.default_static()

@subpackage("libfontenc-devel")
def _devel(self):
    return self.default_devel()
