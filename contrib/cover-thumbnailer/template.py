pkgname = "cover-thumbnailer"
pkgver = "0.10.1"
pkgrel = 0
hostmakedepends = ["bash", "gettext"]
depends = ["gtk+3", "python-gobject", "python-pillow"]
pkgdesc = "Thumbnailer for music album and picture folder covers"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/flozz/cover-thumbnailer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3b5fd373554376a74ea88bb42ad21f0d109b456ed660fe9703468523e1eda279"


def install(self):
    self.do("./install.sh", "--package", self.chroot_destdir)
