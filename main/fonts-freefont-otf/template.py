pkgname = "fonts-freefont-otf"
pkgver = "20120503"
pkgrel = 0
pkgdesc = "Free fonts covering the UCS character set"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://nongnu.org/freefont"
source = f"https://ftp.gnu.org/gnu/freefont/freefont-otf-{pkgver}.tar.gz"
sha256 = "3a6c51868c71b006c33c4bcde63d90927e6fcca8f51c965b8ad62d021614a860"


def install(self):
    self.install_file("*.otf", "usr/share/fonts/freefont", glob=True)
