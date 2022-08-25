pkgname = "imlib2"
pkgver = "1.9.1"
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
    "libtiff-devel", "giflib-devel", "libxcb-devel", "libheif-devel",
    "librsvg-devel",
]
pkgdesc = "Image manipulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Imlib2"
url = "https://www.enlightenment.org"
source = f"$(SOURCEFORGE_SITE)/enlightenment/{pkgname}-src/{pkgname}-{pkgver}.tar.gz"
sha256 = "c319292f5bcab33b91bffaa6f7b0842f9e2d1b90df6c9a2a39db4f24d538b35b"

def post_install(self):
    self.install_license("COPYING")

@subpackage("imlib2-devel")
def _devel(self):
    return self.default_devel()

@subpackage("imlib2-progs")
def _devel(self):
    return self.default_progs()
