pkgname = "imlib2"
pkgver = "1.7.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--sysconfdir=/etc/imlib2",
    "--enable-visibility-hiding"
]
hostmakedepends = ["pkgconf"]
# mp3 loader is disabled because libid3tag is old and busted
makedepends = [
    "freetype-devel", "libpng-devel", "libjpeg-turbo-devel", "libwebp-devel",
    "libtiff-devel", "giflib-devel", "libxcb-devel", 
]
pkgdesc = "Image manipulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Imlib2"
url = "https://www.enlightenment.org"
source = f"$(SOURCEFORGE_SITE)/enlightenment/{pkgname}-src/{pkgname}-{pkgver}.tar.gz"
sha256 = "73337bc38de13e04832f645367baf932b39d8b558d4ed9bc1f13405b92090b96"

def post_install(self):
    self.install_license("COPYING")

@subpackage("imlib2-devel")
def _devel(self):
    return self.default_devel()

@subpackage("imlib2-progs")
def _devel(self):
    return self.default_progs()
