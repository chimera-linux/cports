pkgname = "gnome-console"
pkgver = "46.0"
pkgrel = 2
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
source = (
    f"$(GNOME_SITE)/gnome-console/{pkgver[:-2]}/gnome-console-{pkgver}.tar.xz"
)
sha256 = "1619ce701773b2c0c903718f54768c192ea5074514d55a1774a92c97231d6c3e"
