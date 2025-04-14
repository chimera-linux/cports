pkgname = "gnome-session"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-session"
source = f"$(GNOME_SITE)/gnome-session/{pkgver[: pkgver.find('.')]}/gnome-session-{pkgver}.tar.xz"
sha256 = "dd909fbc5b22cdbdb2fc4df1a47d78d1b5943ccc5e61e6a20a1846246347c417"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
