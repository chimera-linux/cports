pkgname = "libadwaita"
pkgver = "1.5.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=true",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "sassc",
    "vala-devel",
]
makedepends = [
    "appstream-devel",
    "glib-devel",
    "gtk4-devel",
    "harfbuzz-devel",
]
checkdepends = ["fonts-cantarell-otf", "xwayland-run"]
pkgdesc = "GTK4 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/libadwaita/{pkgver[:-2]}/libadwaita-{pkgver}.tar.xz"
sha256 = "7f144c5887d6dd2d99517c00fd42395ee20abc13ce55958a4fda64e6d7e473f8"
options = ["!cross"]


@subpackage("libadwaita-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libadwaita-demo")
def _demo(self):
    self.pkgdesc = f"{pkgdesc} (demo application)"
    return [
        "usr/bin/adwaita-1-demo",
        "usr/share",
    ]
