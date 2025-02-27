pkgname = "lcms2"
pkgver = "2.17"
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
sha256 = "d11af569e42a1baa1650d20ad61d12e41af4fead4aa7964a01f93b08b53ab074"
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
