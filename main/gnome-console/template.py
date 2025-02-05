pkgname = "gnome-console"
pkgver = "47.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "pcre2-devel",
    "vte-gtk4-devel",
]
pkgdesc = "GNOME console"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/console"
source = (
    f"$(GNOME_SITE)/gnome-console/{pkgver[:-2]}/gnome-console-{pkgver}.tar.xz"
)
sha256 = "d3f600b45b51716691aee92870332e9c9a8ca89d553565f3131d9e28074725d0"
