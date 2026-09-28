pkgname = "xrandr"
pkgver = "1.5.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Command line interface to X RandR extension"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xrandr-{pkgver}.tar.xz"
sha256 = "2cafccb2aaf2491a4068676117a0d4f90ab307724b96fffc54cd1da953779400"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
