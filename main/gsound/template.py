pkgname = "gsound"
pkgver = "1.0.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
    "-Denable_vala=true",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
]
makedepends = ["libcanberra-devel", "vala"]
pkgdesc = "Small library for playing system sounds"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GSound"
source = f"$(GNOME_SITE)/gsound/{pkgver[:-2]}/gsound-{pkgver}.tar.xz"
sha256 = "ca2d039e1ebd148647017a7f548862350bc9af01986d39f10cfdc8e95f07881a"


@subpackage("gsound-devel")
def _devel(self):
    return self.default_devel()
