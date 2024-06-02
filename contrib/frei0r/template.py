pkgname = "frei0r"
pkgver = "2.3.2"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gavl-devel",
    "opencv-devel",
]
pkgdesc = "Collection of video plugins"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://frei0r.dyne.org"
source = f"https://github.com/dyne/frei0r/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "304291e0ecb456a8b054fe04e14adc50ace54d0223b7b29165ff5343e820ef9d"


@subpackage("frei0r-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
