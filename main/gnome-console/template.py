pkgname = "gnome-console"
pkgver = "47.0"
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
source = (
    f"$(GNOME_SITE)/gnome-console/{pkgver[:-2]}/gnome-console-{pkgver}.tar.xz"
)
sha256 = "487ec0de0a24f12ef6f778e4aee98d744a9dcc921c9e7df98b2d9f410b00ef52"
