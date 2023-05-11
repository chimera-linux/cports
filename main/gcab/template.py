pkgname = "gcab"
pkgver = f"1.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Ddocs=false"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "vala", "gobject-introspection",
    "gettext-tiny",
]
makedepends = ["glib-devel", "vala"]
pkgdesc = "GObject library to create cabinet files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/msitools"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "46bf7442491faa4148242b9ec2a0786a5f6e9effb1b0566e5290e8cc86f00f0c"
options = ["!cross"]

@subpackage("gcab-devel")
def _devel(self):
    return self.default_devel()
