pkgname = "libadwaita"
pkgver = "1.7.0"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/libadwaita/{pkgver[:-2]}/libadwaita-{pkgver}.tar.xz"
sha256 = "58bf99b8a9f8b0171964de0ae741d01d5a09db3662134fa67541c99a8ed7dec0"
options = ["!cross"]


@subpackage("libadwaita-devel")
def _(self):
    return self.default_devel()


@subpackage("libadwaita-demo")
def _(self):
    self.subdesc = "demo application"
    return [
        "usr/bin/adwaita-1-demo",
        "usr/share",
    ]
