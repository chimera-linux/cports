pkgname = "freealut"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["openal-soft-devel"]
pkgdesc = "OpenAL Utility Toolkit"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/vancegroup/freealut"
source = f"{url}/archive/refs/tags/freealut_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "c3880d7dbb90c7db54e1d6b88aa0a34dd9e2d828fd389be0d2cbb2632b0885dd"


@subpackage("freealut-devel")
def _(self):
    return self.default_devel()
