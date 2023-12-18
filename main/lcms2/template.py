pkgname = "lcms2"
pkgver = "2.16"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://littlecms.com"
source = f"https://github.com/mm2/Little-CMS/releases/download/lcms{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d873d34ad8b9b4cea010631f1a6228d2087475e4dc5e763eb81acc23d9d45a51"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("lcms2-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()


@subpackage("lcms2-progs")
def _progs(self):
    return self.default_progs()
