pkgname = "gnome-text-editor"
pkgver = "48.1"
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
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-text-editor"
source = f"$(GNOME_SITE)/gnome-text-editor/{pkgver[:-2]}/gnome-text-editor-{pkgver}.tar.xz"
sha256 = "52089ba978a665841803b1b69e0e7be75b09a7d54e01e8d0bb29926e0f342437"
