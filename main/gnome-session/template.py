pkgname = "gnome-session"
pkgver = "47.0.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=/tmp",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "elogind-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libice-devel",
    "libsm-devel",
    "libx11-devel",
    "xtrans",
]
depends = [
    "dconf",
    "desktop-file-utils",
    "gsettings-desktop-schemas",
    "polkit",
]
pkgdesc = "GNOME session management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-session"
source = f"$(GNOME_SITE)/gnome-session/{pkgver[: pkgver.find('.')]}/gnome-session-{pkgver}.tar.xz"
sha256 = "56ae9c68e49995793eb2096bcdc4533b111669e1e54c8b6e0b1d952f6a5e8a70"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
