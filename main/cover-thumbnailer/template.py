pkgname = "cover-thumbnailer"
pkgver = "0.10.2"
pkgrel = 0
hostmakedepends = ["bash", "gettext"]
depends = ["gtk+3", "python-gobject", "python-pillow"]
pkgdesc = "Thumbnailer for music album and picture folder covers"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/flozz/cover-thumbnailer"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6365c2a15d3d4c512ebf8ca3b6b97ee121ea876579fa0dcc4de6ab70d21b3a03"


def install(self):
    self.do("./install.sh", "--package", self.chroot_destdir)
