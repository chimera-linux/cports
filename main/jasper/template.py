pkgname = "jasper"
pkgver = "2.0.33"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Reference implementation of the JPEG-2000 codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "JasPer-2.0"
url = "https://ece.engr.uvic.ca/~frodo/jasper"
source = f"https://github.com/jasper-software/{pkgname}/releases/download/version-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "28d28290cc2eaf70c8756d391ed8bcc8ab809a895b9a67ea6e89da23a611801a"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("jasper-devel")
def _devel(self):
    self.depends += ["libjpeg-turbo-devel"]

    return self.default_devel()

@subpackage("jasper-progs")
def _progs(self):
    return self.default_progs()
