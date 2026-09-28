pkgname = "xkeyboard-config"
# 2.45 breaks macintosh layouts
pkgver = "2.44"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dxorg-rules-symlinks=true", "-Dcompat-rules=true"]
hostmakedepends = ["meson", "pkgconf", "libxslt-progs", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp-devel"]
checkdepends = ["gawk"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/xkeyboard-config/xkeyboard-config-{pkgver}.tar.xz"
sha256 = "54d2c33eeebb031d48fa590c543e54c9bcbd0f00386ebc6489b2f47a0da4342a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
