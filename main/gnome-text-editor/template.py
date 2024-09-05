pkgname = "gnome-text-editor"
pkgver = "47_rc"
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
    "gtksourceview-devel",
    "libadwaita-devel",
    "libspelling-devel",
]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/gnome-text-editor/{pkgver[:2]}/gnome-text-editor-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "b53162ca9e73658d4e3b67b5d19bdad9b16962c125801d2bcba7a040ab1e8ceb"
