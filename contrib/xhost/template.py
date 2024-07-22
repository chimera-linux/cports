pkgname = "xhost"
pkgver = "1.0.9"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gettext-devel"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X server access control program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xhost-{pkgver}.tar.gz"
sha256 = "ca850367593fcddc4bff16de7ea1598aa4f6817daf5a803a1258dff5e337f7c3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
