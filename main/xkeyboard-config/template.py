pkgname = "xkeyboard-config"
pkgver = "2.39"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxorg-rules-symlinks=true", "-Dcompat-rules=true"]
hostmakedepends = ["meson", "pkgconf", "xsltproc", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5ac5f533eff7b0c116805fe254fd79b2c9882700a4f9f2c070f8c4eae5aaa682"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
