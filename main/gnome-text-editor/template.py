pkgname = "gnome-text-editor"
pkgver = "45.1"
pkgrel = 1
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
sha256 = "6a86ec9920f466b6ed92695524d3b507b1e84272dafa5341d06a157de868af71"
