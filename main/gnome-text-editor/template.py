pkgname = "gnome-text-editor"
pkgver = "45.2"
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
sha256 = "0e2552fdb3025446cdad9d59b13d75df9a653fc3ea1dc43b919e0f6fa8a846ac"
