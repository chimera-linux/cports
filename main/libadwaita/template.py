pkgname = "libadwaita"
pkgver = "1.7.5"
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
sha256 = "c2c1813c967d45c0f49e907f8c26e66f68fe49dec6436e2d3349350ac9efbd2e"
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
