pkgname = "gnome-initial-setup"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dparental_controls=disabled",
    "-Dsystemd=false",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext", "dconf"]
makedepends = [
    "ibus-devel",
    "networkmanager-devel",
    "accountsservice-devel",
    "polkit-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "fontconfig-devel",
    "libgweather-devel",
    "gnome-online-accounts-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "glib-devel",
    "webkitgtk4-devel",
    "geocode-glib-devel",
    "geoclue-devel",
    "pango-devel",
    "rest-devel",
    "json-glib-devel",
    "heimdal-devel",
    "libsecret-devel",
    "gdm-devel",
    "libpwquality-devel",
    "libnma-devel",
    "libadwaita-devel",
]
depends = ["dconf"]
pkgdesc = "GNOME initial setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b1afe764798f8948bedb95c7ab31bd78529ac5cb481c41f7a7777f264de54bd8"
# FIXME cfi
hardening = ["vis", "!cfi"]
