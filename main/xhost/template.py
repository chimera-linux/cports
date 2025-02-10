pkgname = "xhost"
pkgver = "1.0.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gettext-devel"]
makedepends = ["libx11-devel", "libxmu-devel"]
pkgdesc = "X server access control program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xhost-{pkgver}.tar.gz"
sha256 = "10a157a9c818e6ec17764ba22117e006089107a22aacf58be6de089a76a112f4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
