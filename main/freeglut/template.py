pkgname = "freeglut"
pkgver = "3.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libxxf86vm-devel", "libxi-devel", "mesa-devel", "glu-devel"]
pkgdesc = "Open source implementation of the OpenGL Utility Toolkit library"
license = "MIT"
url = "http://freeglut.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/freeglut/freeglut-{pkgver}.tar.gz"
sha256 = "9c3d4d6516fbfa0280edc93c77698fb7303e443c1aaaf37d269e3288a6c3ea52"


def post_install(self):
    self.install_license("COPYING")


@subpackage("freeglut-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()
