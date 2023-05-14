pkgname = "gnome-text-editor"
pkgver = "44.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-update-icon-cache",
    "gettext-tiny", "vala", "itstool", "desktop-file-utils",
]
makedepends = [
    "gtk4-devel", "glib-devel", "libadwaita-devel", "pcre2-devel",
    "enchant-devel", "gtksourceview-devel", "editorconfig-devel",
    "icu-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f67bc3780734ffa815fcc4c5daa7b555d24e459f81ea2b548e6a85c1612a31ca"
