pkgname = "openimagedenoise"
pkgver = "2.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "python", "ispc"]
makedepends = ["onetbb-devel", "ispc-devel"]
pkgdesc = "High-performance denoising library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://www.openimagedenoise.org"
source = f"https://github.com/OpenImageDenoise/oidn/releases/download/v{pkgver}/oidn-{pkgver}.src.tar.gz"
sha256 = "d26b75fa216165086f65bf48c80648290f2cfed7d3c4bfc1e86c247b46c96b7e"


@subpackage("openimagedenoise-progs")
def _progs(self):
    return self.default_progs()


@subpackage("openimagedenoise-devel")
def _devel(self):
    return self.default_devel()
