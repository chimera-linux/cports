pkgname = "gnome-session"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false",
    "-Dsystemd_session=disable",
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "706d2ffcacac38553a3c0185793f5a2b4aac940bb5e789d953c9808163bef2f1"
# FIXME cfi
hardening = ["vis", "!cfi"]
