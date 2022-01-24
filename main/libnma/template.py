pkgname = "libnma"
pkgver = "1.8.34"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "vala", "glib-devel",
    "gettext-tiny",
]
makedepends = [
    "networkmanager-devel", "gcr-devel", "gtk+3-devel",
    "mobile-broadband-provider-info", "iso-codes",
]
depends = ["networkmanager", "iso-codes"]
pkgdesc = "NetworkManager GNOME applet runtime library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnma"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "49372986f84d23e7fef1471d87ec964c6ab57169f5dfc597b279a5e6aa01b882"

@subpackage("libnma-devel")
def _devel(self):
    return self.default_devel()
