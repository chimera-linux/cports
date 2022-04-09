pkgname = "imlib2"
pkgver = "1.8.1"
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
sha256 = "aa26a3fb0468639f9aacb03ac189fe7f703c80f2bfae76e9647889b0bc664c90"

def post_install(self):
    self.install_license("COPYING")

@subpackage("imlib2-devel")
def _devel(self):
    return self.default_devel()

@subpackage("imlib2-progs")
def _devel(self):
    return self.default_progs()
