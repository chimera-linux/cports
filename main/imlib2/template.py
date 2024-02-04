pkgname = "imlib2"
pkgver = "1.12.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--sysconfdir=/etc/imlib2",
    "--enable-visibility-hiding",
]
hostmakedepends = ["automake", "libtool", "pkgconf"]
# mp3 loader is disabled because libid3tag is old and busted
makedepends = [
    "freetype-devel",
    "libpng-devel",
    "libjpeg-turbo-devel",
    "libwebp-devel",
    "libtiff-devel",
    "giflib-devel",
    "libxcb-devel",
    "libheif-devel",
    "librsvg-devel",
]
pkgdesc = "Image manipulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Imlib2"
url = "https://www.enlightenment.org"
source = (
    f"$(SOURCEFORGE_SITE)/enlightenment/{pkgname}-src/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "e96b43014ac9d61a0775e28a46cf7befbd49654705df845001e849e44839481b"
hardening = ["!cfi"]  # TODO investigate


def post_install(self):
    self.install_license("COPYING")


@subpackage("imlib2-devel")
def _devel(self):
    return self.default_devel()


@subpackage("imlib2-progs")
def _progs(self):
    return self.default_progs()
