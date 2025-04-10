pkgname = "gdk-pixbuf"
pkgver = "2.42.12"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dinstalled_tests=false",
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
source = f"$(GNOME_SITE)/gdk-pixbuf/{pkgver[:-3]}/gdk-pixbuf-{pkgver}.tar.xz"
sha256 = "b9505b3445b9a7e48ced34760c3bcb73e966df3ac94c95a148cb669ab748e3c7"
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
