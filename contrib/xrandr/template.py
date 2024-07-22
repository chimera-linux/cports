pkgname = "xrandr"
pkgver = "1.5.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxrandr-devel"]
pkgdesc = "Command line interface to X RandR extension"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xrandr-{pkgver}.tar.xz"
sha256 = "c8bee4790d9058bacc4b6246456c58021db58a87ddda1a9d0139bf5f18f1f240"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
