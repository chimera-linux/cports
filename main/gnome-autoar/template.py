pkgname = "gnome-autoar"
pkgver = "0.4.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dvapi=true",
    "-Dtests=true",
    "-Dgtk_doc=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["gtk+3-devel", "libarchive-devel"]
pkgdesc = "Archiving functions and widgets for GNOME"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-autoar"
source = (
    f"$(GNOME_SITE)/gnome-autoar/{pkgver[:-2]}/gnome-autoar-{pkgver}.tar.xz"
)
sha256 = "838c5306fc38bfaa2f23abe24262f4bf15771e3303fb5dcb74f5b9c7a615dabe"
options = ["!cross"]


@subpackage("gnome-autoar-devel")
def _(self):
    return self.default_devel()
