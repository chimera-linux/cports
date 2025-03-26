pkgname = "imlib2"
pkgver = "1.12.4"
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
license = "Imlib2"
url = "https://www.enlightenment.org"
source = f"$(SOURCEFORGE_SITE)/enlightenment/imlib2-src/imlib2-{pkgver}.tar.gz"
sha256 = "3dd6538dd012ef140e051b9579633a7c4b073e088326d65df4d3b2d6099193b9"
hardening = ["!cfi"]  # investigate


def post_install(self):
    self.install_license("COPYING")


@subpackage("imlib2-devel")
def _(self):
    return self.default_devel()


@subpackage("imlib2-progs")
def _(self):
    return self.default_progs()
