pkgname = "gnome-console"
pkgver = "44.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "vte-gtk4-devel",
    "libgtop-devel",
    "gsettings-desktop-schemas-devel",
    "pcre2-devel",
]
pkgdesc = "GNOME console"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/console"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b91f44e9a6c0433e96d997f395585206dabac62473993a3c07552fe5888e5a8d"
