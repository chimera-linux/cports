pkgname = "xkeyboard-config"
pkgver = "2.43"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxorg-rules-symlinks=true", "-Dcompat-rules=true"]
hostmakedepends = ["meson", "pkgconf", "libxslt-progs", "python", "perl"]
makedepends = ["libx11-devel", "xkbcomp-devel"]
checkdepends = ["gawk"]
depends = ["xkbcomp"]
pkgdesc = "X Keyboard Configuration Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/XKeyboardConfig"
source = f"$(XORG_SITE)/data/xkeyboard-config/xkeyboard-config-{pkgver}.tar.xz"
sha256 = "c810f362c82a834ee89da81e34cd1452c99789339f46f6037f4b9e227dd06c01"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
