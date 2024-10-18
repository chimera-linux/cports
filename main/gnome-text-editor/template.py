pkgname = "gnome-text-editor"
pkgver = "47.1"
pkgrel = 0
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
    "libspelling-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/gnome-text-editor/{pkgver[:-2]}/gnome-text-editor-{pkgver}.tar.xz"
sha256 = "de95642e2b40ff265feecd86b939e0fd018e4eb2ba499350f2bad2bfcc54010c"
