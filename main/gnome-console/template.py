pkgname = "gnome-console"
pkgver = "47_rc"
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
source = f"$(GNOME_SITE)/gnome-console/{pkgver[:2]}/gnome-console-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "6635ee73edef14f2f2cda3d818d84cf673ee3ca06ea554995a9c44c299f2dd6c"
