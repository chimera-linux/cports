pkgname = "dosfstools"
pkgver = "4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-compat-symlinks"]
hostmakedepends = ["pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "DOS filesystem tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/dosfstools/dosfstools"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "64926eebf90092dca21b14259a5301b7b98e7b1943e8a201c7d726084809b527"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/share/doc")


configure_gen = []
