pkgname = "gnome-calendar"
pkgver = "44.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "itstool",
    "gobject-introspection", "gtk-update-icon-cache", "desktop-file-utils",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "evolution-data-server-devel",
    "gsettings-desktop-schemas-devel", "libgweather-devel", "libical-devel",
    "geoclue-devel", "libpeas-devel", "libsoup-devel",
]
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME calendar"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "30a1b738b670bd124e462468e671187fc0dba5b9ee2af6a8ebd9e7874bf3b77e"
