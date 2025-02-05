pkgname = "gnome-text-editor"
pkgver = "47.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbugreport_url=https://github.com/chimera-linux/cports/issues",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
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
    "libspelling-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/gnome-text-editor/{pkgver[:-2]}/gnome-text-editor-{pkgver}.tar.xz"
sha256 = "46c672bfe86e44de980797636a280f05cc5eaf6cde9b42dc4bcc956405629725"
