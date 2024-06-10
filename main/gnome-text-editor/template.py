pkgname = "gnome-text-editor"
pkgver = "46.3"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dbugreport_url=https://github.com/chimera-linux/cports/issues",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "editorconfig-devel",
    "enchant-devel",
    "gtksourceview-devel",
    "icu-devel",
    "libadwaita-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "005b48104a909be66ae07448d2bc5706c7d113781057a24ff6da55bdf324c73d"
