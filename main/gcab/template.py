pkgname = "gcab"
pkgver = "1.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Ddocs=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "vala",
    "gobject-introspection",
    "gettext-tiny",
]
makedepends = ["glib-devel", "vala"]
pkgdesc = "GObject library to create cabinet files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/msitools"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2f0c9615577c4126909e251f9de0626c3ee7a152376c15b5544df10fc87e560b"
options = ["!cross"]


@subpackage("gcab-devel")
def _devel(self):
    return self.default_devel()
