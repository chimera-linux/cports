pkgname = "gnome-text-editor"
pkgver = "45.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "editorconfig-devel",
    "enchant-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "icu-devel",
    "libadwaita-devel",
    "pcre2-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f3ffcb11a92dfd04ba3c3b3d0e667847d4449a21e012ae36f07dda05ac7d3a52"
