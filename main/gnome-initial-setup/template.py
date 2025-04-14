pkgname = "gnome-initial-setup"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
    "gsettings-desktop-schemas-devel",
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
    "webkitgtk4-devel",
]
depends = ["dconf"]
pkgdesc = "GNOME initial setup"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/gnome-initial-setup/{pkgver[:-2]}/gnome-initial-setup-{pkgver}.tar.xz"
sha256 = "b3dabf7e79b665ff12241fbdba615489513d886224759986af8f48657592315e"
