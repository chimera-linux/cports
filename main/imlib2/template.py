pkgname = "imlib2"
pkgver = "1.12.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--sysconfdir=/etc/imlib2",
    "--enable-visibility-hiding",
]
hostmakedepends = ["pkgconf"]
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
sha256 = "b139dca28d8de24fa50475851fdf59d3439f00e8b42e8c0f8daebb55a102455d"
hardening = ["!cfi"]  # TODO investigate


def post_install(self):
    self.install_license("COPYING")


@subpackage("imlib2-devel")
def _devel(self):
    return self.default_devel()


@subpackage("imlib2-progs")
def _progs(self):
    return self.default_progs()


configure_gen = []
