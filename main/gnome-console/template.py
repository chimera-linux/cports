pkgname = "gnome-console"
pkgver = "48.0.1"
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
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/console"
source = (
    f"$(GNOME_SITE)/gnome-console/{pkgver[:-4]}/gnome-console-{pkgver}.tar.xz"
)
sha256 = "018e908e4daebcfcb150d4f1bb28d98272aa9d14d6815eaf8da45f889db05c49"
