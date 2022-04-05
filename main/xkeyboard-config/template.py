pkgname = "xkeyboard-config"
pkgver = "2.35.1"
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
sha256 = "18ce50ff0c74ae6093062bce1aeab3d363913ea35162fe271f8a0ce399de85cc"

def post_install(self):
    self.install_license("COPYING")
