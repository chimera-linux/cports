pkgname = "xrandr"
pkgver = "1.5.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Command line interface to X RandR extension"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.xz"
sha256 = "7bc76daf9d72f8aff885efad04ce06b90488a1a169d118dea8a2b661832e8762"

def post_install(self):
    self.install_license("COPYING")
