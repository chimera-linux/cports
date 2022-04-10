pkgname = "gnome-initial-setup"
pkgver = "42.1"
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
    "libnma-devel", "libhandy-devel",
]
pkgdesc = "GNOME initial setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "866136ca32922f7cc424d3adc6b1dba7cebe07aa96a19f97c80770e3f2eea71b"
