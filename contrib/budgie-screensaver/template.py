pkgname = "budgie-screensaver"
pkgver = "5.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "intltool", "glib-devel"]
makedepends = [
    "gnome-desktop-devel", "dbus-glib-devel", "linux-pam-devel", "elogind-devel", "libxxf86vm-devel", "libgnomekbd-devel"
]
pkgdesc = "Fork of GNOME Screensaver for Budgie 10"
maintainer = "toukoAMG <toukoamg@tutanota.com>"
license = "GPL-2.0-only"
url = "https://github.com/BuddiesOfBudgie/budgie-screensaver"
source = f"https://github.com/BuddiesOfBudgie/{pkgname}/releases/download/v{pkgver}/{pkgname}-v{pkgver}.tar.xz"
sha256 = "563ac3f845729e9e6d184d2dbf036ab3f51ff244c27f5b286cfcb89acc147f0c"
# needs graphical environment
options = ["!check"]
