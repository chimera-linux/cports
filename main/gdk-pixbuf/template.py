pkgname = "gdk-pixbuf"
pkgver = "2.44.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dinstalled_tests=false",
    # ugly depcycle, figure out later
    "-Dglycin=disabled",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "glib-devel",
    "libpng-devel",
    "libtiff-devel",
    "shared-mime-info",
]
depends = ["shared-mime-info"]
triggers = ["/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders"]
pkgdesc = "Image loading library for GTK"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GdkPixbuf"
source = f"$(GNOME_SITE)/gdk-pixbuf/{pkgver[:-2]}/gdk-pixbuf-{pkgver}.tar.xz"
sha256 = "40a92dcc237ff94b63a80c159a3f6f22cd59f6fb4961f201c78799fa2c8ac0a6"
# FIXME int
hardening = ["!int"]
# check may be disabled
options = ["!cross"]

if self.profile().wordsize == 32:
    # https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/issues/215
    options += ["!check"]


@subpackage("gdk-pixbuf-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/bin/*csource*",
            "usr/share/man/man1/*csource*",
        ]
    )
