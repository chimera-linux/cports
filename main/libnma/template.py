pkgname = "libnma"
pkgver = "1.8.38"
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
sha256 = "241c7202c88af3a83331830c210958866b15c858fab3733bf663837d14d40640"

@subpackage("libnma-devel")
def _devel(self):
    return self.default_devel()
