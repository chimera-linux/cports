pkgname = "gdk-pixbuf"
pkgver = "2.44.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dinstalled_tests=false",
    "-Dglycin=enabled",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "glycin-loaders-none",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "glib-devel",
    "glycin-devel",
    "glycin-loaders-none",
    "shared-mime-info",
]
checkdepends = []
depends = ["shared-mime-info"]
triggers = ["/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders"]
pkgdesc = "Image loading library for GTK"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GdkPixbuf"
source = f"$(GNOME_SITE)/gdk-pixbuf/{pkgver[:-2]}/gdk-pixbuf-{pkgver}.tar.xz"
sha256 = "172f80e3626ec31520a970400f1a3694e04718f6c2cd2885f75250fb5a6995a4"
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
