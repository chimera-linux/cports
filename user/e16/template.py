pkgname = "e16"
pkgver = "1.0.30"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-sound",
    "--enable-sound-pulse",
]
hostmakedepends = ["automake", "gettext", "slibtool", "pkgconf"]
makedepends = [
    "audiofile-devel",
    "dbus-devel",
    "fontconfig-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "gettext-devel",
    "imlib2-devel",
    "libice-devel",
    "libpulse-devel",
    "libsm-devel",
    "libsndfile-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxft-devel",
    "libxinerama-devel",
    "libxpm-devel",
    "libxpresent-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxxf86vm-devel",
    "pango-devel",
]
depends = ["desktop-file-utils", "libpulse-progs", "python"]
pkgdesc = "Themed window manager for X11"
maintainer = "rane <rane+chimera@junkyard.systems>"
license = "BSD-2-Clause"
url = "https://enlightenment.org/e16"
source = f"$(SOURCEFORGE_SITE)/enlightenment/e16/{pkgver}/e16-{pkgver}.tar.xz"
sha256 = "24a0660600b970de173b4debd0d47bf0bcbdb6923bdf7fec5043cbd062d4e41d"


def post_install(self):
    self.install_license("COPYING")
