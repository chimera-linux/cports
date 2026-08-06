pkgname = "python-cairo"
pkgver = "1.29.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["cairo-devel", "python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Cairo graphics library"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "f3f7fde97325cae80224c09f12564ef58d0d0f655da0e3b040f5807bd5bd3142"


@subpackage("python-cairo-devel")
def _(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()
