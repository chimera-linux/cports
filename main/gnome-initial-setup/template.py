pkgname = "gnome-initial-setup"
pkgver = "45.4.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dparental_controls=disabled",
    "-Dsystemd=false",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext", "dconf"]
makedepends = [
    "accountsservice-devel",
    "fontconfig-devel",
    "gdm-devel",
    "geoclue-devel",
    "geocode-glib-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gnome-online-accounts-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "heimdal-devel",
    "ibus-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libnma-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "networkmanager-devel",
    "pango-devel",
    "polkit-devel",
    "rest-devel",
    "webkitgtk4-devel",
]
depends = ["dconf"]
pkgdesc = "GNOME initial setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-4]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "363e09aa3308e7f4074e066253a0182b322ab60376743de178bbb400e54ba8ee"
# FIXME cfi
hardening = ["vis", "!cfi"]
