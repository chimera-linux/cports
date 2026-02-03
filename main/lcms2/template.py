pkgname = "lcms2"
pkgver = "2.18"
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
sha256 = "ee67be3566f459362c1ee094fde2c159d33fa0390aa4ed5f5af676f9e5004347"
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
