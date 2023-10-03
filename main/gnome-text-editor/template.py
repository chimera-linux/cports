pkgname = "gnome-text-editor"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gtk-update-icon-cache",
    "gettext",
    "vala",
    "itstool",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libadwaita-devel",
    "pcre2-devel",
    "enchant-devel",
    "gtksourceview-devel",
    "editorconfig-devel",
    "icu-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "47b3fbe4900eb204413d9af3ae8e0ecd06728d2ac15d02b1a050d02d47226bc1"
