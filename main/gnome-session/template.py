pkgname = "gnome-session"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false", "-Dsystemd_session=disable",
    "-Dsystemduserunitdir=/tmp",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xmlto", "gettext-tiny",
]
makedepends = [
    "glib-devel", "gtk+3-devel", "elogind-devel", "gnome-desktop-devel",
    "json-glib-devel", "libice-devel", "libsm-devel", "libx11-devel", "xtrans"
]
depends = [
    "dconf", "desktop-file-utils", "gsettings-desktop-schemas",
    "hicolor-icon-theme", "polkit"
]
pkgdesc = "GNOME session management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-session"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ccf829a96526135e9e9f917526515d36a5092bdfa316f3737dd8c5a524dbf2c6"
# FIXME cfi
hardening = ["vis", "!cfi"]
