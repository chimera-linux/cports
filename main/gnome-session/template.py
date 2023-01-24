pkgname = "gnome-session"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false", "-Dsystemd_session=disable"
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xmlto", "gettext-tiny",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "elogind-devel", "gnome-desktop-devel",
    "json-glib-devel", "libice-devel", "libsm-devel", "libx11-devel", "xtrans"
]
# /usr/bin/gnome-session uses bash with exec -l
depends = [
    "bash", "dconf", "desktop-file-utils", "gsettings-desktop-schemas",
    "hicolor-icon-theme", "polkit"
]
pkgdesc = "GNOME session management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-session"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3fb9949501385c8c14618e78f178d952df98ad8c91080f4c5e1568c7393ae1f2"
# FIXME cfi
hardening = ["vis", "!cfi"]
