pkgname = "gnome-session"
pkgver = "46.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=/tmp",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "xmlto",
    "gettext",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "elogind-devel",
    "gnome-desktop-devel",
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
source = (
    f"$(GNOME_SITE)/gnome-session/{pkgver[:-2]}/gnome-session-{pkgver}.tar.xz"
)
sha256 = "c6e1624af6090bc4e1a191fe2268abfa7a8de07831ca7a57f217e679bf7b9a54"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.uninstall("tmp")
