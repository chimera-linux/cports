pkgname = "ixion"
pkgver = "0.18.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "python"]
makedepends = ["boost-devel", "python-devel", "mdds"]
checkdepends = ["bash"]
pkgdesc = "General-purpose formula parser and interpreter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/ixion/ixion"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6969e5bd475da5397b5e007d55749e5d0f0a502a72ac6f9a0bb40bbcabebc6e8"


@subpackage("ixion-libs")
def _libs(self):
    return self.default_libs()


@subpackage("ixion-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]


@subpackage("ixion-devel")
def _devel(self):
    return self.default_devel()
