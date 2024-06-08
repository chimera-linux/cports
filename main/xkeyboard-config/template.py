pkgname = "xkeyboard-config"
pkgver = "2.42"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxorg-rules-symlinks=true", "-Dcompat-rules=true"]
hostmakedepends = ["meson", "pkgconf", "xsltproc", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp-devel"]
checkdepends = ["gawk"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a6b06ebfc1f01fc505f2f05f265f95f67cc8873a54dd247e3c2d754b8f7e0807"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
