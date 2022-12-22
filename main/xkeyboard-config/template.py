pkgname = "xkeyboard-config"
pkgver = "2.37"
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
sha256 = "eb1383a5ac4b6210d7c7302b9d6fab052abdf51c5d2c9b55f1f779997ba68c6c"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
