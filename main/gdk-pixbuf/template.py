pkgname = "gdk-pixbuf"
pkgver = "2.44.4"
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
sha256 = "93a1aac3f1427ae73457397582a2c38d049638a801788ccbd5f48ca607bdbd17"
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
