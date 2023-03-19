pkgname = "gnome-session"
pkgver = "44.0_rc1"
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
    "libglib-devel", "gtk+3-devel", "elogind-devel", "gnome-desktop-devel",
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
source = f"$(GNOME_SITE)/{pkgname}/44/{pkgname}-44.rc.tar.xz"
sha256 = "03659950be77c97d8effdda838926a5ffdc7d05fdf98136fc0e9787634e71a41"
# FIXME cfi
hardening = ["vis", "!cfi"]
