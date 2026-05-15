pkgname = "lcms2"
pkgver = "2.19.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Djpeg=enabled",
    "-Dtiff=enabled",
    "-Dutils=true",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libjpeg-turbo-devel", "libtiff-devel"]
pkgdesc = "Small-footprint color management engine"
license = "MIT"
url = "https://littlecms.com"
source = f"https://github.com/mm2/Little-CMS/releases/download/lcms{pkgver}/lcms2-{pkgver}.tar.gz"
sha256 = "bfc54f7bab59fbc921012014a8032e4cba4abd46db47d46b76416a8c0b2815c8"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("lcms2-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()


@subpackage("lcms2-progs")
def _(self):
    return self.default_progs()
