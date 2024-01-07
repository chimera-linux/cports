pkgname = "xkeyboard-config"
pkgver = "2.40"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxorg-rules-symlinks=true", "-Dcompat-rules=true"]
hostmakedepends = ["meson", "pkgconf", "xsltproc", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp"]
checkdepends = ["gawk"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "7a3dba1bec7dc7191432da021242d17c9cf6c89690e6c57b0de048ff8c9d2ae3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
