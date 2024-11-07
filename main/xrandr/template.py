pkgname = "xrandr"
pkgver = "1.5.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Command line interface to X RandR extension"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xrandr-{pkgver}.tar.xz"
sha256 = "f8dd7566adb74147fab9964680b6bbadee87cf406a7fcff51718a5e6949b841c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
