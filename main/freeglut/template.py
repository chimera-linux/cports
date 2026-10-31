pkgname = "freeglut"
pkgver = "3.6.0"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "glu-devel",
    "libglvnd-devel",
    "libxi-devel",
    "libxxf86vm-devel",
    "linux-headers",
]
pkgdesc = "Open source implementation of the OpenGL Utility Toolkit library"
license = "MIT"
url = "http://freeglut.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/freeglut/freeglut-{pkgver}.tar.gz"
sha256 = "9c3d4d6516fbfa0280edc93c77698fb7303e443c1aaaf37d269e3288a6c3ea52"


def post_install(self):
    self.install_license("COPYING")


@subpackage("freeglut-devel")
def _(self):
    # untraced
    self.depends += [
        "pc:gl!libglvnd-devel",
        "pc:x11!libx11-devel",
        "pc:xrandr!libxrandr-devel",
        "pc:xxf86vm!libxxf86vm-devel",
    ]
    return self.default_devel()
