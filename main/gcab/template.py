pkgname = "gcab"
pkgver = "1.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Ddocs=false"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "vala"]
pkgdesc = "GObject library to create cabinet files"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/msitools"
source = f"$(GNOME_SITE)/gcab/{pkgver}/gcab-{pkgver}.tar.xz"
sha256 = "2f0c9615577c4126909e251f9de0626c3ee7a152376c15b5544df10fc87e560b"
options = ["!cross"]


@subpackage("gcab-devel")
def _(self):
    return self.default_devel()
