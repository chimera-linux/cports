pkgname = "ixion"
pkgver = "0.19.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool", "python"]
makedepends = ["boost-devel", "python-devel", "mdds"]
checkdepends = ["bash"]
pkgdesc = "General-purpose formula parser and interpreter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/ixion/ixion"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b5b67ea7fc631a0fda4fff3123f0cc2e3831849bdd8fbae8443be0766a77f243"


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
