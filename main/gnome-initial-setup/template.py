pkgname = "gnome-initial-setup"
pkgver = "41.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dparental_controls=disabled", "-Dcheese=disabled", "-Dsystemd=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny"
]
makedepends = [
    "ibus-devel", "networkmanager-devel", "accountsservice-devel",
    "polkit-devel", "gnome-desktop-devel", "gsettings-desktop-schemas-devel",
    "fontconfig-devel", "libgweather-devel", "gnome-online-accounts-devel",
    "gtk+3-devel", "libglib-devel", "webkitgtk-devel", "geocode-glib-devel",
    "geoclue-devel", "pango-devel", "rest-devel", "json-glib-devel",
    "heimdal-devel", "libsecret-devel", "libpwquality-devel", "gdm-devel",
    "libnma-devel",
]
pkgdesc = "GNOME initial setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "193afbf6a3082da0a32a7714f1e8d52a8db457272975ed2f3654364a33391b3f"
