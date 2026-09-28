pkgname = "imlib2"
pkgver = "1.12.5"
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
    "giflib-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxcb-devel",
]
pkgdesc = "Image manipulation library"
license = "Imlib2"
url = "https://www.enlightenment.org"
source = f"$(SOURCEFORGE_SITE)/enlightenment/imlib2-src/imlib2-{pkgver}.tar.gz"
sha256 = "097d40aee4cf4a349187615b796b37db1652fcc84bb0e8d5c0b380ab651d9095"
hardening = ["!cfi"]  # investigate


def post_install(self):
    self.install_license("COPYING")


@subpackage("imlib2-devel")
def _(self):
    return self.default_devel()


@subpackage("imlib2-progs")
def _(self):
    return self.default_progs()
