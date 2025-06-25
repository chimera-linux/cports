pkgname = "xkeyboard-config"
pkgver = "2.45"
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
sha256 = "169e075a92d957a57787c199e84e359df2931b7196c1c5b4a3d576ee6235a87c"
hardening = ["vis", "cfi"]


def post_install(self):
    # apk bug: can't migrate directory -> symlink
    self.uninstall("usr/share/X11/xkb")
    self.rename(
        "usr/share/xkeyboard-config-2", "usr/share/X11/xkb", relative=False
    )
    self.install_link("usr/share/xkeyboard-config-2", "X11/xkb")
    self.install_license("COPYING")
